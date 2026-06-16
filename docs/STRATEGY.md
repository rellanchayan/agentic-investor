# Strategy — quality at a fair price

The big idea, in one line: **own a few wonderful businesses bought at sensible prices, hold them
patiently, and sell only when the reason we owned them breaks.** Try to beat SPY over years, with
a smoother ride (less scary drops) than picking randomly.

This is the opposite of day trading. We expect to do *little* most days. Patience is the strategy.

## Step 1 — only consider quality businesses
A "quality" business is durable and profitable. We look for:
- a **moat** (a lasting edge: brand, network, switching costs, low-cost scale, patents),
- steady profits and **positive free cash flow** (real leftover cash),
- a healthy balance sheet (not too much debt),
- a product likely still wanted in 10 years,
- big and liquid enough to trade easily.

The research analyst captures this in each company's thesis and gives a **conviction** score 1–5.

## Step 2 — estimate what it's worth (fair value)
A great company can still be a bad investment if you overpay. So we estimate a **fair-value band**
(low / base / high) using simple, transparent math the code does for us (`valuation.py`):
- **earnings multiple** (price vs earnings per share),
- **free-cash-flow yield** (price vs the cash it throws off),
- a **dividend** check for dividend payers,
- a simple **discounted-cash-flow** estimate.

Then we measure the **margin of safety** = how far today's price is below the base fair value.

## Step 3 — the decision (every morning, per company)
- **BUY / ADD** only when: conviction is high (≥ 4), the margin of safety clears our bar (≥ 12%,
  and more when the market posture is cautious), there's room (the sector isn't already full and we
  hold fewer than 8 names, or we already own it), and the daily budget has room.
- **TRIM** (sell part) when: a position is getting near the 25% cap, OR the price has risen above
  the high end of fair value (now expensive), OR our conviction slipped.
- **SELL** (exit) when: a pre-written **thesis-break trigger** fires (e.g. "gross margin falls below
  40% for two quarters"), OR conviction drops below 3. Reducing risk is always allowed.
- **HOLD** otherwise — the usual, correct answer. *A missed buy costs nothing; an overpriced buy
  costs money.*

## Step 4 — buy slowly (dollar-cost-averaging)
A full position is about 10% of the account. But we can only deploy **$5,000 of new money per day**.
So we build a position over many days, a tranche at a time, and never bet everything on one day's
price. Each morning the manager funds the single best opportunity with that day's budget.

## Step 5 — patient pricing
We use **LIMIT + DAY** orders only. We set the buy limit near the current price plus a tiny buffer,
and we're happy to wait. If an order doesn't fill today, it expires and we simply try again tomorrow
if the name is still attractive. We never use market orders, so we never get an ugly surprise fill.

## Step 6 — judge ourselves honestly
We compare our **Sharpe ratio, drawdown, and total return to SPY**. The goal is to beat SPY over
years with a smoother ride — not to win any single month. Raw monthly return is a trap; risk-adjusted
results over time are the real scorecard.

## Why these guardrails
Concentration limits (25% per name, 8 names, ~3 per sector) and the slow daily budget mean no single
mistake can ruin us. We'd rather miss some upside than risk a permanent loss. That discipline is what
makes the strategy realistic enough to one day run with real money.
