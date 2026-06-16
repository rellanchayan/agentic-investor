"""
test_constitution.py — offline unit tests for the hard guardrails.

No network. Redirects the constitution module's file paths to a temp dir so we can
exercise the halt-switch, thesis, daily-budget, and frequency checks deterministically.

Run:  python3 code/tests/test_constitution.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import constitution as C  # noqa: E402

# Paper endpoint so check_live_mode_forbidden passes during tests.
os.environ["ALPACA_ENDPOINT"] = "https://paper-api.alpaca.markets"
os.environ["LIVE_TRADING_AUTHORIZED"] = "false"

PASSED = 0
FAILED = 0


def ok(cond: bool, label: str) -> None:
    global PASSED, FAILED
    if cond:
        PASSED += 1
    else:
        FAILED += 1
        print(f"  FAIL: {label}")


def _sandbox(tmp: Path, *, portfolio: dict, theses=(), completed=(), halt=False):
    """Point the module's paths at a temp dir and seed it."""
    C.HALT_FILE = tmp / ".HALT_TRADING"
    C.PORTFOLIO_FILE = tmp / "portfolio.json"
    C.COMPLETED_DIR = tmp / "completed_trades"
    C.THESES_DIR = tmp / "theses"
    C.COMPLETED_DIR.mkdir(parents=True, exist_ok=True)
    C.THESES_DIR.mkdir(parents=True, exist_ok=True)
    C.PORTFOLIO_FILE.write_text(json.dumps(portfolio))
    if halt:
        C.HALT_FILE.write_text("halt")
    for t in theses:
        (C.THESES_DIR / f"{t}.json").write_text(json.dumps({"ticker": t, "thesis_id": f"{t}-x"}))
    for c in completed:
        (C.COMPLETED_DIR / f"{c['trade_id']}.json").write_text(json.dumps(c))


def _trade(**kw):
    base = {
        "trade_id": "T-1", "ticker": "AAPL", "side": "BUY", "qty": 10, "limit_price": 190.0,
        "order_type": "LIMIT", "time_in_force": "DAY", "reason": "valid reason for a trade here",
        "thesis_id": "AAPL-x",
    }
    base.update(kw)
    return base


def _write_trade(tmp: Path, trade: dict) -> Path:
    p = tmp / f"{trade['trade_id']}.json"
    p.write_text(json.dumps(trade))
    return p


PORTFOLIO_1M = {"equity": 1_000_000.0, "cash": 1_000_000.0, "positions": []}


