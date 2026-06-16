"""test_thesis.py — offline tests for thesis validation + staleness. No network."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import thesis as T  # noqa: E402

PASSED = FAILED = 0


def ok(cond, label):
    global PASSED, FAILED
    if cond:
        PASSED += 1
    else:
        FAILED += 1
        print(f"  FAIL: {label}")


def valid_thesis():
    return {
        "ticker": "AAPL", "thesis_id": "AAPL-2026Q2", "company": "Apple Inc.",
        "sector": "technology", "as_of": "2026-Q2", "retrieved": "2026-06-14",
        "refresh_due": "2099-01-01",
        "business_summary": "Sells phones, computers, and high-margin services.",
        "moat": {"type": "ecosystem + brand", "rating": "wide"},
        "quality": {"revenue_growth_3y": 0.06, "gross_margin": 0.46, "roic": 0.45,
                    "net_debt_to_ebitda": 0.4, "fcf_positive": True},
        "valuation": {"price": 190.0, "price_source": "alpaca", "price_asof": "2026-06-14",
                      "fair_value_low": 175, "fair_value_base": 205, "fair_value_high": 235,
                      "method": "pe+fcf"},
        "conviction": 4,
        "bull_case": ["services growth"], "risks": ["china demand"],
        "what_would_break_thesis": ["gross margin < 40% sustained"],
        "catalysts": ["Q3 earnings"],
        "sources": [{"claim": "FY25 gross margin 46.2%", "value": 0.462,
                     "url": "https://www.sec.gov/cgi-bin/browse-edgar", "publisher": "SEC EDGAR",
                     "as_of": "FY2025", "retrieved": "2026-06-14"}],
        "data_quality": ["filing-backed"],
    }


def run():
    # 1. valid passes
    ok(T.validate(valid_thesis())[0], "valid thesis should pass")

    # 2. missing field fails
    t = valid_thesis(); del t["valuation"]
    ok(not T.validate(t)[0], "missing valuation should fail")

    # 3. numbers but no sources fails (uncited numbers)
    t = valid_thesis(); t["sources"] = []
    ok(not T.validate(t)[0], "numeric facts with no sources should fail")

    # 4. conviction out of range fails
    t = valid_thesis(); t["conviction"] = 7
    ok(not T.validate(t)[0], "conviction 7 should fail")
    t = valid_thesis(); t["conviction"] = 0
    ok(not T.validate(t)[0], "conviction 0 should fail")

    # 5. no sell triggers fails
    t = valid_thesis(); t["what_would_break_thesis"] = []
    ok(not T.validate(t)[0], "no sell triggers should fail")

    # 6. bad moat rating fails
    t = valid_thesis(); t["moat"] = {"type": "x", "rating": "huge"}
    ok(not T.validate(t)[0], "bad moat rating should fail")

    # 7. fair value band order enforced
    t = valid_thesis(); t["valuation"]["fair_value_low"] = 300
    ok(not T.validate(t)[0], "low>base should fail band order")

    # 8. source missing url fails
    t = valid_thesis(); t["sources"][0].pop("url")
    ok(not T.validate(t)[0], "source missing url should fail")

    # 9. bad data_quality flag fails
    t = valid_thesis(); t["data_quality"] = ["made-up"]
    ok(not T.validate(t)[0], "invalid data_quality flag should fail")

    # 10. staleness
    fresh = valid_thesis()  # refresh_due 2099
    ok(not T.is_stale(fresh, "2026-06-16"), "future refresh_due is not stale")
    old = valid_thesis(); old["refresh_due"] = "2020-01-01"
    ok(T.is_stale(old, "2026-06-16"), "past refresh_due is stale")
    bad = valid_thesis(); bad["refresh_due"] = "garbage"
    ok(T.is_stale(bad, "2026-06-16"), "unparseable refresh_due treated as stale")

    # 11. summary computes margin of safety
    s = T.thesis_summary(valid_thesis())
    ok(s["margin_of_safety"] is not None and s["margin_of_safety"] > 0,
       f"summary MoS positive when price below base {s['margin_of_safety']}")

    print(f"\ntest_thesis: {PASSED} passed, {FAILED} failed")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(run())
