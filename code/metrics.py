"""
metrics.py — honest, risk-adjusted scorekeeping vs SPY.

Judging a strategy on "did it beat SPY this month" gets it abandoned at the worst
time. So this reports what actually matters over the long run — Sharpe ratio, max
drawdown, volatility, MAR (return per unit of drawdown), and LIMIT fill rate — each
next to SPY for context. It also writes an honest end-of-day summary.

Every fill number comes from reconciled orders (Alpaca is the source of truth). We
never assume a fill.

Usage:
    python3 code/metrics.py                 # long-run plain-English report
    python3 code/metrics.py --json          # long-run report as JSON
    python3 code/metrics.py --summary       # write state/runs/<today>-summary.json
    python3 code/metrics.py --summary --date 2026-06-16
"""

from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY_FILE = ROOT / "state" / "portfolio_history.jsonl"
COMPLETED_DIR = ROOT / "state" / "completed_trades"
PORTFOLIO_FILE = ROOT / "state" / "portfolio.json"
RUNS_DIR = ROOT / "state" / "runs"

RISK_FREE_RATE = float(os.environ.get("RISK_FREE_RATE", "0.045"))


# ----------------------------- equity-series math -----------------------------

def load_equity_series() -> list[dict]:
    if not HISTORY_FILE.exists():
        return []
    by_day: dict[str, float] = {}
    for line in HISTORY_FILE.read_text().splitlines():
        try:
            d = json.loads(line)
            by_day[d["timestamp_utc"][:10]] = float(d["equity"])
        except Exception:
            continue
    return [{"date": k, "equity": by_day[k]} for k in sorted(by_day)]


def daily_returns(values: list[float]) -> list[float]:
    return [values[i] / values[i - 1] - 1 for i in range(1, len(values)) if values[i - 1] > 0]


def sharpe(values: list[float], rf: float = RISK_FREE_RATE) -> float | None:
    rets = daily_returns(values)
    if len(rets) < 2:
        return None
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    sd = math.sqrt(var)
    if sd <= 0:
        return None
    daily_rf = (1 + rf) ** (1 / 252) - 1
    return (mean - daily_rf) / sd * math.sqrt(252)


def max_drawdown(values: list[float]) -> float:
    if not values:
        return 0.0
    hwm, mdd = values[0], 0.0
    for v in values:
        hwm = max(hwm, v)
        if hwm > 0:
            mdd = min(mdd, v / hwm - 1)
    return mdd


def annualized_vol(values: list[float]) -> float:
    rets = daily_returns(values)
    if len(rets) < 2:
        return 0.0
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var) * math.sqrt(252)


def cagr(values: list[float]) -> float | None:
    if len(values) < 2 or values[0] <= 0:
        return None
    years = len(values) / 252
    if years <= 0:
        return None
    return (values[-1] / values[0]) ** (1 / years) - 1


# ----------------------------- fills & round-trips -----------------------------

def _filled_trades() -> list[dict]:
    out = []
    if not COMPLETED_DIR.exists():
        return out
    for path in COMPLETED_DIR.glob("*.json"):
        try:
            t = json.loads(path.read_text())
        except Exception:
            continue
        if str(t.get("status", "")).lower() in ("filled", "partially_filled") and float(t.get("filled_qty") or 0) > 0:
            out.append(t)
    out.sort(key=lambda t: str(t.get("submitted_at_utc", "")))
    return out


def realized_roundtrips() -> tuple[list[dict], float]:
    """FIFO-match SELLs to earlier BUYs per ticker to compute realized profit/loss."""
    lots: dict[str, list[list]] = {}   # ticker -> [[qty, price], ...]
    roundtrips: list[dict] = []
    total = 0.0
    for t in _filled_trades():
        tkr = str(t.get("ticker", "")).upper()
        qty = float(t.get("filled_qty") or 0)
        price = float(t.get("filled_avg_price") or t.get("limit_price") or 0)
        side = str(t.get("side", "")).upper()
        when = str(t.get("reconciled_at_utc") or t.get("submitted_at_utc", ""))[:10]
        if side == "BUY":
            lots.setdefault(tkr, []).append([qty, price])
        elif side == "SELL":
            remaining = qty
            q = lots.get(tkr, [])
            while remaining > 1e-9 and q:
                lot = q[0]
                matched = min(remaining, lot[0])
                pnl = (price - lot[1]) * matched
                total += pnl
                roundtrips.append({
                    "ticker": tkr, "qty": round(matched, 4),
                    "buy_price": round(lot[1], 2), "sell_price": round(price, 2),
                    "pnl": round(pnl, 2), "closed_date": when,
                })
                lot[0] -= matched
                remaining -= matched
                if lot[0] <= 1e-9:
                    q.pop(0)
    return roundtrips, round(total, 2)


