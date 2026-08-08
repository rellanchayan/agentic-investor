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

- Six theses on file, zero near-term buy candidates: in a strongly rising market (SPY +11.9% over six months, above its 200-day MA) the broad-market premium flows first to prominent, widely-followed names — and those are the natural targets of thesis research. When no thesis has been in buy range in over two months, redirect at least some weekly research slots toward quality businesses that are lagging the broad market or trading below their own 200-day MA; their temporary price weakness is where a margin of safety is more likely to already exist. Business quality must still meet the full standard; only the research queue priority changes. First observed after six theses and zero buys in 53 calendar days of operation. — 2026-08-08

- A process gap longer than five trading days makes the thesis itself stale, not just the entry-opportunity window. After 11 calendar days without a price check (2026-07-23 to 2026-08-03), the fair-value estimates for MSFT, V, and AAPL may themselves have shifted — earnings releases, guidance, or macro changes can alter what a business is worth, meaning the entry threshold we are waiting for may no longer be correct. On return from any gap of five or more consecutive missed morning reviews, re-verify the underlying business assumptions in each active thesis before using it to set an entry price; a price-only check is not enough. — 2026-08-03
- A future event named in a decision file as a posture-driver or key catalyst creates a specific review obligation for that date — beyond the general daily obligation. The Jul 23 file named "FOMC July 28-29" as a key factor shaping the cautious posture; the system then went dark for Jul 24 and Jul 28-30, missing the event entirely. If a specific date or event appears in a decision file as a catalyst to watch, it is a standing commitment to review on that date. Past-you flagged it in calm deliberation; future-you must show up. — 2026-07-30
- When live thesis candidates exist, a multi-day process gap is not just a documentation failure — it is a potential missed-entry failure. The morning review is the only mechanism that can check whether a candidate's price crossed the buy threshold. Five consecutive days without a write-up (2026-07-14 to 2026-07-21) left MSFT, V, and AAPL unpriced for a full week; whether any of them traded within our margin of safety during that window cannot be recovered from the record. If the system is in watching-mode with named candidates, the morning review is mandatory, not optional. — 2026-07-21
- The end-of-day journal (`docs/journal/<date>.md`) is mandatory every trading day, including days with zero trades. The 2026-07-13 EOD journal was never written, leaving a permanent gap in the post-mortem record. A no-trade day still needs a written close: it documents whether prices moved within range, whether the cautious posture was deliberately reconfirmed, and whether the morning review actually ran. Without it, those questions can never be answered. — 2026-07-14
- Cash held because no name met the margin-of-safety test is disciplined patience; cash held because the morning process did not run is passive inaction. Only a written `docs/decisions/<date>.md` distinguishes the two — from the outside, both look identical. After three missed files in five trading days (2026-06-17, 2026-06-18, 2026-06-22), the rule must be structural: if no decision file exists, treat the day as a process failure, not a hold decision. — 2026-06-22
- The morning cycle must produce a `docs/decisions/<date>.md` every trading day — even when the conclusion is "hold, no orders." Two consecutive days (2026-06-17 and 2026-06-18) had no decision file; future reviews cannot reconstruct intent without one. — 2026-06-18

## Changelog
- 2026-08-08 — Added lesson: in a hot broad market, thesis research gravitates toward well-known premium names where no margin of safety exists; redirect some weekly research slots toward quality names lagging the market or below their own 200-day MA, where fair value is more likely already at hand.
- 2026-08-03 — Added lesson: a gap of 5+ consecutive missed morning reviews makes the thesis's fair-value estimate itself stale, not just the price-check window; on return, re-verify business fundamentals before using any active thesis to set an entry price.
- 2026-07-30 — Added lesson: a future event named in a decision file as a catalyst or posture-driver is a standing commitment to review on that date; missing the FOMC window (Jul 28-29) that was flagged on Jul 23 demonstrates this failure mode.
- 2026-07-21 — Added lesson: multi-day process gaps with live thesis candidates are potential missed-entry failures, not just documentation failures.
- 2026-07-14 — Added lesson: EOD journal is mandatory every trading day, including no-trade days; missing 2026-07-13 EOD is a permanent audit gap.
- 2026-06-22 — Added lesson: missing decision file makes disciplined patience indistinguishable from passive inaction; must be treated as a process failure.
- 2026-06-18 — Added first learned lesson: morning decision file is mandatory every trading day.
- 2026-06-16 — Playbook created with founding principles.
