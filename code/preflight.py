"""
preflight.py — the cheap gate that runs FIRST every market morning.

It answers one question before any expensive thinking happens: "is it safe and
sensible to run the morning routine right now?" No language-model cost.

It prints a JSON verdict and sets an exit code:
    verdict = "PROCEED" (exit 0) → market open, not halted, Alpaca reachable
    verdict = "EXIT"    (exit 3) → do nothing (halted / closed / Alpaca down)

Unlike a day trader, we have no loss-stop here — we hold for the long run. If the
daily buy budget is already used up we still PROCEED (we can still hold, trim, or
sell); the verdict just notes the budget is exhausted.

Usage:
    python3 code/preflight.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import budget as B  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
HALT_FILE = ROOT / ".HALT_TRADING"


def _run_client(*flags: str) -> dict | None:
    try:
        out = subprocess.run(
            [sys.executable, "code/alpaca_client.py", *flags],
            cwd=ROOT, text=True, capture_output=True,
        )
        if out.returncode != 0:
            return None
        return json.loads(out.stdout)
    except Exception:
        return None


def verdict(name: str, reason: str, **extra) -> dict:
    return {"verdict": name, "reason": reason, **extra}


def run() -> tuple[dict, int]:
    # 1. Human kill-switch
    if HALT_FILE.exists():
        return verdict("EXIT", ".HALT_TRADING present — trading halted by a human"), 3

    # 2. Market actually open (Alpaca is the authority on holidays / half-days)
    clock = _run_client("--clock")
    if clock is None:
        return verdict("EXIT", "Alpaca unreachable — doing nothing this run (safe default)"), 3
    if not clock.get("is_open"):
        return verdict("EXIT", "market is closed today", next_open=clock.get("next_open")), 3

    # 3. Account reachable (gives equity + cash for sizing)
    acct = _run_client("--account")
    if acct is None:
        return verdict("EXIT", "could not read account — doing nothing this run (safe default)"), 3

    bud = B.remaining()
    return verdict(
        "PROCEED", "market open, not halted, Alpaca reachable",
        equity=acct.get("equity"), cash=acct.get("cash"),
        budget_remaining_usd=bud["remaining_usd"],
        budget_exhausted=bud["remaining_usd"] <= 0,
    ), 0


def main() -> int:
    v, code = run()
    print(json.dumps(v, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
