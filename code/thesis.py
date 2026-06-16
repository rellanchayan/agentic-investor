"""
thesis.py — the keeper of research theses.

A "thesis" is our written, cited reason for owning (or wanting to own) a company.
One file per ticker: state/theses/<TICKER>.json. It holds the business story, the
moat, the key numbers (with sources), a fair-value band, a conviction score, and —
crucially — an explicit list of "what would break this thesis" (our sell triggers).

This module does three jobs:
  1. VALIDATE a thesis (`--check`): every numeric fact must carry a citation, the
     required fields must be present, conviction must be 1–5, and there must be at
     least one sell trigger. A thesis that fails is not allowed to justify a BUY.
  2. Report STALENESS (`--stale`): which theses are past their refresh date and need
     a fresh look (used by the morning and weekly routines).
  3. Provide small helpers other code reads (load_thesis, is_stale, thesis_summary).

CLI:
    python3 code/thesis.py --check AAPL
    python3 code/thesis.py --check state/theses/AAPL.json
    python3 code/thesis.py --check-all
    python3 code/thesis.py --stale
    python3 code/thesis.py --summary AAPL
    python3 code/thesis.py --template MSFT > state/theses/MSFT.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clockutil import et_today_str  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
THESES_DIR = ROOT / "state" / "theses"

REQUIRED_TOP = [
    "ticker", "thesis_id", "company", "sector", "as_of", "retrieved", "refresh_due",
    "business_summary", "moat", "quality", "valuation", "conviction",
    "bull_case", "risks", "what_would_break_thesis", "catalysts", "sources", "data_quality",
]
MOAT_RATINGS = {"none", "narrow", "wide"}
DATA_QUALITY_FLAGS = {"filing-backed", "aggregator-only", "incomplete"}


def _path_for(arg: str) -> Path:
    """Accept either a ticker (AAPL) or a path to a thesis JSON."""
    p = Path(arg)
    if p.suffix == ".json" and p.exists():
        return p
    return THESES_DIR / f"{arg.upper()}.json"


def load_thesis(ticker: str) -> dict | None:
    p = THESES_DIR / f"{ticker.upper()}.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def _is_number(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _numeric_facts(thesis: dict) -> list[str]:
    """Names of numeric facts the thesis asserts (these MUST be backed by sources)."""
    facts = []
    for k, v in (thesis.get("quality") or {}).items():
        if _is_number(v):
            facts.append(f"quality.{k}")
    return facts


def validate(thesis: dict) -> tuple[bool, list[str], list[str]]:
    """Return (ok, errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    for k in REQUIRED_TOP:
        if k not in thesis:
            errors.append(f"missing required field: {k}")
    if errors:
        return False, errors, warnings  # can't validate deeper without the fields

    # conviction 1..5
    conv = thesis.get("conviction")
    if not (isinstance(conv, int) and 1 <= conv <= 5):
        errors.append(f"conviction must be an integer 1–5, got {conv!r}")

    # moat
    moat = thesis.get("moat") or {}
    if str(moat.get("rating", "")).lower() not in MOAT_RATINGS:
        errors.append(f"moat.rating must be one of {sorted(MOAT_RATINGS)}, got {moat.get('rating')!r}")

    # sell triggers must exist
    if not (isinstance(thesis.get("what_would_break_thesis"), list) and thesis["what_would_break_thesis"]):
        errors.append("what_would_break_thesis must be a non-empty list (we need sell triggers)")

    # valuation band sanity
    val = thesis.get("valuation") or {}
    fv = {k: val.get(k) for k in ("fair_value_low", "fair_value_base", "fair_value_high")}
    if all(_is_number(fv[k]) for k in fv):
        if not (fv["fair_value_low"] <= fv["fair_value_base"] <= fv["fair_value_high"]):
            errors.append("valuation fair_value_low <= base <= high is violated")
    else:
        warnings.append("valuation band is incomplete (some fair_value_* are not numbers)")
    if not val.get("price_source"):
        warnings.append("valuation.price_source missing (price should come from Alpaca)")

    # data_quality flags
    dq = thesis.get("data_quality") or []
    if not isinstance(dq, list) or not dq or any(f not in DATA_QUALITY_FLAGS for f in dq):
        errors.append(f"data_quality must be a non-empty list from {sorted(DATA_QUALITY_FLAGS)}")

    # CITATIONS: every numeric fact must be backed by at least one source.
    sources = thesis.get("sources") or []
    facts = _numeric_facts(thesis)
    if facts and not sources:
        errors.append(f"thesis asserts numbers {facts} but has NO sources — uncited numbers are not allowed")
    for i, s in enumerate(sources):
        for field in ("claim", "url", "publisher", "as_of", "retrieved"):
            if not s.get(field):
                errors.append(f"sources[{i}] missing '{field}'")
        if s.get("url") and not str(s["url"]).startswith("http"):
            errors.append(f"sources[{i}].url does not look like a URL: {s['url']!r}")

    # soft check: a filing-backed claim should actually cite a filing
    if "filing-backed" in dq and not any(
        "sec.gov" in str(s.get("url", "")).lower() or "edgar" in str(s.get("publisher", "")).lower()
        or "investor" in str(s.get("url", "")).lower()
        for s in sources
    ):
        warnings.append("data_quality says 'filing-backed' but no source looks like an SEC filing / IR page")

    # refresh_due parseable
    try:
        date.fromisoformat(str(thesis.get("refresh_due")))
    except Exception:
        errors.append(f"refresh_due must be YYYY-MM-DD, got {thesis.get('refresh_due')!r}")

    return (not errors), errors, warnings


def is_stale(thesis: dict, today_str: str | None = None) -> bool:
    today_str = today_str or et_today_str()
    try:
        return date.fromisoformat(str(thesis["refresh_due"])) < date.fromisoformat(today_str)
    except Exception:
        return True  # unparseable / missing → treat as stale so it gets refreshed


def thesis_summary(thesis: dict, current_price: float | None = None) -> dict:
    val = thesis.get("valuation") or {}
    base = val.get("fair_value_base")
    price = current_price if current_price is not None else val.get("price")
    mos = None
    if _is_number(base) and _is_number(price) and base:
        mos = round((base - price) / base, 4)
    return {
        "ticker": thesis.get("ticker"),
        "conviction": thesis.get("conviction"),
        "fair_value": {k: val.get(k) for k in ("fair_value_low", "fair_value_base", "fair_value_high")},
        "price_used": price,
        "margin_of_safety": mos,
        "data_quality": thesis.get("data_quality"),
        "stale": is_stale(thesis),
        "refresh_due": thesis.get("refresh_due"),
        "moat": (thesis.get("moat") or {}).get("rating"),
    }


def _template(ticker: str) -> dict:
    t = ticker.upper()
    return {
        "ticker": t,
        "thesis_id": f"{t}-YYYYQn",
        "company": "",
        "sector": "",
        "as_of": "YYYY-Qn",
        "retrieved": et_today_str(),
        "refresh_due": "YYYY-MM-DD",
        "business_summary": "Plain-English: what does this company sell and how does it make money?",
        "moat": {"type": "", "rating": "narrow"},
        "quality": {
            "revenue_growth_3y": "unknown", "gross_margin": "unknown", "roic": "unknown",
            "net_debt_to_ebitda": "unknown", "fcf_positive": "unknown",
        },
        "valuation": {
            "price": "unknown", "price_source": "alpaca", "price_asof": et_today_str(),
            "fair_value_low": "unknown", "fair_value_base": "unknown", "fair_value_high": "unknown",
            "method": "pe + fcf_yield",
        },
        "conviction": 3,
        "bull_case": [],
        "risks": [],
        "what_would_break_thesis": [],
        "catalysts": [],
        "sources": [
            {"claim": "", "value": "", "url": "https://", "publisher": "", "as_of": "", "retrieved": et_today_str()},
        ],
        "data_quality": ["incomplete"],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--check", metavar="TICKER_OR_PATH")
    p.add_argument("--check-all", action="store_true")
    p.add_argument("--stale", action="store_true")
    p.add_argument("--summary", metavar="TICKER")
    p.add_argument("--template", metavar="TICKER")
    args = p.parse_args()

    if args.template:
        print(json.dumps(_template(args.template), indent=2))
        return 0

    if args.summary:
        th = load_thesis(args.summary)
        if not th:
            print(f"no thesis for {args.summary}", file=sys.stderr)
            return 1
        print(json.dumps(thesis_summary(th), indent=2))
        return 0

    if args.check:
        path = _path_for(args.check)
        if not path.exists():
            print(f"FAIL: no thesis file at {path}", file=sys.stderr)
            return 1
        thesis = json.loads(path.read_text())
        ok, errs, warns = validate(thesis)
        print(f"Thesis check: {'PASS' if ok else 'FAIL'} — {path.name}")
        for w in warns:
            print(f"  [WARN] {w}")
        for e in errs:
            print(f"  [FAIL] {e}")
        return 0 if ok else 1

    if args.check_all:
        any_fail = False
        files = sorted(THESES_DIR.glob("*.json"))
        if not files:
            print("no theses yet")
            return 0
        for f in files:
            thesis = json.loads(f.read_text())
            ok, errs, _ = validate(thesis)
            print(f"  {'PASS' if ok else 'FAIL'} {f.name}" + ("" if ok else f" — {errs[0]}"))
            any_fail = any_fail or not ok
        return 1 if any_fail else 0

    if args.stale:
        out = {"stale": [], "fresh": [], "invalid": []}
        today = et_today_str()
        for f in sorted(THESES_DIR.glob("*.json")):
            try:
                th = json.loads(f.read_text())
            except Exception:
                out["invalid"].append(f.stem)
                continue
            ok, _, _ = validate(th)
            if not ok:
                out["invalid"].append(th.get("ticker", f.stem))
            elif is_stale(th, today):
                out["stale"].append(th.get("ticker", f.stem))
            else:
                out["fresh"].append(th.get("ticker", f.stem))
        print(json.dumps(out, indent=2))
        return 0

    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
