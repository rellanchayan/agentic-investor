"""
budget.py — how much of today's strict buy budget is left.

The constitution sets a hard $5,000/day cap on NEW buys (selling is never capped).
This tells the portfolio-manager how many dollars it may still deploy today, so it
can size today's tranche. It reads the same source of truth the constitution uses:
the BUY orders already submitted today.

CLI:
    python3 code/budget.py --remaining
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from constitution import MAX_DAILY_INVEST_USD, _todays_completed  # noqa: E402


def used_today() -> float:
    """Total dollars of BUY orders already submitted today."""
    return sum(
        float(d.get("limit_price", 0)) * float(d.get("qty", 0))
        for d in _todays_completed()
        if str(d.get("side", "")).upper() == "BUY"
    )


def remaining() -> dict:
    used = used_today()
    return {
        "daily_budget_usd": MAX_DAILY_INVEST_USD,
        "used_today_usd": round(used, 2),
        "remaining_usd": round(max(0.0, MAX_DAILY_INVEST_USD - used), 2),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--remaining", action="store_true")
    args = p.parse_args()
    if args.remaining or True:  # default action
        print(json.dumps(remaining(), indent=2))
        return 0


if __name__ == "__main__":
    sys.exit(main())
