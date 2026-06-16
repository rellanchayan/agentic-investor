# Apple Inc. (AAPL) — Research Thesis

**As of:** FY2025 (fiscal year ended Sept 27, 2025) | **Written:** 2026-06-16
**Price (Alpaca):** $297.46 | **Verdict:** Wonderful business, expensive price.

## What Apple does (plain English)
Apple designs and sells premium consumer hardware — iPhone, Mac, iPad, Apple Watch,
AirPods — and an increasingly large, high-margin **Services** business (App Store,
iCloud, Apple Music/TV+, AppleCare, advertising, payments). It makes money two ways:
selling devices at strong margins, then earning a recurring, software-like cut from the
~2.4-billion active devices already in people's hands. iPhone is still the biggest single
product line ($209.6B of FY2025's $416.2B revenue, per stockanalysis/SEC), but Services
is the profit engine that keeps growing and carries much higher margins than hardware.

## The moat — WIDE
- **Switching costs / ecosystem lock-in:** iMessage, iCloud, Apple Watch pairing, App
  Store purchases, Continuity between devices. Leaving Apple means losing all of it.
- **Brand & pricing power:** Apple commands premium prices and 46.9% company-wide gross
  margin (FY2025) — extraordinary for a hardware company.
- **Installed base network effect:** ~2.4B active devices (company-reported record) feed a
  recurring Services stream that competitors cannot easily replicate.
- **Capital efficiency:** ROIC is enormous (well over 50%) because Apple returns almost all
  cash to shareholders, keeping invested capital tiny relative to profits.

## Key numbers (all cited — see sources)
| Metric | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Revenue | $416.16B | $391.04B | $383.29B |
| Gross margin | 46.9% | 46.2% | 44.1% |
| Net income | $112.01B | $93.74B | $96.99B |
| Diluted EPS | $7.46 | $6.09 | $6.13 |
| Operating cash flow | $111.48B | $118.25B | $110.54B |
| Free cash flow | $98.77B | $108.81B | $99.58B |

- **Revenue growth:** +6.4% in FY2025; but the 3-year CAGR (FY2022→FY2025) is only ~1.8% —
  Apple is a slow grower, not a fast one. The FY2025 net-income jump is partly because FY2024
  carried a one-time European tax charge.
- **Net debt:** total debt $98.66B minus cash & short-term investments $54.70B ≈ **$44B net
  debt**. Against ~$145B EBITDA that is **~0.3x net-debt/EBITDA** — very conservative.
- **FCF positive:** yes, strongly — $98.8B FCF in FY2025. FCF/share ≈ $6.58.
- **Capital return:** $96.7B of buybacks + $15.4B dividends in FY2025; share count fell from
  15.4B to 15.0B diluted shares.

## Fair value
Computed with `code/valuation.py` blending two methods on cited FY2025 figures:
- **P/E:** EPS $7.46 × {24, 29, 34}. Even 34x is generous for ~2-6% revenue growth, but
  reflects Apple's quality and Services mix.
- **FCF yield:** FCF/share $6.58 at {4.5%, 3.8%, 3.2%} yields.

**Fair value band: ~$163 (low) / $195 (base) / $230 (high).**

At today's **$297.46**, the price sits **above the high end** — a **margin of safety of about
-53% versus the base case** (i.e. the stock is ~53% above our base fair value). At ~40x
trailing earnings and a ~2.2% FCF yield, the market is pricing in re-acceleration (AI features,
Services growth) that our cited fundamentals do not yet show.

## Risks (as hard as the bull case)
- **Valuation risk is the dominant risk.** Even a great business is a poor investment if
  bought at ~40x earnings with low single-digit revenue growth.
- **iPhone concentration:** ~half of revenue still rides on one product in a saturated,
  replacement-cycle market.
- **China:** large revenue and manufacturing exposure to geopolitical and competitive risk.
- **Regulatory / App Store:** antitrust and the EU Digital Markets Act threaten the
  high-margin Services take-rate (the Google search-default payment is also under attack).
- **AI execution:** Apple has been seen as a laggard in generative AI; the premium assumes it
  catches up.

## Sell triggers (what would break the thesis)
1. Company-wide **gross margin falls below 42%** for two consecutive quarters.
2. **Revenue shrinks year-over-year for two consecutive fiscal years.**
3. **Services revenue growth turns negative** for two consecutive quarters (the moat engine).
4. **Net-debt/EBITDA rises above 1.5x** (a sign of strained capital discipline).
5. A **forced material change to the App Store model** (regulatory) that visibly cuts Services
   margin or revenue.
6. Any **serious accounting red flag** or restatement.

Note for the PM: this is a HOLD/WATCH on price, not a buy here. It would become interesting
on a pullback into roughly the $200-$230 zone (base-to-high fair value).

## Sources
- Apple FY2025 10-K (SEC EDGAR): https://www.sec.gov/Archives/edgar/data/0000320193/000032019325000079/aapl-20250927.htm
- Apple Q4 FY2025 8-K earnings release (SEC EDGAR): https://www.sec.gov/Archives/edgar/data/0000320193/000032019325000077/a8-kex991q4202509272025.htm
- Apple Newsroom Q4 FY2025 press release: https://www.apple.com/newsroom/2025/10/apple-reports-fourth-quarter-results/
- Financial line items cross-check: https://stockanalysis.com/stocks/AAPL/financials/
- Balance sheet: https://stockanalysis.com/stocks/AAPL/financials/balance-sheet/
- Cash flow: https://stockanalysis.com/stocks/AAPL/financials/cash-flow-statement/
- Price: Alpaca quote feed (2026-06-16), $297.46
