"""
screen.py — a mechanical liquidity + trend snapshot of the watchlist.

This does NOT decide quality (that needs real research — the candidate-scout and
research-analyst do that with the web). screen.py just measures the easy, numeric
things from price data so the weekly routine has context:
  * current price, 50-day and 200-day moving averages (trend),
  * 6-month price change,
  * average dollar volume over 20 days (how easy it is to trade — "liquidity"),
  * a simple "liquid?" flag.

A moving average is just the average closing price over the last N days; price above
it usually means an uptrend. We use prices ONLY from Alpaca.

Usage:
    python3 code/screen.py            # print + write state/day/<today>/screen.json
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clockutil import et_today_str  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WATCHLIST_FILE = ROOT / "state" / "watchlist.txt"
MIN_AVG_DOLLAR_VOL = 20_000_000  # $20M/day traded = comfortably liquid for our size


def _watchlist() -> list[str]:
    if not WATCHLIST_FILE.exists():
        return []
    out = []
    for line in WATCHLIST_FILE.read_text().splitlines():
        line = line.split("#")[0].strip().upper()
        if line and line not in out:
            out.append(line)
    return out


def _bars(ticker: str, days: int = 250) -> list[dict]:
    try:
        out = subprocess.run(
            [sys.executable, "code/alpaca_client.py", "--bars", ticker, "--days", str(days)],
            cwd=ROOT, text=True, capture_output=True,
        )
        if out.returncode != 0:
            return []
        return json.loads(out.stdout).get("bars", [])
    except Exception:
        return []


def _sma(closes: list[float], n: int) -> float | None:
    if len(closes) < n:
        return None
    return sum(closes[-n:]) / n


def screen_one(ticker: str) -> dict:
    bars = _bars(ticker)
    closes = [b["c"] for b in bars]
    vols = [b["v"] for b in bars]
    if len(closes) < 30:
        return {"ticker": ticker, "available": False, "note": f"only {len(closes)} bars"}
    last = closes[-1]
    sma50 = _sma(closes, 50)
    sma200 = _sma(closes, 200)
    ret_6m = (closes[-1] / closes[-126] - 1) if len(closes) >= 126 else None
    n_vol = min(20, len(closes))
    avg_dollar_vol = sum(closes[-n_vol:][i] * vols[-n_vol:][i] for i in range(n_vol)) / n_vol
    return {
        "ticker": ticker,
        "available": True,
        "price": round(last, 2),
        "sma50": round(sma50, 2) if sma50 else None,
        "sma200": round(sma200, 2) if sma200 else None,
        "above_50d": (last > sma50) if sma50 else None,
        "above_200d": (last > sma200) if sma200 else None,
        "ret_6m": round(ret_6m, 4) if ret_6m is not None else None,
        "avg_dollar_vol_20d": round(avg_dollar_vol, 0),
        "liquid": avg_dollar_vol >= MIN_AVG_DOLLAR_VOL,
    }


def run() -> dict:
    rows = [screen_one(t) for t in _watchlist()]
    out = {"date_et": et_today_str(), "rows": rows,
           "illiquid": [r["ticker"] for r in rows if r.get("available") and not r.get("liquid")]}
    day_dir = ROOT / "state" / "day" / out["date_et"]
    day_dir.mkdir(parents=True, exist_ok=True)
    (day_dir / "screen.json").write_text(json.dumps(out, indent=2))
    return out


def main() -> int:
    print(json.dumps(run(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
