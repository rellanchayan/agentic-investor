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

- Several named watchlist names (NKE, MCD, WMT, AVGO) corrected 10-35% in Q3 2026 while carrying no filing-backed thesis — corrections on un-valued names cannot be acted on. A watchlist is not a thesis bench: naming a business as worth researching and completing a valuation of it are different acts, and only the second one lets you buy. Thesis work must be done in calm conditions before a name corrects; writing one during a falling-price window is faster, more rushed, and likely to be worse. When prioritizing which theses to build next, rank watchlist names by "most likely to reach a fair price in the next six months" — those are the ones where preparation has the highest option value. — 2026-08-29

- At 73 days with zero fills, cash drag reached a measured 2.49 pp deficit vs SPY — the first concrete number attached to sustained inaction. Prior lessons named bench expansion as urgent; this number makes the cost explicit: at the SPY pace seen since inception, holding all cash costs roughly 1 pp per month. The lesson is not to lower standards, but that "expand the thesis bench" is now an obligation with a measurable, compounding price tag, not a preference to satisfy when convenient. Every week the bench stays at three deeply-overvalued names is a week that cost cannot be recovered. — 2026-08-28

- Four separate multi-day morning-cycle gaps in 66 days of operation (Jun 17-22, Jul 14-21, Jul 23-Aug 3, Aug 17-21) confirm a structural execution failure, not an isolated oversight. Writing further lessons about missing reviews has not changed behavior. The morning cycle must be automated and externally triggered; until it is, every parameter setting and thesis target is irrelevant — the process that would act on them is not running. Tuning is not the fix. — 2026-08-21
- When every named thesis candidate trades well above entry thresholds (here, 33-47% above as of 2026-08-19), diligent morning reviews still produce "hold cash" indefinitely — the bottleneck is bench coverage, not process compliance. A thesis bench of only three deeply overvalued names is not a valid position; it is a capability gap. When no named candidate is within 20% of its entry price, expanding the thesis bench to include more quality names at different valuations is the primary investment obligation, not optional weekend research. — 2026-08-19
- A process gap longer than five trading days makes the thesis itself stale, not just the entry-opportunity window. After 11 calendar days without a price check (2026-07-23 to 2026-08-03), the fair-value estimates for MSFT, V, and AAPL may themselves have shifted — earnings releases, guidance, or macro changes can alter what a business is worth, meaning the entry threshold we are waiting for may no longer be correct. On return from any gap of five or more consecutive missed morning reviews, re-verify the underlying business assumptions in each active thesis before using it to set an entry price; a price-only check is not enough. — 2026-08-03
- A future event named in a decision file as a posture-driver or key catalyst creates a specific review obligation for that date — beyond the general daily obligation. The Jul 23 file named "FOMC July 28-29" as a key factor shaping the cautious posture; the system then went dark for Jul 24 and Jul 28-30, missing the event entirely. If a specific date or event appears in a decision file as a catalyst to watch, it is a standing commitment to review on that date. Past-you flagged it in calm deliberation; future-you must show up. — 2026-07-30
- When live thesis candidates exist, a multi-day process gap is not just a documentation failure — it is a potential missed-entry failure. The morning review is the only mechanism that can check whether a candidate's price crossed the buy threshold. Five consecutive days without a write-up (2026-07-14 to 2026-07-21) left MSFT, V, and AAPL unpriced for a full week; whether any of them traded within our margin of safety during that window cannot be recovered from the record. If the system is in watching-mode with named candidates, the morning review is mandatory, not optional. — 2026-07-21
- The end-of-day journal (`docs/journal/<date>.md`) is mandatory every trading day, including days with zero trades. The 2026-07-13 EOD journal was never written, leaving a permanent gap in the post-mortem record. A no-trade day still needs a written close: it documents whether prices moved within range, whether the cautious posture was deliberately reconfirmed, and whether the morning review actually ran. Without it, those questions can never be answered. — 2026-07-14
- Cash held because no name met the margin-of-safety test is disciplined patience; cash held because the morning process did not run is passive inaction. Only a written `docs/decisions/<date>.md` distinguishes the two — from the outside, both look identical. After three missed files in five trading days (2026-06-17, 2026-06-18, 2026-06-22), the rule must be structural: if no decision file exists, treat the day as a process failure, not a hold decision. — 2026-06-22
- The morning cycle must produce a `docs/decisions/<date>.md` every trading day — even when the conclusion is "hold, no orders." Two consecutive days (2026-06-17 and 2026-06-18) had no decision file; future reviews cannot reconstruct intent without one. — 2026-06-18

## Changelog
- 2026-08-29 — Added lesson: several watchlist names (NKE, MCD, WMT, AVGO) corrected 10-35% in Q3 2026 with no thesis ready; a watchlist name without a completed valuation is false preparation — you cannot act on a correction you cannot measure. Prioritize thesis-building on names most likely to reach fair value in the next six months.
- 2026-08-28 — Added lesson: cash drag reached a measured 2.49 pp deficit vs SPY after 73 days of zero fills; bench expansion now carries an explicit, compounding cost of roughly 1 pp per month.
- 2026-08-21 — Added lesson: four multi-day morning-cycle gaps in 66 days is a structural execution failure, not a parameter problem; automation is the fix, not another written rule.
- 2026-08-19 — Added lesson: a bench of only 3 deeply overvalued names is a capability gap, not a valid posture; expanding the thesis bench is the primary investment obligation when no named candidate is within 20% of its entry price.
- 2026-08-03 — Added lesson: a gap of 5+ consecutive missed morning reviews makes the thesis's fair-value estimate itself stale, not just the price-check window; on return, re-verify business fundamentals before using any active thesis to set an entry price.
- 2026-07-30 — Added lesson: a future event named in a decision file as a catalyst or posture-driver is a standing commitment to review on that date; missing the FOMC window (Jul 28-29) that was flagged on Jul 23 demonstrates this failure mode.
- 2026-07-21 — Added lesson: multi-day process gaps with live thesis candidates are potential missed-entry failures, not just documentation failures.
- 2026-07-14 — Added lesson: EOD journal is mandatory every trading day, including no-trade days; missing 2026-07-13 EOD is a permanent audit gap.
- 2026-06-22 — Added lesson: missing decision file makes disciplined patience indistinguishable from passive inaction; must be treated as a process failure.
- 2026-06-18 — Added first learned lesson: morning decision file is mandatory every trading day.
- 2026-06-16 — Playbook created with founding principles.
