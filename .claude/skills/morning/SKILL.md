---
name: morning
description: The weekday-morning routine. Reviews the portfolio and watchlist like a long-term investor and decides what to buy, trim, sell, or leave alone — then places patient LIMIT orders. Paper trading only.
allowed-tools: Bash(bash code/run_phase.sh *), Bash(bash code/cloud_sync.sh *), Bash(python3 code/*), Bash(.venv/bin/python code/*), Read, Edit(state/**), Edit(docs/**), WebSearch, WebFetch
---

# Morning

Runs once each weekday, a little after the 9:30 AM New York open (so prices are live).
This is the heart of the system: think like a patient investor, act rarely, write down
why. Paper money only.

## Step 0 — load saved memory (cloud)
```bash
bash code/cloud_sync.sh pull
```

## Step 1 — the mechanical gate + snapshot
```bash
bash code/run_phase.sh morning
```
This runs the cheap safety gate (`preflight.py`) and, only if it says PROCEED, reconciles
yesterday's still-open orders, snapshots the account/positions, and builds today's
`state/day/<today>/context.json` (today = New York date).

Read the printed verdict and branch:
- **EXIT** (market closed / `.HALT_TRADING` present / Alpaca unreachable): do NOTHING.
  Write one honest line to `docs/decisions/<today>.md` saying why (e.g. "Market closed
  today — no review."), then go to Step 6. If `.HALT_TRADING` exists, never delete it.
- **PROCEED**: continue to Step 2.

## Step 2 — read the market "weather"
Run the **market-weather-analyst** (`.claude/agents/market-weather-analyst.md`). It writes
`docs/macro/<today>.md` and `state/day/<today>/macro.json` with a posture:
*opportunistic / normal / cautious*. A cautious posture means demand a bigger discount
before buying.

## Step 3 — refresh any stale research that matters today
```bash
.venv/bin/python code/thesis.py --stale
```
For any name we **hold** or any **candidate** we might act on today whose thesis is
`stale` or missing, run the **research-analyst** (`.claude/agents/research-analyst.md`)
on that one ticker to refresh `state/theses/<TICKER>.json`. Do NOT refresh names you have
no intention of acting on — keep it focused. If nothing relevant is stale, skip this step.

## Step 4 — decide (the portfolio manager)
Run the **portfolio-manager** (`.claude/agents/portfolio-manager.md`). It reads the
context, the macro posture, the theses, and the remaining $5,000 daily budget, then:
- writes one trade file per order to `state/pending_trades/`,
- writes the full plain-English analysis to `docs/decisions/<today>.md`
  (what / price / why / why-it's-the-right-choice / risks / budget used, plus the HOLD
  list and the "waiting for a better price" watchlist).
Most mornings the right answer is mostly HOLD. That is fine.

## Step 5 — independent risk check, then submit
For EACH file in `state/pending_trades/`:
1. Run the **risk-officer** (`.claude/agents/risk-officer.md`) on it. It returns PASS or VETO.
2. If VETO, leave the order unsubmitted and note it in the decisions doc. Do not argue.
3. If PASS, submit it (the constitution runs again inside `--submit`; it is safe to call twice):
```bash
.venv/bin/python code/constitution.py --check state/pending_trades/<file>.json
.venv/bin/python code/alpaca_client.py --submit state/pending_trades/<file>.json
```
Never claim an order filled — a DAY limit may fill later or expire. Only `--reconcile`
(run tomorrow morning and at end of day) decides what actually filled.

## Step 6 — save memory (cloud)
```bash
bash code/cloud_sync.sh push morning
```
Then stop. Golden rule: a missed buy costs nothing; an overpriced buy costs money.
