# agentic-investor

An autonomous, agent-driven **long-term investor** on Alpaca **paper money**. It researches
companies in depth, buys good businesses at fair prices, holds patiently, sells when the reason
to own them breaks, logs everything in plain English, and tries to beat SPY over the years.

**Paper money only.** No real dollars are at risk. See `MIGRATION_CHECKLIST.md` before that ever changes.

## What it does
- Every weekday **morning**: reviews holdings + watchlist, decides buy/trim/sell/hold, places patient
  LIMIT orders within a strict **$5,000/day** budget, and writes `docs/decisions/<date>.md`.
- Every weekday **after the close**: reconciles real fills, writes an honest journal, learns one small thing.
- Every **Saturday**: deep research — refreshes company theses, scouts new names, updates the playbook.

New here? Read `docs/HOW_IT_WORKS.md`, then `docs/GLOSSARY.md`, then `docs/STRATEGY.md` and `docs/RISK.md`.

## Setup (local)
1. Put your Alpaca **paper** keys in `.env` (already gitignored). See `.env.example`.
2. Install dependencies:
   ```bash
   python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
   ```
3. Check the connection:
   ```bash
   .venv/bin/python code/alpaca_client.py --healthcheck
   ```

## Run it by hand (recommended before scheduling)
```bash
bash code/run_phase.sh morning     # gate + reconcile + snapshot + build context
# then the morning skill drives the agents (see .claude/skills/morning/SKILL.md)
bash code/run_phase.sh eod          # reconcile + day summary + record buys
bash code/run_phase.sh weekly       # screen + calibration report
```
In Claude Code you can also run the routines as skills: `/morning`, `/end-of-day`, `/weekly-research`,
and `/halt` (emergency stop).

## Run it automatically (cloud routines)
So you don't have to do anything, schedule the three routines as Claude Code cloud routines (times in
New York / Eastern, which handles daylight saving automatically):
- `/morning` — weekdays at 9:45 AM ET (`45 9 * * 1-5`)
- `/end-of-day` — weekdays at 4:15 PM ET (`15 16 * * 1-5`)
- `/weekly-research` — Saturdays at 9:00 AM ET (`0 9 * * 6`)

On **each** routine, set these environment variables (the cloud doesn't read your local `.env`):
`ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_ENDPOINT=https://paper-api.alpaca.markets`,
`AGENTIC_SYNC=1`, and `GITHUB_TOKEN` (a fine-grained token with Contents: write, so the bot can save
its state/theses/journals back to GitHub between runs).

To save state across cloud runs you need a GitHub remote for this repo (the cloud gets a fresh
checkout each time). `code/cloud_sync.sh` pulls at the start and pushes at the end of each routine.

## Stop it
Create a file named `.HALT_TRADING` in this folder (or run `/halt`). The bot then places no new orders.
Only you can remove that file.

## Layout
- `code/` — the mechanical engine (Alpaca client, constitution, valuation, metrics, tuner, …).
- `state/` — machine truth (config, watchlist, theses, trades, run summaries). Synced via git.
- `docs/` — plain-English analysis (decisions, research, journals, playbook). Synced via git.
- `.claude/agents/` — the 7 specialist agents. `.claude/skills/` — the 4 routines.
