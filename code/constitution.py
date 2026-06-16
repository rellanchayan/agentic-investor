"""
constitution.py — programmatic guardrails for the long-term investor.

These are HARD limits. They live in code (not config) so a corrupted config or a
confused agent can never loosen them. The checks run inside
`alpaca_client.submit()`, so no order reaches Alpaca without passing every one.

Run as a script:
    python3 code/constitution.py --check state/pending_trades/<trade_id>.json

Exit code 0 = PASS, non-zero = FAIL. Stdout is human-readable.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
HALT_FILE = ROOT / ".HALT_TRADING"
PORTFOLIO_FILE = ROOT / "state" / "portfolio.json"
COMPLETED_DIR = ROOT / "state" / "completed_trades"
THESES_DIR = ROOT / "state" / "theses"

# ------ Hard limits (inviolable; the tuner can NEVER touch these) ------

MAX_POSITION_PCT = 0.25          # ≤ 25% of equity in any one ticker
MAX_OPEN_POSITIONS = 8           # at most 8 holdings at once
MAX_TRADES_PER_DAY = 20
MAX_TRADES_PER_WEEK = 50
# The strict daily budget: most we will deploy into NEW buys in a single day.
# Selling to raise cash / reduce risk is NEVER capped.
MAX_DAILY_INVEST_USD = 5000.0
# A single buy can never exceed the whole daily budget.
MAX_PER_TRADE_USD = 5000.0

# Leveraged / inverse / volatility ETFs and the like — never allowed.
FORBIDDEN_SUBSTRINGS_IN_SYMBOL = {
    # leveraged
    "TQQQ", "SQQQ", "UPRO", "SPXU", "SOXL", "SOXS", "TNA", "TZA", "LABU", "LABD",
    "FAS", "FAZ", "TMF", "TMV", "UVXY", "VIXY", "SVXY", "VXX", "UDOW", "SDOW",
    "SPXL", "SPXS", "QLD", "SDS", "SSO", "TSLL", "NVDL",
    # inverse
    "SH", "PSQ", "DOG", "RWM", "SEF",
}


@dataclass
class CheckResult:
    name: str
    passed: bool
    note: str = ""

    def __str__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"  [{status}] {self.name}{(': ' + self.note) if self.note else ''}"


class ConstitutionViolation(Exception):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConstitutionViolation(f"required file missing: {path}")
    with path.open() as f:
        return json.load(f)


def check_halt_switch() -> CheckResult:
    if HALT_FILE.exists():
        return CheckResult("halt_switch", False, f"{HALT_FILE.name} exists — trading is halted")
    return CheckResult("halt_switch", True)


def check_live_mode_forbidden() -> CheckResult:
    """Hard refuse anything that is not the paper endpoint. Paper only, always."""
    endpoint = os.environ.get("ALPACA_ENDPOINT", "")
    if "paper-api.alpaca.markets" not in endpoint:
        return CheckResult(
            "live_mode_forbidden", False,
            f"ALPACA_ENDPOINT must be paper-api.alpaca.markets, got: {endpoint!r}",
        )
    if os.environ.get("LIVE_TRADING_AUTHORIZED", "").lower() == "true":
        return CheckResult(
            "live_mode_forbidden", False,
            "LIVE_TRADING_AUTHORIZED is true; this build operates paper-only.",
        )
    return CheckResult("live_mode_forbidden", True)


def check_forbidden_instrument(trade: dict) -> CheckResult:
    ticker = trade.get("ticker", "").upper()
    if ticker in FORBIDDEN_SUBSTRINGS_IN_SYMBOL:
        return CheckResult("forbidden_instrument", False, f"{ticker} is on the denylist (leveraged/inverse/vol)")
    # Refuse anything that looks like an option/contract symbol (mix of digits + length).
    if any(c.isdigit() for c in ticker) and len(ticker) > 6:
        return CheckResult("forbidden_instrument", False, f"{ticker} looks like an option/contract symbol")
    if not ticker.isalpha() or not (1 <= len(ticker) <= 5):
        return CheckResult("forbidden_instrument", False, f"{ticker!r} is not a plain stock/ETF ticker")
    return CheckResult("forbidden_instrument", True)


def check_side(trade: dict) -> CheckResult:
    side = trade.get("side", "").upper()
    if side not in {"BUY", "SELL"}:
        return CheckResult("side", False, f"side must be BUY or SELL, got {side!r}")
    return CheckResult("side", True)


def check_order_type(trade: dict) -> CheckResult:
    order_type = trade.get("order_type", "LIMIT").upper()
    tif = trade.get("time_in_force", "DAY").upper()
    if order_type != "LIMIT":
        return CheckResult("order_type", False, f"order_type must be LIMIT, got {order_type}")
    if tif != "DAY":
        return CheckResult("order_type", False, f"time_in_force must be DAY, got {tif}")
    return CheckResult("order_type", True)


def check_position_size(trade: dict, portfolio: dict) -> CheckResult:
    """A BUY's resulting position must stay within the 25%-per-name cap."""
    if trade["side"].upper() != "BUY":
        return CheckResult("position_size", True, "sell — not applicable")
    equity = float(portfolio.get("equity", 0))
    if equity <= 0:
        return CheckResult("position_size", False, "portfolio equity unknown — cannot size-check")
    ticker = trade["ticker"].upper()
    notional = float(trade["limit_price"]) * float(trade["qty"])
    current_pos_value = 0.0
    for pos in portfolio.get("positions", []):
        if pos["ticker"].upper() == ticker:
            current_pos_value = float(pos["market_value"])
            break
    post_pct = (current_pos_value + notional) / equity
    if post_pct > MAX_POSITION_PCT:
        return CheckResult("position_size", False,
                           f"post-trade position would be {post_pct:.1%} > {MAX_POSITION_PCT:.0%} cap")
    return CheckResult("position_size", True, f"post-trade position {post_pct:.1%}")


