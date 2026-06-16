# Risk — every safety rule, in one place

This system is built to be safe and honest first, profitable second. Here is everything that
protects the account.

## Hard limits (in code — `code/constitution.py` — the bot can NEVER break these)
| Rule | Limit | Why |
|---|---|---|
| Paper only | `paper-api.alpaca.markets` enforced twice | No real money is ever at risk in this build |
| Order type | LIMIT + DAY only | Never an ugly surprise fill from a market order |
| Daily buy budget | $5,000 of new buys per day | Buys slowly; never bets everything at one price |
| Per-trade cap | $5,000 max per single buy | One order can't blow the day's budget |
| Per-name cap | ≤ 25% of the account in one ticker | One company can't sink us |
| Holdings cap | ≤ 8 names | Stay diversified and focused |
| Cash only | spend settled cash, never buying power | No margin, no leverage, no borrowed risk |
| Frequency | ≤ 20 trades/day, ≤ 50/week | No frantic over-trading |
| Reason required | every trade needs a real written reason | "No reason = no trade" |
| Thesis required | every BUY must cite a valid thesis | We never buy something we haven't researched |
| No day trading | no buying and selling the same name the same day | We're investors, not traders |

These are constants in code, not settings. A confused agent or a corrupted config file cannot
loosen them. The tuner is structurally unable to touch them.

## Soft guidelines (in `state/config.json` — may be nudged within `state/param_bounds.json`)
Things like the required margin of safety, the conviction bar, the target position size, and how
far past the quote to set a limit. These are guidelines the manager follows; the tuner may adjust
them by tiny, logged, reversible steps — but always inside hard bounds, and never while we're
losing money.

## The kill-switch: `.HALT_TRADING`
- Create a file named `.HALT_TRADING` in the project root (or run `/halt`) to stop all new orders.
- While it exists: the morning gate exits, `--submit` refuses, and the constitution fails every order.
- It does NOT sell anything by itself. **Only a human removes it.** The bot must never delete it.

## Automatic "do nothing" cases (the morning gate, `preflight.py`)
The morning routine does nothing at all if: `.HALT_TRADING` exists, the market is closed (Alpaca's
clock is the authority on holidays/half-days), or Alpaca is unreachable. Safe by default.

## Honesty protections
- We only believe an order filled when `--reconcile` confirms it against Alpaca.
- Every number in a thesis must be **cited**; `thesis.py --check` rejects uncited numbers.
- Prices come only from Alpaca, never the web. Fundamentals come from filings, with sources.
- The journal reports losses as plainly as gains.

## What this does NOT protect against (be honest)
- **Being wrong about a business.** Guardrails limit the damage of any one mistake; they don't make
  our judgment correct.
- **Paper vs. real life.** Paper fills are idealized. Real trading adds fees, worse fills, taxes, and
  the emotional pressure of real money. Strong paper results are necessary but not sufficient.
- **Market crashes.** We will fall when the market falls; we aim to fall *less* and recover, not to
  dodge every drop.

When the rules don't cover a situation, the right move is to stop and ask a human.
