# Playbook — the rules we've learned

This is the living rulebook the portfolio manager reads every morning. It starts with our founding
principles. The learning-coach adds durable, dated lessons over time as experience teaches us
something real. Keep it as RULES, not a diary. Newest lessons go at the top of "Learned lessons."

## Founding principles (do not delete)
1. **Quality first, price second, patience always.** Only own businesses we understand with a
   durable moat and real free cash flow. Only buy them with a margin of safety. Hold for years.
2. **A missed buy costs nothing; an overpriced buy costs money.** When in doubt, HOLD and keep cash.
3. **Buy slowly.** Use the daily budget to dollar-cost-average; never chase, never bet it all at once.
4. **Sell on a broken thesis, not on a scary headline.** We wrote the sell triggers in calm times;
   we follow them. Reducing risk is always allowed.
5. **Diversify.** Respect the per-name, per-sector, and 8-holding limits even when one idea feels great.
6. **Be honest.** Never claim an unconfirmed fill. Never hide a loss. Cite every number. Prices from
   Alpaca, fundamentals from filings.
7. **Beat SPY over years, on a risk-adjusted basis** (Sharpe and drawdown), not in any single month.
8. **The hard limits are sacred.** They live in code and are never to be worked around.

## Learned lessons

- Writing a rule is not the same as enforcing it. The mandatory-decision-file rule was written on 2026-06-18 and strengthened on 2026-06-22; four consecutive trading days still produced no morning file. A rule that is only in the playbook but has no enforcement gate in the process loop will be silently skipped. The EOD phase must confirm that a decision file exists before marking the day complete; if it does not, the day is flagged as a process failure regardless of how the journal explains it. — 2026-06-26
- Cash held because no name met the margin-of-safety test is disciplined patience; cash held because the morning process did not run is passive inaction. Only a written `docs/decisions/<date>.md` distinguishes the two — from the outside, both look identical. After three missed files in five trading days (2026-06-17, 2026-06-18, 2026-06-22), the rule must be structural: if no decision file exists, treat the day as a process failure, not a hold decision. — 2026-06-22
- The morning cycle must produce a `docs/decisions/<date>.md` every trading day — even when the conclusion is "hold, no orders." Two consecutive days (2026-06-17 and 2026-06-18) had no decision file; future reviews cannot reconstruct intent without one. — 2026-06-18

## Changelog
- 2026-06-26 — Added lesson: a playbook rule with no enforcement gate in the process loop will be silently skipped; writing the rule is not enough.
- 2026-06-22 — Added lesson: missing decision file makes disciplined patience indistinguishable from passive inaction; must be treated as a process failure.
- 2026-06-18 — Added first learned lesson: morning decision file is mandatory every trading day.
- 2026-06-16 — Playbook created with founding principles.
