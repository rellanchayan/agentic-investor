"""
calibration.py — are our high-conviction buys actually the ones that work?

Every time we buy, we write down how sure we were (conviction 1–5) and how cheap it
looked (margin of safety). Later we look back: did the conviction-5 buys really do
better than the conviction-3 buys? If not, our confidence is miscalibrated and the
learning-coach should make us demand a bigger margin of safety before buying.

This is awareness, not auto-trading. It never places an order.

How it measures return:
  * For names we STILL hold: mark-to-market using the current price from portfolio.json.
  * For names we've SOLD: the realized result lives in the journal / metrics round-trips;
    this tool marks them "exited" so we don't double-count.

CLI:
    python3 code/calibration.py --record    # log any new filled buys (run at end of day)
    python3 code/calibration.py --report    # show conviction buckets vs return
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPLETED_DIR = ROOT / "state" / "completed_trades"
PORTFOLIO_FILE = ROOT / "state" / "portfolio.json"
LEDGER = ROOT / "state" / "calibration.jsonl"


def _existing_ids() -> set[str]:
    ids = set()
    if LEDGER.exists():
        for line in LEDGER.read_text().splitlines():
            try:
                ids.add(json.loads(line)["trade_id"])
            except Exception:
                continue
    return ids


def record() -> dict:
    """Append a calibration row for each newly-filled BUY not already logged."""
    seen = _existing_ids()
    added = []
    if COMPLETED_DIR.exists():
        for path in sorted(COMPLETED_DIR.glob("*.json")):
            try:
                t = json.loads(path.read_text())
            except Exception:
                continue
            if str(t.get("side", "")).upper() != "BUY":
                continue
            if str(t.get("status", "")).lower() not in ("filled", "partially_filled"):
                continue
            if float(t.get("filled_qty") or 0) <= 0:
                continue
            tid = t.get("trade_id")
            if not tid or tid in seen:
                continue
            row = {
                "trade_id": tid,
                "ticker": str(t.get("ticker", "")).upper(),
                "buy_date": str(t.get("reconciled_at_utc") or t.get("submitted_at_utc", ""))[:10],
                "conviction": t.get("conviction"),
                "margin_of_safety": t.get("margin_of_safety"),
                "buy_price": float(t.get("filled_avg_price") or t.get("limit_price") or 0),
                "qty": float(t.get("filled_qty") or 0),
            }
            with LEDGER.open("a") as f:
                f.write(json.dumps(row) + "\n")
            seen.add(tid)
            added.append(tid)
    return {"recorded": added, "count": len(added)}


def _current_prices() -> dict:
    try:
        p = json.loads(PORTFOLIO_FILE.read_text())
        return {pos["ticker"].upper(): float(pos.get("current_price") or 0) for pos in p.get("positions", [])}
    except Exception:
        return {}


def report() -> dict:
    if not LEDGER.exists():
        return {"note": "no calibration history yet — buys get recorded at end of day"}
    prices = _current_prices()
    buckets: dict[int, list[float]] = {}
    open_rows, exited = 0, 0
    detail = []
    for line in LEDGER.read_text().splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        tkr = r["ticker"]
        conv = r.get("conviction")
        cur = prices.get(tkr, 0)
        if cur > 0 and r.get("buy_price"):
            ret = cur / r["buy_price"] - 1
            open_rows += 1
            if isinstance(conv, int):
                buckets.setdefault(conv, []).append(ret)
            detail.append({"ticker": tkr, "conviction": conv, "mtm_return": round(ret, 4), "status": "open"})
        else:
            exited += 1
            detail.append({"ticker": tkr, "conviction": conv, "status": "exited (see journal for realized result)"})
    by_conviction = {
        str(c): {"avg_mtm_return": round(sum(v) / len(v), 4), "n": len(v)}
        for c, v in sorted(buckets.items())
    }
    return {
        "open_positions_measured": open_rows,
        "exited_positions": exited,
        "by_conviction": by_conviction,
        "detail": detail,
        "note": "Open positions are marked to market. Higher conviction should, over time, show higher average return.",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--record", action="store_true")
    p.add_argument("--report", action="store_true")
    args = p.parse_args()
    if args.record:
        print(json.dumps(record(), indent=2))
        return 0
    if args.report:
        print(json.dumps(report(), indent=2))
        return 0
    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
