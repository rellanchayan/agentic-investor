"""
valuation.py — transparent, arithmetic-only fair-value estimates.

Why this exists: a language model should NOT do the arithmetic that decides what a
business is worth — it can slip. So the research-analyst gathers the *cited* inputs
(earnings per share, free cash flow per share, dividend, sensible multiples) and this
module does the actual math. Every number it prints can be traced back to an input.

It estimates a fair-value BAND (low / base / high), never a single magic number, and
a "margin of safety" = how far today's price sits below the base fair value. A bigger
margin of safety means more cushion if we are wrong.

Methods (use whichever the inputs support):
  * PE (price-to-earnings): fair price = earnings-per-share x a sensible multiple.
  * FCF yield: fair price = free-cash-flow-per-share / a target yield.
  * Dividend yield: fair price = dividend-per-share / a target yield.
  * DCF-lite: a simple discounted-cash-flow point estimate (explicit assumptions).

CLI:
    python3 code/valuation.py --from inputs.json
    echo '{...}' | python3 code/valuation.py --stdin

Input JSON shape (all fields optional except price + at least one method):
{
  "ticker": "AAPL",
  "price": 190.0,
  "methods": {
    "pe":             {"eps": 6.5,  "multiples": [22, 27, 32]},
    "fcf_yield":      {"fcf_per_share": 6.8, "yields": [0.050, 0.042, 0.035]},
    "dividend_yield": {"dps": 1.0,  "yields": [0.0070, 0.0060, 0.0050]},
    "dcf_lite":       {"fcf_per_share": 6.8, "growth": 0.08, "years": 10,
                       "discount": 0.10, "terminal_growth": 0.025}
  }
}
"""

from __future__ import annotations

import argparse
import json
import sys


def _band(values: list[float]) -> dict:
    """Turn up to three numbers into a sorted low/base/high band."""
    vals = sorted(float(v) for v in values)
    if len(vals) == 1:
        return {"low": vals[0], "base": vals[0], "high": vals[0]}
    if len(vals) == 2:
        return {"low": vals[0], "base": (vals[0] + vals[1]) / 2, "high": vals[1]}
    return {"low": vals[0], "base": vals[1], "high": vals[-1]}


def pe_fair_value(eps: float, multiples: list[float]) -> dict:
    """fair price = eps x multiple, for each multiple."""
    return _band([eps * m for m in multiples])


def yield_fair_value(per_share_cash: float, yields: list[float]) -> dict:
    """fair price = per-share cash / target yield. A lower target yield = a higher price,
    so we sort the resulting prices into the band automatically."""
    prices = [per_share_cash / y for y in yields if y and y > 0]
    return _band(prices) if prices else {"low": 0.0, "base": 0.0, "high": 0.0}


def dcf_lite(fcf_per_share: float, growth: float, years: int,
             discount: float, terminal_growth: float) -> float:
    """A simple two-stage discounted-cash-flow value per share.

    Stage 1: grow free cash flow per share at `growth` for `years`, discount each year.
    Stage 2: a Gordon terminal value (perpetual growth at `terminal_growth`), discounted.
    Returns a single point estimate. Assumptions are explicit and printed.
    """
    if discount <= terminal_growth:
        # Guard against a divide-by-(<=0) terminal — return just the discounted stage 1.
        terminal = 0.0
    pv = 0.0
    cf = fcf_per_share
    for t in range(1, years + 1):
        cf = cf * (1 + growth)
        pv += cf / ((1 + discount) ** t)
    if discount > terminal_growth:
        terminal_cf = cf * (1 + terminal_growth)
        terminal = (terminal_cf / (discount - terminal_growth)) / ((1 + discount) ** years)
    return pv + terminal


def margin_of_safety(price: float, base_fair_value: float) -> float:
    """How far price sits below base fair value, as a fraction. Positive = undervalued."""
    if base_fair_value <= 0:
        return 0.0
    return (base_fair_value - price) / base_fair_value


def evaluate(inp: dict) -> dict:
    price = float(inp.get("price", 0) or 0)
    methods = inp.get("methods", {}) or {}
    per_method: dict[str, dict] = {}

    if "pe" in methods:
        m = methods["pe"]
        per_method["pe"] = pe_fair_value(float(m["eps"]), list(m["multiples"]))
    if "fcf_yield" in methods:
        m = methods["fcf_yield"]
        per_method["fcf_yield"] = yield_fair_value(float(m["fcf_per_share"]), list(m["yields"]))
    if "dividend_yield" in methods:
        m = methods["dividend_yield"]
        per_method["dividend_yield"] = yield_fair_value(float(m["dps"]), list(m["yields"]))
    if "dcf_lite" in methods:
        m = methods["dcf_lite"]
        pt = dcf_lite(float(m["fcf_per_share"]), float(m["growth"]), int(m["years"]),
                      float(m["discount"]), float(m["terminal_growth"]))
        per_method["dcf_lite"] = {"low": pt, "base": pt, "high": pt}

    if not per_method:
        return {"error": "no usable valuation methods provided", "price": price}

    # Aggregate: average each of low/base/high across the methods provided. Transparent
    # and stable; the per-method detail is returned too so the reasoning is auditable.
    n = len(per_method)
    low = sum(b["low"] for b in per_method.values()) / n
    base = sum(b["base"] for b in per_method.values()) / n
    high = sum(b["high"] for b in per_method.values()) / n
    fair = {"low": round(low, 2), "base": round(base, 2), "high": round(high, 2)}

    return {
        "ticker": inp.get("ticker"),
        "price": price,
        "methods_used": sorted(per_method.keys()),
        "per_method": {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in per_method.items()},
        "fair_value": fair,
        "margin_of_safety": round(margin_of_safety(price, base), 4),
        "verdict": _verdict(price, fair),
    }


def _verdict(price: float, fair: dict) -> str:
    if price <= 0 or fair["base"] <= 0:
        return "unknown"
    if price < fair["low"]:
        return "cheap (below the low end of fair value)"
    if price > fair["high"]:
        return "expensive (above the high end of fair value)"
    if price < fair["base"]:
        return "fair, leaning cheap"
    return "fair, leaning expensive"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--from", dest="path", help="path to a JSON file of valuation inputs")
    p.add_argument("--stdin", action="store_true", help="read inputs JSON from stdin")
    args = p.parse_args()

    if args.stdin:
        inp = json.load(sys.stdin)
    elif args.path:
        with open(args.path) as f:
            inp = json.load(f)
    else:
        p.print_help()
        return 1

    print(json.dumps(evaluate(inp), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
