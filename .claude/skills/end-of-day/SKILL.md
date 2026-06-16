---
name: end-of-day
description: The weekday after-close routine. Finds out what actually filled, writes an honest journal, and learns one small lesson. Paper trading only.
allowed-tools: Bash(bash code/run_phase.sh *), Bash(bash code/cloud_sync.sh *), Bash(python3 code/*), Bash(.venv/bin/python code/*), Read, Edit(state/**), Edit(docs/**)
---

# End of Day

Runs once each weekday after the 4:00 PM New York close. Its only job is honesty and
learning: record what truly happened today, then improve by a little.

## Step 0 — load saved memory (cloud)
```bash
bash code/cloud_sync.sh pull
```

## Step 1 — the mechanical truth
```bash
bash code/run_phase.sh eod
```
This reconciles every order against Alpaca (the only source of fill truth), snapshots
equity into the history, writes `state/runs/<today>-summary.json`, prints the long-run
scorecard vs SPY, and records the conviction of any newly-filled buys.

## Step 2 — write the honest journal
Run the **journal-writer** (`.claude/agents/journal-writer.md`). It reads the day summary
and the reconciled trades and writes:
- `docs/journal/<today>.md` — what we planned, what actually filled, today's result
  (realized + unrealized), and 1–3 plain lessons. Every number comes from the tools, not
  memory.
- `docs/trades/<today>.md` — a short card for each order that filled today.
- a **thesis post-mortem** appended to `docs/research/<TICKER>.md` for any name we SOLD
  today (was the thesis right? what did we miss? did the sell trigger work?).

## Step 3 — learn one small thing (the learning coach)
Run the **learning-coach** (`.claude/agents/learning-coach.md`). It:
- runs the gated, reversible tuner (`tuner.py --status` then, only if a rule fires and the
  gate is open, `tuner.py --run`). Most days it changes nothing — that is healthy.
- adds at most one durable, dated lesson to `docs/PLAYBOOK.md` if today taught us something.
It can NEVER change a hard limit.

## Step 4 — save memory (cloud)
```bash
bash code/cloud_sync.sh push eod
```
Then stop. Never say an order filled if it did not. Never hide a loss.