def check_max_open_positions(trade: dict, portfolio: dict) -> CheckResult:
    """A BUY of a brand-new name must not push us past the 8-holding ceiling."""
    if trade["side"].upper() != "BUY":
        return CheckResult("max_open_positions", True, "sell — not applicable")
    held = {p["ticker"].upper() for p in portfolio.get("positions", [])}
    ticker = trade["ticker"].upper()
    if ticker in held:
        return CheckResult("max_open_positions", True, f"already holding {ticker} ({len(held)} names)")
    if len(held) >= MAX_OPEN_POSITIONS:
        return CheckResult("max_open_positions", False,
                           f"already at {len(held)} holdings (max {MAX_OPEN_POSITIONS}); cannot open a new name")
    return CheckResult("max_open_positions", True, f"{len(held)}/{MAX_OPEN_POSITIONS} holdings")


def check_per_trade_cap(trade: dict) -> CheckResult:
    if trade["side"].upper() != "BUY":
        return CheckResult("per_trade_cap", True, "sell — not applicable")
    notional = float(trade["limit_price"]) * float(trade["qty"])
    if notional > MAX_PER_TRADE_USD + 1e-6:
        return CheckResult("per_trade_cap", False,
                           f"single buy ${notional:,.0f} exceeds ${MAX_PER_TRADE_USD:,.0f} per-trade cap")
    return CheckResult("per_trade_cap", True, f"${notional:,.0f} of ${MAX_PER_TRADE_USD:,.0f}")


def check_cash_available(trade: dict, portfolio: dict) -> CheckResult:
    """BUYs must fit in SETTLED CASH — not buying power. This is how we forbid margin."""
    if trade["side"].upper() != "BUY":
        return CheckResult("cash_available", True, "sell — not applicable")
    cash = float(portfolio.get("cash", 0))
    notional = float(trade["limit_price"]) * float(trade["qty"])
    if notional > cash:
        return CheckResult("cash_available", False,
                           f"trade needs ${notional:,.2f}, cash is ${cash:,.2f} (no margin allowed)")
    return CheckResult("cash_available", True, f"trade needs ${notional:,.2f}, cash is ${cash:,.2f}")


def _trades_in_window(days: int) -> int:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    if not COMPLETED_DIR.exists():
        return 0
    count = 0
    for f in COMPLETED_DIR.glob("*.json"):
        try:
            d = json.loads(f.read_text())
            submitted = d.get("submitted_at_utc")
            if submitted and datetime.fromisoformat(submitted.replace("Z", "+00:00")) >= cutoff:
                count += 1
        except Exception:
            continue
    return count


def check_frequency(trade: dict) -> CheckResult:
    day_count = _trades_in_window(1)
    week_count = _trades_in_window(7)
    if day_count >= MAX_TRADES_PER_DAY:
        return CheckResult("frequency", False, f"already {day_count} trades today (max {MAX_TRADES_PER_DAY})")
    if week_count >= MAX_TRADES_PER_WEEK:
        return CheckResult("frequency", False, f"already {week_count} trades this week (max {MAX_TRADES_PER_WEEK})")
    return CheckResult("frequency", True, f"day {day_count}/{MAX_TRADES_PER_DAY}, week {week_count}/{MAX_TRADES_PER_WEEK}")