def fill_rate() -> tuple[float | None, dict]:
    details = {"final_orders": 0, "filled": 0, "partial": 0, "unfilled": 0, "pending": 0}
    if not COMPLETED_DIR.exists():
        return None, details
    for path in COMPLETED_DIR.glob("*.json"):
        try:
            t = json.loads(path.read_text())
        except Exception:
            continue
        status = str(t.get("status", "")).lower()
        if status in ("submitted", "accepted", "pending_new", "new"):
            details["pending"] += 1
            continue
        details["final_orders"] += 1
        fq = float(t.get("filled_qty") or 0)
        q = float(t.get("qty") or 0)
        if fq <= 0:
            details["unfilled"] += 1
        elif q and fq >= q:
            details["filled"] += 1
        else:
            details["partial"] += 1
    final = details["final_orders"]
    rate = (details["filled"] / final) if final else None
    return rate, details


def unrealized_pl() -> float | None:
    try:
        p = json.loads(PORTFOLIO_FILE.read_text())
        return round(sum(float(pos.get("unrealized_pl", 0)) for pos in p.get("positions", [])), 2)
    except Exception:
        return None


# ----------------------------- SPY benchmark -----------------------------

def spy_series_for(dates: list[str]) -> list[float] | None:
    if len(dates) < 2:
        return None
    span = 30
    try:
        from datetime import date
        span = (date.fromisoformat(dates[-1]) - date.fromisoformat(dates[0])).days + 15
    except Exception:
        pass
    try:
        out = subprocess.run(
            [sys.executable, "code/alpaca_client.py", "--bars", "SPY", "--days", str(max(span, 20))],
            cwd=ROOT, text=True, capture_output=True,
        )
        if out.returncode != 0:
            return None
        bars = json.loads(out.stdout).get("bars", [])
    except Exception:
        return None
    by_day = {b["t"][:10]: float(b["c"]) for b in bars}
    aligned, last = [], None
    for d in dates:
        for bd in sorted(by_day):
            if bd <= d:
                last = by_day[bd]
        if last is not None:
            aligned.append(last)
    return aligned if len(aligned) >= 2 else None


def build_report() -> dict:
    series = load_equity_series()
    if len(series) < 2:
        return {"error": "Not enough history yet — run the bot for at least two days."}
    values = [s["equity"] for s in series]
    dates = [s["date"] for s in series]
    rate, fill_details = fill_rate()
    spy = spy_series_for(dates)
    _, realized = realized_roundtrips()

    report = {
        "as_of": dates[-1], "started": dates[0], "days_of_history": len(series),
        "equity": round(values[-1], 2),
        "total_return": round(values[-1] / values[0] - 1, 4),
        "realized_pnl": realized,
        "unrealized_pnl": unrealized_pl(),
        "sharpe": round(sharpe(values), 2) if sharpe(values) is not None else None,
        "max_drawdown": round(max_drawdown(values), 4),
        "annualized_vol": round(annualized_vol(values), 4),
        "fill_rate": round(rate, 3) if rate is not None else None,
        "fill_details": fill_details,
    }
    cg = cagr(values)
    mdd = max_drawdown(values)
    report["mar"] = round(cg / abs(mdd), 2) if cg is not None and mdd < 0 else None
    if spy:
        report["spy_total_return"] = round(spy[-1] / spy[0] - 1, 4)
        report["spy_sharpe"] = round(sharpe(spy), 2) if sharpe(spy) is not None else None
        report["spy_max_drawdown"] = round(max_drawdown(spy), 4)
        report["spy_annualized_vol"] = round(annualized_vol(spy), 4)
    return report


