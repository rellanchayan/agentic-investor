# Migration checklist — before any real money

This project is **paper-only** today, and the code is hard-wired that way. This checklist is the
gate that must be fully satisfied before even thinking about real dollars. Treat it as a contract
with yourself. Nothing here is automatic — a human decides.

## A. The code is true and tested
- [ ] All offline unit tests pass (`code/tests/`): constitution, valuation, thesis.
- [ ] A bad order is reliably refused by `constitution.py --check` (over-budget, >25%, >8 names,
      market order, no thesis, no reason, not enough cash).
- [ ] `.HALT_TRADING` blocks every submit; the bot never deletes it.
- [ ] Sells are never blocked by the daily budget (risk reduction always possible).
- [ ] Orders are idempotent (the same `trade_id` never double-submits).
- [ ] Unfilled DAY limits are handled: the next morning re-prices and re-attempts if still wanted.
- [ ] Missed-run catch-up: if a morning run is skipped, the next run reconciles and reviews safely.
- [ ] `_require_paper()` and `check_live_mode_forbidden` both refuse a live endpoint (verified).

## B. A real paper track record (12–24 months, at least one full market cycle)
- [ ] We lived through at least one real downturn and recovery while invested.
- [ ] We held a thesis that broke and exited it cleanly via its pre-written trigger (with a
      post-mortem in `docs/research/`).
- [ ] **Sharpe ratio ≥ SPY** and **MAR ≥ SPY**, with **lower max drawdown** than SPY, over the
      track record (`metrics.py`).
- [ ] Conviction is calibrated: high-conviction buys actually outperformed low-conviction ones
      (`calibration.py --report`).
- [ ] Zero violations of any hard limit or the daily budget across the whole record.
- [ ] Theses are consistently **filing-backed**, not aggregator-only or incomplete.
- [ ] LIMIT fill rate is healthy and understood (we know how often patient limits miss).

## C. Operational guardrails before the first real dollar
- [ ] A **separate** live account and a **separate, new** live code path that does not yet exist —
      the paper code in this repo stays paper-only forever.
- [ ] Fund in stages (e.g. 10–25% first), not all at once.
- [ ] Re-confirm the hard limits for the real account size (the $5,000/day budget and the 25% / 8-name
      caps may need to be re-chosen for real capital).
- [ ] A written, pre-committed rule that **lagging SPY in a bull market will NOT** trigger abandoning
      the discipline or loosening the limits.
- [ ] The `.HALT_TRADING` kill-switch is documented and tested on the live path.
- [ ] Taxes, fees, and real-fill slippage are modeled and understood.
- [ ] A human reviews and signs off. When the rules don't cover something, stop and ask.

> Reminder: strong paper results are necessary but **not sufficient**. Paper money has no fees, no
> taxes, idealized fills, and no emotional pressure. Respect the difference.
