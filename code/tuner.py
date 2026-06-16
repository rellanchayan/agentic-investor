"""
tuner.py — the small, careful, reversible learning dial.

Most of how this bot "learns" is written in plain English (thesis post-mortems and
the PLAYBOOK). This file is the OPTIONAL numeric part: after enough history, it may
nudge ONE soft setting, by ONE small step, staying inside hard bounds, and it writes
down exactly what it changed so any change can be undone.

It will NOT tune while we're losing — "don't optimize while you're bleeding." And it
can NEVER touch the hard limits in constitution.py (they are not in param_bounds.json).

CLI:
    python3 code/tuner.py --status        # show whether tuning is allowed + what it would do
    python3 code/tuner.py --run           # apply at most one change (if gate is open + a rule fires)
    python3 code/tuner.py --revert <id>   # undo a specific change
    python3 code/tuner.py --reset         # restore config.json to config.defaults.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clockutil import et_today_str  # noqa: E402
import metrics as M  # noqa: E402
import calibration as CAL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "state" / "config.json"
DEFAULTS = ROOT / "state" / "config.defaults.json"
BOUNDS = ROOT / "state" / "param_bounds.json"
LEDGER = ROOT / "state" / "tuning_ledger.jsonl"

MIN_DAYS_HISTORY = 20        # need a real track record before tuning anything
FREEZE_DRAWDOWN = -0.10      # if deeper in drawdown than this, freeze (don't optimize while bleeding)
LOSING_STREAK_DAYS = 5       # if the last N days are net negative, freeze
COOLDOWN_DAYS = 2            # don't change the same parameter two runs in a row


def _load(path: Path) -> dict:
    return json.loads(path.read_text())


def _clamp_to_step(value, bound) -> float | int:
    v = max(bound["min"], min(bound["max"], value))
    if isinstance(bound["step"], int) and float(bound["step"]).is_integer():
        return int(round(v))
    return round(v, 6)


def _recent_changes() -> list[dict]:
    out = []
    if LEDGER.exists():
        for line in LEDGER.read_text().splitlines():
            try:
                out.append(json.loads(line))
            except Exception:
                continue
    return out


def _param_on_cooldown(param: str, today: str) -> bool:
    from datetime import date
    for row in _recent_changes():
        if row.get("param") == param:
            try:
                d = date.fromisoformat(row["date"])
                if (date.fromisoformat(today) - d).days < COOLDOWN_DAYS:
                    return True
            except Exception:
                continue
    return False


def gating() -> dict:
    """Decide whether tuning is allowed right now. Returns {allowed, reasons}."""
    reasons = []
    series = M.load_equity_series()
    if len(series) < MIN_DAYS_HISTORY:
        reasons.append(f"only {len(series)} days of history (<{MIN_DAYS_HISTORY}) — too early to tune")
    values = [s["equity"] for s in series]
    if values:
        dd = M.max_drawdown(values)
        if dd < FREEZE_DRAWDOWN:
            reasons.append(f"in a {dd:.0%} drawdown (deeper than {FREEZE_DRAWDOWN:.0%}) — frozen")
        if len(values) > LOSING_STREAK_DAYS:
            recent = values[-(LOSING_STREAK_DAYS + 1):]
            if recent[-1] < recent[0]:
                reasons.append(f"last {LOSING_STREAK_DAYS} days net-negative — frozen (don't optimize while bleeding)")
    return {"allowed": not reasons, "reasons": reasons}


def propose() -> dict | None:
    """Return a single proposed change, or None. Conservative, evidence-based."""
    cfg = _load(CONFIG)
    bounds = _load(BOUNDS)
    today = et_today_str()

    # Rule 1: poor fill rate → be slightly more marketable on buys.
    rate, fd = M.fill_rate()
    if rate is not None and fd["final_orders"] >= 10 and rate < 0.70:
        param = "limit_buy_above_bid_pct"
        if not _param_on_cooldown(param, today):
            new = _clamp_to_step(cfg[param] + bounds[param]["step"], bounds[param])
            if new != cfg[param]:
                return {"param": param, "from": cfg[param], "to": new,
                        "reason": "LIMIT fill rate is low — pay a touch more to actually get filled",
                        "evidence": {"fill_rate": round(rate, 3), "final_orders": fd["final_orders"]}}

    # Rule 2: elevated drawdown OR miscalibrated conviction → demand a bigger margin of safety.
    series = M.load_equity_series()
    values = [s["equity"] for s in series]
    dd = M.max_drawdown(values) if values else 0.0
    cal = CAL.report()
    by = cal.get("by_conviction", {})
    miscalibrated = False
    if "5" in by and "3" in by and by["5"]["n"] >= 3 and by["3"]["n"] >= 3:
        miscalibrated = by["5"]["avg_mtm_return"] <= by["3"]["avg_mtm_return"]
    if (FREEZE_DRAWDOWN <= dd < -0.05) or miscalibrated:
        param = "min_margin_of_safety"
        if not _param_on_cooldown(param, today):
            new = _clamp_to_step(cfg[param] + bounds[param]["step"], bounds[param])
            if new != cfg[param]:
                return {"param": param, "from": cfg[param], "to": new,
                        "reason": ("high-conviction buys aren't outperforming — demand cheaper entries"
                                   if miscalibrated else "drawdown is building — demand more cushion before buying"),
                        "evidence": {"drawdown": round(dd, 4), "miscalibrated_conviction": miscalibrated}}

    return None


def apply_change(change: dict) -> dict:
    cfg = _load(CONFIG)
    cfg[change["param"]] = change["to"]
    CONFIG.write_text(json.dumps(cfg, indent=2))
    row = {
        "id": f"TUNE-{et_today_str().replace('-', '')}-{change['param']}",
        "date": et_today_str(),
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "param": change["param"], "from": change["from"], "to": change["to"],
        "reason": change["reason"], "evidence": change["evidence"], "reverted": False,
    }
    with LEDGER.open("a") as f:
        f.write(json.dumps(row) + "\n")
    return row


def revert(change_id: str) -> dict:
    if not LEDGER.exists():
        return {"error": "no tuning ledger"}
    rows = [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()]
    target = next((r for r in rows if r["id"] == change_id and not r.get("reverted")), None)
    if not target:
        return {"error": f"no active change with id {change_id}"}
    cfg = _load(CONFIG)
    cfg[target["param"]] = target["from"]
    CONFIG.write_text(json.dumps(cfg, indent=2))
    target["reverted"] = True
    LEDGER.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    return {"reverted": change_id, "param": target["param"], "restored_to": target["from"]}


def reset() -> dict:
    defaults = _load(DEFAULTS)
    defaults.pop("_comment", None)
    cfg = _load(CONFIG)
    cfg.update(defaults)
    CONFIG.write_text(json.dumps(cfg, indent=2))
    return {"reset": True, "restored": list(defaults.keys())}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--status", action="store_true")
    p.add_argument("--run", action="store_true")
    p.add_argument("--revert", metavar="ID")
    p.add_argument("--reset", action="store_true")
    args = p.parse_args()

    if args.reset:
        print(json.dumps(reset(), indent=2)); return 0
    if args.revert:
        print(json.dumps(revert(args.revert), indent=2)); return 0

    gate = gating()
    if args.status:
        prop = propose() if gate["allowed"] else None
        print(json.dumps({"gating": gate, "would_change": prop}, indent=2))
        return 0
    if args.run:
        if not gate["allowed"]:
            print(json.dumps({"action": "none", "gating": gate})); return 0
        prop = propose()
        if not prop:
            print(json.dumps({"action": "none", "reason": "no rule fired — current settings look fine"})); return 0
        print(json.dumps({"action": "changed", "change": apply_change(prop)}, indent=2))
        return 0

    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
