# Glossary — every term, in plain English

If you've never invested before, read this once. The whole system is explained with these words.

### The basics
- **Stock / share**: a tiny piece of ownership in a company. Own a share of Apple and you own a
  (very small) slice of Apple.
- **ETF**: a single fund you can buy that holds many stocks at once. Buying one share of an ETF is
  like buying a basket. Example: **SPY** holds the 500 biggest US companies.
- **Ticker**: a company's short code on the stock market (Apple = AAPL, Microsoft = MSFT).
- **Portfolio**: everything we own.
- **Position / holding**: the shares we own of one company.
- **Cash**: money in the account not yet invested.
- **Equity**: the total value of the account (cash + the current value of all holdings).

### Buying and selling
- **Limit order**: an order to buy or sell only at a set price or better. "Buy AAPL, but pay no
  more than $192." We use these so we never overpay. The opposite is a **market order** (buy at
  whatever the price is right now) — we never use those, because the price could surprise us.
- **DAY order**: an order that only lasts for today. If it doesn't fill by the close, it's cancelled
  and we simply try again tomorrow. All our orders are LIMIT + DAY.
- **Fill**: the order actually went through. **Filled** = done. **Expired** = a DAY limit didn't fill
  and was cancelled at the close (normal and harmless).
- **Reconcile**: ask Alpaca what really happened to our orders. We only believe an order filled when
  reconcile confirms it — we never assume.

### Judging a business (quality)
- **Moat**: a lasting advantage that protects a company from competitors — a beloved brand, a network
  of users, high cost to switch away, low-cost production, or patents. **Wide moat** = very durable.
- **Revenue**: total sales. **Earnings / net income**: profit left after all costs.
- **Gross margin**: out of each $1 of sales, how much is left after the direct cost of the product.
  Higher means more pricing power.
- **ROIC (return on invested capital)**: how much profit the company makes for each dollar it has
  invested in the business. Steadily above ~10–15% is a sign of a great compounding business.
- **Free cash flow (FCF)**: the real cash left over after running and maintaining the business. Cash
  is harder to fake than "earnings," so we like it.
- **Debt**: money the company owes. A little is fine; too much is dangerous.

### Judging the price (value)
- **EPS (earnings per share)**: profit ÷ number of shares.
- **P/E (price-to-earnings)**: the share price ÷ EPS. Roughly, how many years of today's profit you
  pay for the stock. A lower P/E is cheaper (for the same quality).
- **Fair value**: a sensible estimate of what the business is actually worth per share. We compute a
  **band** — a low, base, and high estimate — never one magic number.
- **Margin of safety**: how far the current price sits below our base fair value. If fair value is
  $200 and the price is $170, the margin of safety is 15%. A bigger margin = a bigger cushion if
  we're wrong. We only buy with a margin of safety.

### How we invest
- **Conviction**: how sure we are about a company, 1 (avoid) to 5 (love it). We only buy at 4+.
- **Diversification**: not putting too much in one company or one industry, so one bad surprise can't
  sink us. Hence the limits: max 25% in one name, max 8 names, max ~3 per sector.
- **Sector**: the industry group a company belongs to (technology, health care, energy, …).
- **Dollar-cost-averaging (DCA)**: buying a little at a time instead of all at once, so we don't bet
  everything on one day's price. Our $5,000/day budget forces this.
- **Position weight**: what share of the whole account one holding is (e.g. AAPL = 9% of equity).
- **Thesis**: our written reason for owning a company, plus the exact things that would make us sell.
- **Thesis-break trigger**: a pre-written condition (e.g. "gross margin falls below 40%") that, if it
  happens, tells us to sell — so we decide with a clear head in advance, not in a panic.

### Judging ourselves
- **Benchmark / SPY**: the thing we compare against. Beating SPY over years is the goal.
- **Total return**: how much the account grew, in percent.
- **Drawdown**: how far the account has fallen from its highest point. A −10% drawdown means we're
  10% below the peak. Smaller is better.
- **Volatility**: how bumpy the ride is (how much the value swings). Lower is calmer.
- **Sharpe ratio**: return earned for each unit of bumpiness. Higher is better — it rewards smooth
  gains, not lucky gambles.
- **MAR**: yearly return ÷ worst drawdown. Higher means we made good money without scary dips.

### Safety
- **`.HALT_TRADING`**: an emergency stop file. While it exists, the bot places no new orders. Only a
  human removes it.
- **Paper money**: pretend money on a real market simulation. No real dollars are at risk yet.
- **Constitution**: the hard rules in code that the bot can never break (the limits above).
