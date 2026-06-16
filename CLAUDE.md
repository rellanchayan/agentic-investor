# CLAUDE.md — Agentic Long-Term Investor

This project invests with **paper money only**, on Alpaca, acting like a patient,
long-term, "quality at a fair price" investor. It tries to beat SPY over years.

No system can guarantee profit. This repo's job is to make disciplined, well-researched
paper investments, record everything honestly, and improve with experience.

> Note: this file deliberately **overrides** the Desktop-level `CLAUDE.md` rule "no markdown
> logs." Here, detailed plain-English analysis docs are a core deliverable.

---

## 1. Trading Mode

- Paper trading only. Alpaca paper endpoint only (`paper-api.alpaca.markets`). No live trading.
- No options, futures, shorts, margin, or crypto.
- No market orders. **LIMIT + DAY** orders only.
- Long-term horizon: hold for months/years. No day trading (no same-day round trips).

---

## 2. What We Can Trade

- Stocks and normal ETFs of large, liquid, profitable, understandable businesses.
- Avoid junk: penny stocks, OTC names, leveraged/inverse/volatility ETFs.
- Plain tickers only (no dotted share classes like BRK.B — the code needs clean symbols).
- We measure ourselves against **SPY**.

---

## 3. Hard Limits (enforced in `code/constitution.py` — never tunable)

- **$5,000 of new buys per day** (the strict daily budget). Selling is never capped.
- **$5,000 maximum per single buy.**
- **≤ 25%** of the account in any one ticker.
- **≤ 8 holdings** at once.
- Spend only **settled cash** — no margin / leverage.
- **≤ 20 trades/day, ≤ 50 trades/week.**
- Every BUY must cite a **thesis** (`state/theses/<TICKER>.json`). No thesis = no buy.
- Every trade needs a real written **reason**. No reason = no trade.

The account starts at ~$1,000,000 of paper money, so $5,000/day is a deliberately slow,
disciplined pace (dollar-cost-averaging). Soft guidelines (margin of safety, target weight,
etc.) live in `state/config.json` and may be nudged by the tuner within `state/param_bounds.json`.

---

## 4. Trade File

The portfolio-manager writes one JSON per order to `state/pending_trades/`:

```json
{
  "trade_id": "T-20260616-AAPL-001",
  "ticker": "AAPL",
  "side": "BUY",
  "action": "ADD",
  "qty": 12,
  "limit_price": 192.40,
  "order_type": "LIMIT",
  "time_in_force": "DAY",
  "thesis_id": "AAPL-2026Q2",
  "conviction": 4,
  "fair_value": {"low": 175, "base": 205, "high": 235, "method": "pe+fcf"},
  "margin_of_safety": 0.0615,
  "target_weight": 0.10,
  "reason": "Short reason for the trade.",
  "risk": "The main risk / the thesis-break trigger.",
  "status": "ready"
}
```

`--submit` stamps the order id and moves the file to `state/completed_trades/`. `--reconcile`
later records the real fill (`filled_qty`, `filled_avg_price`). We never assume a fill.

---

## 5. Daily / Weekly Cycle

- **Morning** (weekdays, after the 9:30 ET open) — `/morning`: gate → reconcile → snapshot →
  market weather → refresh stale theses → decide (buy/trim/sell/hold) → risk-check → submit →
  write `docs/decisions/<date>.md`.
- **End of day** (weekdays after the 4:00 ET close) — `/end-of-day`: reconcile real fills →
  day summary → honest journal + trade cards + sell post-mortems → learn one small thing.
- **Weekly** (Saturday, market closed) — `/weekly-research`: refresh theses on rotation, scout
  new quality names, fold calibration findings into the playbook.

---

## 6. Commands

```bash
python3 code/alpaca_client.py --healthcheck
python3 code/alpaca_client.py --positions
python3 code/alpaca_client.py --quote AAPL
python3 code/alpaca_client.py --bars AAPL --days 250
python3 code/alpaca_client.py --clock
python3 code/preflight.py
python3 code/context.py
python3 code/budget.py --remaining
python3 code/thesis.py --check AAPL        # validate a thesis (cited numbers, sell triggers)
python3 code/thesis.py --stale             # which theses need refreshing
python3 code/valuation.py --from inputs.json
python3 code/constitution.py --check state/pending_trades/<id>.json
python3 code/alpaca_client.py --submit state/pending_trades/<id>.json
python3 code/alpaca_client.py --reconcile
python3 code/metrics.py                    # long-run scorecard vs SPY
python3 code/metrics.py --summary          # today's run summary
python3 code/calibration.py --report
python3 code/tuner.py --status
bash code/run_phase.sh {morning|eod|weekly}
```

---

## 7. Stop Rules

Do not trade if:
- `.HALT_TRADING` exists,
- the Alpaca paper API is down or the market is closed,
- the trade fails `python3 code/constitution.py --check <trade_json>`,
- the order is not LIMIT + DAY,
- there isn't enough settled cash, or it would break a hard limit.

If `.HALT_TRADING` exists: place no new orders, do NOT delete the file, log that trading is halted.

---

## 8. Logging Rules

- Machine truth lives in `state/` (JSON/JSONL). Alpaca is the final word on fills.
- Human-readable analysis lives in `docs/` (plain English markdown) — this is required here.
- Submitted trades move to `state/completed_trades/`. Daily summaries go in `state/runs/`.
- State + docs are synced across cloud runs via git (`code/cloud_sync.sh`).

---

## 9. Honesty Rules

- Never say an order filled if it did not (only `--reconcile` decides).
- Never hide a loss. Never invent data, prices, or fundamentals.
- Every number in a thesis must be cited; if data is missing, say what is missing.
- Never claim certainty about future prices.
- If the rules don't cover a situation, stop and ask Chayan.

---

## 10. Core Idea

Own a few wonderful businesses bought at sensible prices. Add slowly. Sell only when the reason
to own them breaks. Beat SPY over years, not days. Keep it honest, and learn from the truth.