def run():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)

        # 1. A clean, fully valid BUY passes everything.
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"])
        p = _write_trade(tmp, _trade())
        passed, results = C.run_all_checks(p)
        ok(passed, f"clean BUY should pass; got {[str(r) for r in results if not r.passed]}")

        # 2. Position over 25% cap fails.
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"])
        ok(not C.check_position_size(_trade(qty=2000, limit_price=200.0), PORTFOLIO_1M).passed,
           "position > 25% should fail")  # 2000*200 = 400k > 250k cap

        # 3. 9th new name fails max_open_positions.
        full = {"equity": 1_000_000.0, "cash": 1_000_000.0,
                "positions": [{"ticker": f"S{i}", "market_value": 50_000} for i in range(8)]}
        ok(not C.check_max_open_positions(_trade(ticker="NEWX"), full).passed,
           "9th new name should fail max_open_positions")
        ok(C.check_max_open_positions(_trade(ticker="S0"), full).passed,
           "adding to an existing name should pass max_open_positions")

        # 4. Single buy over $5,000 fails per_trade_cap.
        ok(not C.check_per_trade_cap(_trade(qty=100, limit_price=200.0)).passed,
           "$20k single buy should fail per_trade_cap")
        ok(C.check_per_trade_cap(_trade(qty=10, limit_price=200.0)).passed,
           "$2k single buy should pass per_trade_cap")

        # 5. Not enough cash fails (no margin).
        broke = {"equity": 1_000_000.0, "cash": 100.0, "positions": []}
        ok(not C.check_cash_available(_trade(qty=10, limit_price=190.0), broke).passed,
           "buy beyond cash should fail (no margin)")

        # 6. Daily budget: prior buys + this order over $5,000 fails.
        prior = {"trade_id": "T-prior", "ticker": "MSFT", "side": "BUY",
                 "qty": 10, "limit_price": 400.0,  # $4,000 already today
                 "submitted_at_utc": __import__("datetime").datetime.now(
                     __import__("datetime").timezone.utc).isoformat()}
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"], completed=[prior])
        ok(not C.check_daily_invest_cap(_trade(qty=10, limit_price=190.0)).passed,
           "$4k prior + $1.9k would exceed $5k/day budget — should fail")
        ok(C.check_daily_invest_cap(_trade(qty=5, limit_price=190.0)).passed,
           "$4k prior + $950 stays under $5k/day — should pass")

        # 7. Order type / TIF.
        ok(not C.check_order_type(_trade(order_type="MARKET")).passed, "MARKET should fail")
        ok(not C.check_order_type(_trade(time_in_force="GTC")).passed, "GTC should fail")
        ok(C.check_order_type(_trade()).passed, "LIMIT+DAY should pass")

        # 8. Forbidden / malformed instruments.
        ok(not C.check_forbidden_instrument(_trade(ticker="TQQQ")).passed, "TQQQ should fail")
        ok(not C.check_forbidden_instrument(_trade(ticker="SQQQ")).passed, "SQQQ should fail")
        ok(C.check_forbidden_instrument(_trade(ticker="AAPL")).passed, "AAPL should pass")

        # 9. Reason required.
        ok(not C.check_trade_reason(_trade(reason="x")).passed, "tiny reason should fail")
        ok(not C.check_trade_reason({"side": "BUY"}).passed, "no reason should fail")

        # 10. Thesis required for BUY, exempt for SELL.
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"])
        ok(not C.check_thesis_cited(_trade(ticker="ZZZZ", thesis_id="z")).passed,
           "BUY without a thesis file should fail")
        ok(not C.check_thesis_cited(_trade(thesis_id="")).passed, "BUY without thesis_id should fail")
        ok(C.check_thesis_cited(_trade()).passed, "BUY with a real thesis should pass")
        ok(C.check_thesis_cited(_trade(side="SELL", ticker="ZZZZ", thesis_id="")).passed,
           "SELL is exempt from thesis requirement")

        # 11. SELL is exempt from buy-only caps.
        sell = _trade(side="SELL", qty=1000, limit_price=200.0)  # $200k sell
        ok(C.check_per_trade_cap(sell).passed, "SELL exempt from per_trade_cap")
        ok(C.check_daily_invest_cap(sell).passed, "SELL exempt from daily budget")
        ok(C.check_cash_available(sell, broke).passed, "SELL exempt from cash check")
        ok(C.check_position_size(sell, PORTFOLIO_1M).passed, "SELL exempt from position size")

        # 12. Halt switch blocks everything.
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"], halt=True)
        ok(not C.check_halt_switch().passed, ".HALT_TRADING should fail halt_switch")
        p = _write_trade(tmp, _trade())
        passed, _ = C.run_all_checks(p)
        ok(not passed, "any trade should fail while halted")

        # 13. No same-day round trip.
        sell_today = {"trade_id": "T-sold", "ticker": "AAPL", "side": "SELL", "qty": 5,
                      "limit_price": 190.0,
                      "submitted_at_utc": __import__("datetime").datetime.now(
                          __import__("datetime").timezone.utc).isoformat()}
        _sandbox(tmp, portfolio=PORTFOLIO_1M, theses=["AAPL"], completed=[sell_today])
        ok(not C.check_no_day_trade(_trade()).passed,
           "buying AAPL after selling it today should fail no_day_trade")

    print(f"\ntest_constitution: {PASSED} passed, {FAILED} failed")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(run())