# ----------------------------- day summary -----------------------------

def _todays(date_str: str) -> list[dict]:
    if not COMPLETED_DIR.exists():
        return []
    out = []
    for path in COMPLETED_DIR.glob("*.json"):
        try:
            t = json.loads(path.read_text())
        except Exception:
            continue
        if str(t.get("submitted_at_utc", ""))[:10] == date_str:
            out.append(t)
    return out


def build_day_summary(date_str: str) -> dict:
    todays = _todays(date_str)
    buys = [t for t in todays if str(t.get("side", "")).upper() == "BUY"]
    sells = [t for t in todays if str(t.get("side", "")).upper() == "SELL"]
    budget_used = sum(float(t.get("limit_price", 0)) * float(t.get("qty", 0)) for t in buys)
    roundtrips, realized_total = realized_roundtrips()
    realized_today = round(sum(r["pnl"] for r in roundtrips if r["closed_date"] == date_str), 2)
    rate, fill_details = fill_rate()

    portfolio = {}
    try:
        portfolio = json.loads(PORTFOLIO_FILE.read_text())
    except Exception:
        pass

    long_run = build_report()
    summary = {
        "date": date_str,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "equity": portfolio.get("equity"),
        "cash": portfolio.get("cash"),
        "drawdown_from_hwm": portfolio.get("drawdown_from_hwm"),
        "num_holdings": len(portfolio.get("positions", [])),
        "trades_today": len(todays),
        "buys_today": len(buys),
        "sells_today": len(sells),
        "budget_used_today_usd": round(budget_used, 2),
        "realized_pnl_today": realized_today,
        "realized_pnl_total": realized_total,
        "unrealized_pnl": unrealized_pl(),
        "fill_rate": round(rate, 3) if rate is not None else None,
        "fill_details": fill_details,
        "spy_total_return": long_run.get("spy_total_return"),
        "total_return": long_run.get("total_return"),
    }
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    (RUNS_DIR / f"{date_str}-summary.json").write_text(json.dumps(summary, indent=2))
    return summary


def print_plain(r: dict) -> None:
    if "error" in r:
        print(r["error"])
        return
    print(f"RISK-ADJUSTED REPORT — as of {r['as_of']} (started {r['started']}, {r['days_of_history']} days)")
    print(f"  Account value:       ${r['equity']:,.2f}   (total return {r['total_return']:+.2%})")
    print(f"  Realized P&L:        ${r['realized_pnl']:,.2f}   Unrealized: ${(r['unrealized_pnl'] or 0):,.2f}")
    print(f"  Sharpe ratio:        {r['sharpe']}" + (f"   vs SPY {r['spy_sharpe']}" if r.get('spy_sharpe') is not None else ""))
    print(f"  Max drawdown:        {r['max_drawdown']:.2%}" + (f"   vs SPY {r['spy_max_drawdown']:.2%}" if r.get('spy_max_drawdown') is not None else ""))
    print(f"  Annualized vol:      {r['annualized_vol']:.2%}" + (f"   vs SPY {r['spy_annualized_vol']:.2%}" if r.get('spy_annualized_vol') is not None else ""))
    print(f"  MAR (return/drawdn): {r['mar']}")
    if r["fill_rate"] is not None:
        fd = r["fill_details"]
        print(f"  LIMIT fill rate:     {r['fill_rate']:.0%}  ({fd['filled']} filled / {fd['final_orders']} final, {fd['pending']} pending)")
    else:
        print("  LIMIT fill rate:     no completed orders yet")
    print("  Reminder: judge this on Sharpe / drawdown vs SPY, not on raw return.")


def main() -> int:
    sys.path.insert(0, str(ROOT / "code"))
    from clockutil import et_today_str
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--date", default=None)
    args = parser.parse_args()

    if args.summary:
        date_str = args.date or et_today_str()
        print(json.dumps(build_day_summary(date_str), indent=2))
        return 0

    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_plain(report)
    return 0 if "error" not in report else 1


if __name__ == "__main__":
    raise SystemExit(main())
