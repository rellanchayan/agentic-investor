"""test_valuation.py — offline tests for the fair-value arithmetic. No network."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import valuation as V  # noqa: E402

PASSED = FAILED = 0


def ok(cond, label):
    global PASSED, FAILED
    if cond:
        PASSED += 1
    else:
        FAILED += 1
        print(f"  FAIL: {label}")


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol


def run():
    # PE band
    b = V.pe_fair_value(10.0, [10, 15, 20])
    ok(b == {"low": 100.0, "base": 150.0, "high": 200.0}, f"pe band {b}")

    # Yield band: lower yield => higher price; band sorts itself.
    b = V.yield_fair_value(5.0, [0.05, 0.04, 0.025])  # prices 100, 125, 200
    ok(approx(b["low"], 100) and approx(b["base"], 125) and approx(b["high"], 200), f"yield band {b}")

    # Margin of safety
    ok(approx(V.margin_of_safety(80, 100), 0.20), "MoS 80 vs 100 = 0.20")
    ok(V.margin_of_safety(120, 100) < 0, "MoS negative when overpriced")
    ok(V.margin_of_safety(100, 0) == 0.0, "MoS guards divide-by-zero")

    # DCF-lite is positive and finite; terminal guard when discount<=terminal_growth.
    v = V.dcf_lite(5.0, 0.08, 10, 0.10, 0.025)
    ok(v > 0 and v < 1e6, f"dcf_lite finite positive {v}")
    v2 = V.dcf_lite(5.0, 0.08, 10, 0.02, 0.025)  # discount <= terminal_growth
    ok(v2 > 0 and v2 < 1e9, f"dcf_lite terminal guard {v2}")

    # evaluate end-to-end
    out = V.evaluate({"price": 90, "methods": {"pe": {"eps": 10, "multiples": [10, 12, 14]}}})
    ok(out["fair_value"]["base"] == 120.0, f"evaluate base {out['fair_value']}")
    ok(out["margin_of_safety"] > 0, "evaluate MoS positive when cheap")
    ok(out["verdict"].startswith("cheap"), f"evaluate verdict {out['verdict']}")

    # no methods → error
    ok("error" in V.evaluate({"price": 100, "methods": {}}), "no methods returns error")

    print(f"\ntest_valuation: {PASSED} passed, {FAILED} failed")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(run())