def _todays_completed() -> list[dict]:
    today = datetime.now(timezone.utc).date().isoformat()
    out: list[dict] = []
    if not COMPLETED_DIR.exists():
        return out
    for f in COMPLETED_DIR.glob("*.json"):
        try:
            d = json.loads(f.read_text())
            if str(d.get("submitted_at_utc", ""))[:10] == today:
                out.append(d)
        except Exception:
            continue
    return out


def check_daily_invest_cap(trade: dict) -> CheckResult:
    """Total BUY dollars submitted today + this order must stay under the $5k/day budget.
    Sells are exempt — reducing risk is never throttled."""
    if trade["side"].upper() != "BUY":
        return CheckResult("daily_invest_cap", True, "sell — not applicable")
    notional = float(trade["limit_price"]) * float(trade["qty"])
    prior = sum(
        float(d.get("limit_price", 0)) * float(d.get("qty", 0))
        for d in _todays_completed() if str(d.get("side", "")).upper() == "BUY"
    )
    if prior + notional > MAX_DAILY_INVEST_USD + 1e-6:
        return CheckResult("daily_invest_cap", False,
                           f"today's buys ${prior:,.0f} + ${notional:,.0f} would exceed ${MAX_DAILY_INVEST_USD:,.0f}/day budget")
    return CheckResult("daily_invest_cap", True, f"${prior + notional:,.0f} of ${MAX_DAILY_INVEST_USD:,.0f}/day")


def check_no_day_trade(trade: dict) -> CheckResult:
    """No same-day round trips. We are an investor, not a day trader."""
    ticker = trade.get("ticker", "").upper()
    side = trade.get("side", "").upper()
    opposite = "SELL" if side == "BUY" else "BUY"
    for d in _todays_completed():
        if str(d.get("ticker", "")).upper() == ticker and str(d.get("side", "")).upper() == opposite:
            return CheckResult("no_day_trade", False,
                               f"{ticker} already had a {opposite} today — a {side} now would be a same-day round trip")
    return CheckResult("no_day_trade", True)


def check_trade_reason(trade: dict) -> CheckResult:
    reason = trade.get("reason") or trade.get("thesis")
    if not reason or len(str(reason).strip()) < 10:
        return CheckResult("trade_reason", False, "missing a real written reason (no reason = no trade)")
    return CheckResult("trade_reason", True)


def check_thesis_cited(trade: dict) -> CheckResult:
    """Every BUY must reference a real, cached research thesis. No thesis = no buy.
    Sells are exempt so we can always reduce risk on a name."""
    if trade["side"].upper() != "BUY":
        return CheckResult("thesis_cited", True, "sell — not applicable")
    thesis_id = str(trade.get("thesis_id", "")).strip()
    if not thesis_id:
        return CheckResult("thesis_cited", False, "BUY has no thesis_id — every buy must cite a thesis")
    ticker = trade.get("ticker", "").upper()
    thesis_file = THESES_DIR / f"{ticker}.json"
    if not thesis_file.exists():
        return CheckResult("thesis_cited", False,
                           f"no thesis file at state/theses/{ticker}.json — research the name first")
    return CheckResult("thesis_cited", True, f"thesis {thesis_id}")


def run_all_checks(trade_path: Path) -> tuple[bool, list[CheckResult]]:
    trade = _load_json(trade_path)
    portfolio = _load_json(PORTFOLIO_FILE) if PORTFOLIO_FILE.exists() else {"equity": 0, "cash": 0, "positions": []}

    results: list[CheckResult] = [
        check_halt_switch(),
        check_live_mode_forbidden(),
        check_forbidden_instrument(trade),
        check_side(trade),
        check_order_type(trade),
        check_position_size(trade, portfolio),
        check_max_open_positions(trade, portfolio),
        check_per_trade_cap(trade),
        check_cash_available(trade, portfolio),
        check_frequency(trade),
        check_daily_invest_cap(trade),
        check_no_day_trade(trade),
        check_trade_reason(trade),
        check_thesis_cited(trade),
    ]
    passed = all(r.passed for r in results)
    return passed, results


def main() -> int:
    if load_dotenv:
        load_dotenv(ROOT / ".env", override=True)
    p = argparse.ArgumentParser()
    p.add_argument("--check", required=True, help="path to trade JSON")
    args = p.parse_args()
    trade_path = Path(args.check)
    if not trade_path.exists():
        print(f"ERROR: trade file not found: {trade_path}", file=sys.stderr)
        return 2

    passed, results = run_all_checks(trade_path)
    print(f"Constitution check: {'PASS' if passed else 'FAIL'} — {trade_path.name}")
    for r in results:
        print(r)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
