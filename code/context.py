"""
context.py — build the one morning snapshot the portfolio-manager reads.

Instead of the manager making dozens of separate look-ups, this gathers everything
into a single file: state/day/<today>/context.json. It contains:
  * the account (equity, cash, drawdown),
  * each holding with its weight, profit, and a one-line thesis summary,
  * each watchlist name with its current price, fair-value band, and margin of safety,
  * how concentrated we are by sector,
  * how much of today's $5,000 buy budget is left,
  * a simple market-trend hint (is SPY above or below its 200-day average?).

Prices come ONLY from Alpaca (one batched request). If Alpaca is unreachable, prices
are left null and a note says so — we never invent a price.

CLI:
    python3 code/context.py            # build + print today's context
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clockutil import et_today_str  # noqa: E402
import thesis as T  # noqa: E402
import budget as B  # noqa: E402

try:
    from dotenv import load_dotenv
    ROOT = Path(__file__).resolve().parent.parent
    load_dotenv(ROOT / ".env", override=True)
except ImportError:
    ROOT = Path(__file__).resolve().parent.parent

PORTFOLIO_FILE = ROOT / "state" / "portfolio.json"
WATCHLIST_FILE = ROOT / "state" / "watchlist.txt"
SECTORS_FILE = ROOT / "state" / "sectors.json"


def _load_watchlist() -> list[str]:
    if not WATCHLIST_FILE.exists():
        return []
    out = []
    for line in WATCHLIST_FILE.read_text().splitlines():
        line = line.split("#")[0].strip().upper()
        if line and line not in out:
            out.append(line)
    return out


def _load_json(path: Path, default):
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def _latest_prices(tickers: list[str]) -> tuple[dict, str | None]:
    """Batched latest-quote fetch from Alpaca (IEX). Returns ({ticker: price}, note)."""
    if not tickers:
        return {}, None
    try:
        from alpaca.data.historical import StockHistoricalDataClient
        from alpaca.data.requests import StockLatestQuoteRequest
        from alpaca.data.enums import DataFeed
        import os
        dc = StockHistoricalDataClient(os.environ.get("ALPACA_API_KEY"), os.environ.get("ALPACA_SECRET_KEY"))
        req = StockLatestQuoteRequest(symbol_or_symbols=tickers, feed=DataFeed.IEX)
        res = dc.get_stock_latest_quote(req)
        prices = {}
        for t in tickers:
            q = res.get(t)
            if not q:
                continue
            bid, ask = float(q.bid_price or 0), float(q.ask_price or 0)
            if bid > 0 and ask > 0:
                prices[t] = round((bid + ask) / 2, 2)
            elif ask > 0:
                prices[t] = round(ask, 2)
            elif bid > 0:
                prices[t] = round(bid, 2)
        return prices, None
    except Exception as e:
        return {}, f"price fetch failed: {e}"


def _spy_trend() -> dict:
    """Is SPY above or below its 200-day average? A simple market-weather hint."""
    try:
        from datetime import timedelta
        from alpaca.data.historical import StockHistoricalDataClient
        from alpaca.data.requests import StockBarsRequest
        from alpaca.data.enums import DataFeed
        from alpaca.data.timeframe import TimeFrame
        import os
        dc = StockHistoricalDataClient(os.environ.get("ALPACA_API_KEY"), os.environ.get("ALPACA_SECRET_KEY"))
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=420)
        req = StockBarsRequest(symbol_or_symbols="SPY", timeframe=TimeFrame.Day, start=start, end=end, feed=DataFeed.IEX)
        bars = dc.get_stock_bars(req).data.get("SPY", [])
        closes = [float(b.close) for b in bars]
        if len(closes) < 200:
            return {"available": False, "note": f"only {len(closes)} daily bars (<200)"}
        sma200 = sum(closes[-200:]) / 200
        last = closes[-1]
        return {
            "available": True,
            "spy_last": round(last, 2),
            "spy_sma200": round(sma200, 2),
            "above_200d": last > sma200,
            "note": f"SPY {last:.2f} is {'ABOVE' if last > sma200 else 'BELOW'} its 200-day average {sma200:.2f}",
        }
    except Exception as e:
        return {"available": False, "note": f"trend fetch failed: {e}"}


def build() -> dict:
    portfolio = _load_json(PORTFOLIO_FILE, None)
    if portfolio is None:
        return {"error": "no state/portfolio.json — run `alpaca_client.py --positions` first"}

    equity = float(portfolio.get("equity", 0))
    cash = float(portfolio.get("cash", 0))
    positions = portfolio.get("positions", [])
    held = {p["ticker"].upper(): p for p in positions}
    watchlist = _load_watchlist()
    sectors = _load_json(SECTORS_FILE, {})

    universe = sorted(set(list(held.keys()) + watchlist + ["SPY"]))
    prices, price_note = _latest_prices(universe)

    # Holdings with weight, profit, and thesis summary.
    holdings = []
    for tkr, p in held.items():
        th = T.load_thesis(tkr)
        cur = prices.get(tkr) or p.get("current_price")
        holdings.append({
            "ticker": tkr,
            "qty": p.get("qty"),
            "avg_entry_price": p.get("avg_entry_price"),
            "current_price": cur,
            "market_value": p.get("market_value"),
            "weight": round(float(p.get("market_value", 0)) / equity, 4) if equity else None,
            "unrealized_pl": p.get("unrealized_pl"),
            "unrealized_plpc": p.get("unrealized_plpc"),
            "sector": sectors.get(tkr, "unknown"),
            "thesis": T.thesis_summary(th, cur) if th else {"note": "NO THESIS — research before adding/holding decision"},
        })

    # Watchlist names we do NOT already hold.
    candidates = []
    for tkr in watchlist:
        if tkr in held:
            continue
        th = T.load_thesis(tkr)
        cur = prices.get(tkr)
        candidates.append({
            "ticker": tkr,
            "current_price": cur,
            "sector": sectors.get(tkr, "unknown"),
            "thesis": T.thesis_summary(th, cur) if th else {"note": "NO THESIS — research before any buy"},
        })

    # Sector exposure (held only).
    sector_exposure: dict[str, float] = {}
    for h in holdings:
        s = h["sector"]
        sector_exposure[s] = round(sector_exposure.get(s, 0.0) + (h["weight"] or 0.0), 4)

    return {
        "date_et": et_today_str(),
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "account": {
            "equity": equity,
            "cash": cash,
            "drawdown_from_hwm": portfolio.get("drawdown_from_hwm", 0.0),
            "holding_slots_used": len(held),
            "holding_slots_max": 8,
        },
        "budget": B.remaining(),
        "market_trend": _spy_trend(),
        "holdings": holdings,
        "candidates": candidates,
        "sector_exposure": sector_exposure,
        "price_source": "alpaca-iex (midpoint of bid/ask)",
        "notes": [n for n in [price_note] if n],
    }


def main() -> int:
    ctx = build()
    if "error" in ctx:
        print(ctx["error"], file=sys.stderr)
        return 1
    day_dir = ROOT / "state" / "day" / ctx["date_et"]
    day_dir.mkdir(parents=True, exist_ok=True)
    (day_dir / "context.json").write_text(json.dumps(ctx, indent=2))
    print(json.dumps(ctx, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
