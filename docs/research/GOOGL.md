# GOOGL — Alphabet Inc. (research thesis)

*As of FY2025 (year ended 2025-12-31). Retrieved 2026-06-20. Refresh due ~2026-09-18.*
*Price from Alpaca; all fundamentals from Alphabet's official Q4/FY2025 earnings release and SEC filings.*

## What the company does (in plain English)
Alphabet is the parent of Google. It earns money three ways:

1. **Google Services** — the cash engine. Search advertising, YouTube (ads + subscriptions),
   Android, Chrome, Google Play, and consumer subscriptions (Google One, YouTube Premium —
   over 325M paid subs). Q4 2025 revenue $95.9B; Q4 operating income $40.1B.
2. **Google Cloud** — the fast-growing second engine. Cloud infrastructure (GCP), Workspace,
   and enterprise AI. Q4 2025 revenue $17.7B, up **48%** year-over-year, now a **>$70B annual
   run rate**, and newly profitable ($5.3B Q4 operating income).
3. **Other Bets** — Waymo and small ventures; loss-making and immaterial to value today.

FY2025 total revenue was **$402.8B (+15%)** — the first year ever above $400B.

## Why it has a moat (wide)
Google Search has dominant share of the world's information queries, with a data-and-distribution
flywheel: more usage → better results/ads → more usage. YouTube leads online video. Android and
Chrome control how billions of people reach the web. On top of that, Alphabet owns the **full AI
stack** — frontier Gemini models, custom TPU chips, and a global data-center footprint — which it
uses to defend Search and grow Cloud. Management says Search usage is at record highs and the
Gemini app passed **750M monthly active users**, suggesting (so far) that AI is expanding rather
than cannibalizing Search. I rate the moat **wide**.

## The key numbers (all cited)
| Metric | FY2025 | Source |
|---|---|---|
| Revenue | $402.836B (+15.1% YoY; FY2023 $307.394B → 14.5% 3y CAGR) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) / [FY23 cross-check](https://www.macrotrends.net/stocks/charts/GOOGL/alphabet/revenue) |
| Gross margin | 59.7% (gross profit $240.301B) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) |
| Operating margin | 32.0% (op income $129.039B) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) |
| Net income / diluted EPS | $132.170B / $10.81 (GAAP) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) |
| Free cash flow | ~$73.27B (OCF $164.713B − capex $91.447B) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) |
| Balance sheet | ~$80B net cash (cash+marketables $126.843B vs LT debt $46.547B) | [IR release](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) |
| ROE | ~35.7% on average equity | computed from IR figures |

**Two honesty notes on the numbers:**
- GAAP net income ($132.2B) is **inflated by ~$24.6B of pre-tax mark-to-market gains on equity
  securities** — a volatile, non-operating item. Stripping the ~$20.5B after-tax portion gives a
  **normalized diluted EPS of ~$9.13** (vs GAAP $10.81). I used the normalized figure for valuation.
- Free cash flow is **depressed by an AI-capex surge**: capex nearly doubled to $91.4B in FY2025,
  and 2026 guidance is **$175–185B**. So today's ~$73B FCF understates the steady-state cash the
  core business could throw off — but those returns are unproven, so I do not give credit for them.

## Fair value (how I got it)
Computed with `code/valuation.py`, blending two methods:
- **P/E:** normalized EPS $9.13 × multiples 24 / 28 / 32 → $219 / $256 / $292.
- **FCF yield:** FCF/share $5.99 at 4.0% / 3.5% / 3.0% → $150 / $171 / $200.

**Blended fair value: low $184 · base $213 · high $246.**

The FCF method is deliberately harsh because capex is at a cyclical peak; if the AI buildout earns
its cost of capital, normalized FCF (and fair value) would be materially higher than this band.

**Current price $367.93 sits far above even the high end.** Margin of safety at the base case is
about **−72%** — i.e., the market is pricing in years of strong growth, margin durability, and a
big payoff from AI capex. There is **no margin of safety today.**

## Conviction: 4 / 5
This is a genuinely wonderful business (wide moat, ~60% gross margin, ~36% ROE, net cash, two growth
engines). The "4" reflects business quality, not the entry price. The price is the problem, not the
company. Suggested target weight if/when bought with a margin of safety: ~10%.

## The real risks (as hard as the bull case)
- **Valuation.** ~40x normalized EPS and a capex-depressed ~3.8% FCF yield. Priced for success.
- **AI capex bet.** $91B in FY2025, $175–185B guided for 2026. If returns disappoint, FCF and ROIC fall.
- **AI as a threat to the core.** AI answer engines could erode the high-margin Search ad model.
- **Antitrust.** Google lost the U.S. DOJ search-monopoly case; remedies (default-deal limits, data
  sharing, or structural relief) plus separate ad-tech litigation could hit the most profitable parts.
- **Earnings quality.** Volatile equity-securities gains flatter GAAP EPS.
- **Dual-class control.** Founders hold voting control; minority holders have limited say.

## Sell triggers (the rules the manager will follow)
1. Google Services (ad) revenue declines YoY for **two consecutive quarters**.
2. Total revenue growth falls below **8%** for two consecutive quarters with no margin offset.
3. Google Cloud growth falls below **20%** for two consecutive quarters.
4. Consolidated operating margin falls below **25%** for two consecutive quarters.
5. Free cash flow turns negative for a full year, or net cash flips to net debt above 1.5x EBITDA.
6. A regulatory remedy forces a structural break-up or materially cuts Search/ad-tech revenue or margin.
7. Any serious accounting restatement or governance red flag.

## What would make me want to buy
A pullback toward the **$245 high / $213 base** zone would open a real margin of safety. Short of that,
evidence that AI capex is earning its keep (Cloud margins expanding, FCF re-accelerating) could justify
a higher fair-value band on the next refresh.

*Sources: [Alphabet Q4/FY2025 earnings release (IR)](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/2025q4-alphabet-earnings-release.pdf) · [Alphabet Q1 2026 10-Q (SEC)](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm) · [FY2023 revenue cross-check (Macrotrends)](https://www.macrotrends.net/stocks/charts/GOOGL/alphabet/revenue) · Price: Alpaca paper market data.*
