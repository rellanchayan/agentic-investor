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

- When live thesis candidates exist, a multi-day process gap is not just a documentation failure — it is a potential missed-entry failure. The morning review is the only mechanism that can check whether a candidate's price crossed the buy threshold. Five consecutive days without a write-up (2026-07-14 to 2026-07-21) left MSFT, V, and AAPL unpriced for a full week; whether any of them traded within our margin of safety during that window cannot be recovered from the record. If the system is in watching-mode with named candidates, the morning review is mandatory, not optional. — 2026-07-21
- The end-of-day journal (`docs/journal/<date>.md`) is mandatory every trading day, including days with zero trades. The 2026-07-13 EOD journal was never written, leaving a permanent gap in the post-mortem record. A no-trade day still needs a written close: it documents whether prices moved within range, whether the cautious posture was deliberately reconfirmed, and whether the morning review actually ran. Without it, those questions can never be answered. — 2026-07-14
- Cash held because no name met the margin-of-safety test is disciplined patience; cash held because the morning process did not run is passive inaction. Only a written `docs/decisions/<date>.md` distinguishes the two — from the outside, both look identical. After three missed files in five trading days (2026-06-17, 2026-06-18, 2026-06-22), the rule must be structural: if no decision file exists, treat the day as a process failure, not a hold decision. — 2026-06-22
- The morning cycle must produce a `docs/decisions/<date>.md` every trading day — even when the conclusion is "hold, no orders." Two consecutive days (2026-06-17 and 2026-06-18) had no decision file; future reviews cannot reconstruct intent without one. — 2026-06-18

## Changelog
- 2026-07-21 — Added lesson: multi-day process gaps with live thesis candidates are potential missed-entry failures, not just documentation failures.
- 2026-07-14 — Added lesson: EOD journal is mandatory every trading day, including no-trade days; missing 2026-07-13 EOD is a permanent audit gap.
- 2026-06-22 — Added lesson: missing decision file makes disciplined patience indistinguishable from passive inaction; must be treated as a process failure.
- 2026-06-18 — Added first learned lesson: morning decision file is mandatory every trading day.
- 2026-06-16 — Playbook created with founding principles.
