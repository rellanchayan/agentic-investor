---
name: weekly-research
description: The weekend deep-research routine. Refreshes company theses, hunts for new quality businesses, and folds calibration findings into the playbook. Paper trading only; places no orders.
allowed-tools: Bash(bash code/run_phase.sh *), Bash(bash code/cloud_sync.sh *), Bash(python3 code/*), Bash(.venv/bin/python code/*), Read, Edit(state/**), Edit(docs/**), WebSearch, WebFetch
---

# Weekly Research

Runs once a week (Saturday morning ET, market closed). This is the slow, deep thinking
the daily routine has no time for. It places NO orders.

## Step 0 — load saved memory (cloud)
```bash
bash code/cloud_sync.sh pull
```

## Step 1 — the mechanical snapshot
```bash
bash code/run_phase.sh weekly
```
This refreshes prices, writes a liquidity + trend snapshot of the watchlist to
`state/day/<today>/screen.json`, and prints the conviction-calibration report.

## Step 2 — refresh the theses on rotation
```bash
.venv/bin/python code/thesis.py --stale
```
Run the **research-analyst** (`.claude/agents/research-analyst.md`) on the names that are
stale or invalid — prioritise names we **hold**, then the strongest **candidates**. Aim to
refresh a handful each week so every thesis is re-checked at least quarterly. Each refresh
must keep its numbers **cited** (`thesis.py --check <TICKER>` must pass).

## Step 3 — hunt for new quality businesses
Run the **candidate-scout** (`.claude/agents/candidate-scout.md`). It proposes new names
for `state/watchlist.txt` (updating `state/sectors.json` too) and writes
`docs/research/candidates-<today>.md`. It proposes; it never buys.

## Step 4 — fold the lessons in
Run the **learning-coach** (`.claude/agents/learning-coach.md`) in review mode: read the
calibration report and the week's journals, and add any durable lesson to
`docs/PLAYBOOK.md` (e.g. "conviction-5 buys have outperformed — trust them more" or the
opposite). It can NEVER change a hard limit.

## Step 5 — save memory (cloud)
```bash
bash code/cloud_sync.sh push weekly
```
Then stop. Deep research is how next week's decisions get smarter.
