# Apple Inc. (AAPL) — Research Thesis

**Thesis ID:** AAPL-2026Q3 · **As of:** fiscal Q3 2026 (quarter ended 2026-06-27)
**Written:** 2026-09-17 · **Refresh due:** 2026-10-17 (FY2026 Q4 earnings land late October)
**Price used:** $332.55 (Alpaca) · **Conviction:** 3 / 5
**Verdict: wonderful business, wrong price. Do not buy here.**

---

## 1. What the company actually does, in plain words

Apple sells premium consumer electronics — iPhone, Mac, iPad, Apple Watch, AirPods — and then
sells the same customer software and subscriptions for years afterwards through Services (App
Store, iCloud, Apple Music, Apple TV+, AppleCare, advertising, payments, and a fee from Google
for being the default search engine).

In the June 2026 quarter, revenue was **$109.417B**, split roughly:

| Line | Q3 FY2026 | Share of revenue | vs a year ago |
|---|---|---|---|
| iPhone | $54.252B | 49.6% | +21.7% |
| Services | $30.739B | 28.1% | +12.1% |
| Mac | $10.352B | 9.5% | +28.7% |
| Wearables/Home/Accessories | $7.883B | 7.2% | +6.5% |
| iPad | $6.191B | 5.7% | -5.9% |
| **Total** | **$109.417B** | | **+16.4%** |

([SEC 8-K, Q3 FY2026](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm))

The model is simple: sell a device at a fat margin, then collect a software-like, recurring cut
from that customer for the next five to ten years.

## 2. The moat — **wide**

A "moat" is a lasting advantage that keeps competitors from taking your customers. Apple has
four, stacked on top of each other:

1. **Switching costs.** Your photos, messages, purchases, Watch, AirPods and family sharing all
   live inside the ecosystem. Leaving is painful, so people don't.
2. **Brand and pricing power.** Company gross margin was **50.1% in Q3 FY2026** and **48.7% on a
   trailing-twelve-month basis** — for a business that is still about 74% hardware by revenue,
   that is extraordinary (TTM Products revenue $346.3B of $466.8B = 74%). Only a brand with real
   pricing power earns that.
3. **Installed-base network effect.** The active-device base hit an all-time high again this
   quarter (per CFO Kevan Parekh), and every extra device makes Services more valuable.
4. **Capital efficiency.** Apple produced **~$136.7B of free cash flow over the last twelve
   months on only ~$10.0B of capital spending**. It gets its AI compute mostly through partners
   (Google's Gemini now powers the revamped Siri) rather than spending tens of billions on its
   own data centres, unlike its mega-cap peers.

I am rating the moat **wide** and I am more confident in that rating than I was three months ago:
the "China is collapsing / Apple can't grow" narrative that hung over the stock in 2024–25 has
been decisively broken — Greater China revenue grew **+22.4%** in Q3 FY2026.

## 3. The key numbers (all from SEC filings)

Trailing twelve months = Q4 FY2025 + the first nine months of FY2026.

| What | Number | Where it comes from |
|---|---|---|
| Revenue (TTM) | **$466.823B** | $102.466B ([Q4 FY25 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019325000077/a8-kex991q4202509272025.htm)) + $364.357B ([Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm)) |
| Revenue growth, latest 9 months | **+16.2%** ($364.357B vs $313.695B) | [Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm) |
| Revenue growth, 3-year CAGR | **~6.8%** (FY2023 $383.285B → TTM $466.823B) | [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax.json) |
| Gross margin (TTM) | **48.7%** | derived from the two 8-Ks above |
| Diluted EPS (TTM) | **$8.73** ($1.85 + $6.88) | [Q4 FY25 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019325000077/a8-kex991q4202509272025.htm), [Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm) |
| Free cash flow (TTM) | **~$136.7B** (OCF $146.72B − capex $10.04B) | [Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm) |
| FCF per diluted share (TTM) | **$9.29** | $136.683B ÷ 14,714.676M shares |
| Balance sheet | **Net CASH ~$62.2B** ($146.517B cash + securities vs $84.3B debt) | [Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm) |
| Net-debt / EBITDA | **negative — there is no net debt** | as above |
| ROIC | **~67%** (NOPAT ~$127.6B ÷ invested capital ~$191.8B) | operating income $154.83B, 17.6% effective tax rate, equity $107.5B + debt $84.3B |
| Buybacks | **$62.094B in 9M FY2026**; $138.0B of authorization left | [Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000018/a8-kex991q3202606272026.htm), [10-Q](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm) |

**Plain-English read:** this is one of the best businesses on earth. It earns roughly 67 cents of
after-tax operating profit per dollar of capital invested, generates more free cash in a year
than most countries' budgets, owes nobody anything on net, and is buying back ~2% of itself
annually. Growth, which was flat for three years, has re-accelerated to 16%.

## 4. Fair value — and why the price is a problem

I used two methods and blended them with `code/valuation.py` so the arithmetic is checkable.

**Method 1 — Price/Earnings.** TTM diluted EPS **$8.73**, multiplied by 24 / 28 / 33.
The base of 28x is set deliberately at Apple's own **10-year median P/E of ~27.25x**
([GuruFocus](https://www.gurufocus.com/term/pettm/AAPL)). The 33x high case allows for the fact
that growth has re-accelerated; the 24x low case reflects a world where the Fed has just hiked to
3.75–4.00% and long-duration assets de-rate.

→ **$209.52 / $244.44 / $288.09**

**Method 2 — Free-cash-flow yield.** TTM FCF per share **$9.29**, at required yields of
5.0% / 4.2% / 3.5%. With cash yielding roughly 4%, demanding a 3.5–5.0% cash return from a stock
is the honest hurdle today.

→ **$185.80 / $221.19 / $265.43**

### Blended fair value band

| | Low | Base | High |
|---|---|---|---|
| Fair value | **$197.66** | **$232.82** | **$276.76** |

**Price today: $332.55. That is ~43% ABOVE our base fair value, and ~20% above the top of the
band.** Margin of safety = **−42.8%** — i.e. there is none; there is a negative cushion.

At $332.55 you are paying **38.1x trailing earnings** for a **2.79% free-cash-flow yield**, in a
market where a Treasury bill pays roughly 4% with no risk at all.

### The bull's rebuttal, stated fairly
If you believe the 16% growth rate persists and give Apple 35x on a forward FY2027 EPS somewhere
near $10, you get roughly $350 and today's price looks fine. That is a coherent view. It is also
a view that requires *both* a peak multiple *and* the supercycle to keep running. I am not
willing to underwrite both at once — see the next section for why.

## 5. The risks — written as hard as the bull case

1. **Valuation is the whole problem.** 38.1x TTM earnings against a 10-year median of 27.25x.
   Even our optimistic case is 17% below the market price.
2. **The earnings themselves are flattered.** Q3 FY2026's 50.1% gross margin **included about
   2 percentage points — and $0.11 of EPS — from one-off tariff refunds** after the February 2026
   Supreme Court ruling. Paying a peak multiple for peak, partly one-off earnings is exactly how
   permanent capital loss happens.
3. **Growth is already guided to slow.** For Q4 FY2026 management guided **revenue +9–11%** (down
   from 16%) and **gross margin 47–48%**, with a ~2.5 percentage-point FX headwind
   ([earnings call, 2026-07-30](https://www.macrumors.com/2026/07/30/apple-3q-2026-earnings/)).
4. **Costs and supply are tightening.** The Q3 FY2026 10-Q warns of "supply constraints and
   increasing costs for components" and expects those trends "to intensify" — advanced-node
   (2nm/3nm) capacity and rising memory prices.
5. **Regulators are aiming at the most profitable revenue Apple has.**
   - EU DMA: a €500M fine already levied and under appeal, plus a separate Article 6(4)
     investigation carrying exposure of **up to 10% of worldwide net sales**.
   - Epic: the Ninth Circuit's December 2025 injunction bars Apple from charging *any* commission
     on purchases made outside an app; the Supreme Court granted review of the contempt standard
     on 2026-06-30.
   - DOJ's March 2024 monopolization suit is still live.
   - Remedies in the Google search case could cut Apple's search-licensing revenue, which is
     close to 100% margin.
   ([10-Q](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm))
6. **One product is half the company,** and the current growth is substantially an upgrade
   supercycle. Supercycles pull demand forward and create ugly comparisons the year after.
7. **Apple rents its AI rather than owning it.** The new Siri runs on Google's Gemini models.
   That solved the near-term product gap, but it means the most important platform technology of
   the decade is licensed — and it deepens a commercial tie that regulators are attacking.
8. **China is ~17% of revenue and a large share of manufacturing** — a standing geopolitical and
   tariff exposure, even after the tariff refunds.

## 6. Trend check (Alpaca only)

Price **$332.55** is above its **50-day average $319.65** and well above its **200-day average
$286.03**; the 52-week close range is **$245.30–$340.01**. The stock is in a strong uptrend near
its highs. That is momentum, not value — and it is precisely why we are not buying.

## 7. Sell triggers — the exact rules

If we ever own it, these are the rules that force a review or a sale. They are written now, in
calm conditions, so we follow them later.

1. Company gross margin falls **below 44%** for two consecutive quarters (currently 48.7% TTM).
2. Total revenue **shrinks year-over-year for two consecutive fiscal years**.
3. **Services revenue declines year-over-year for two consecutive quarters.**
4. **iPhone revenue declines year-over-year for three consecutive quarters.**
5. The ~$62.2B net cash position turns into **net debt above 1.0x EBITDA**.
6. **TTM free cash flow falls below $90B** (a ~35% fall from $136.7B).
7. A **final, non-appealable** ruling that strips the App Store commission on a material share of
   transactions, or ends the Google search-licensing payments, with no offsetting replacement.
8. **Annual buybacks fall below $40B** while the balance sheet is still net cash — a signal
   management no longer thinks the shares are worth retiring.
9. Any serious **accounting red flag, restatement, or auditor change**.

**Entry discipline (not a sell rule):** do not initiate or add above **$233** (base fair value).
A first tranche is only justified **below ~$210**, roughly 10% under base.

## 8. What would make me buy

- A pullback into the **$200–$233** zone. That needs a ~30–40% decline — historically that has
  required a broad market de-rating or a real growth stumble, both of which are possible with the
  Fed hiking into 3.4% inflation.
- **Q4 FY2026 results (late October 2026)** are the key near-term test: do the guided 9–11%
  growth and 47–48% gross margin hold once the tariff refunds stop flattering the numbers?

## 9. Why conviction is 3, not 4 or 5

The *business* deserves a 4 or 5 — the moat got wider, growth re-accelerated, the balance sheet
is a fortress, and the data is entirely filing-backed. But conviction here means "would we
happily own a lot of this, for years, at this price," and the answer is no: we would be paying
43% above our own estimate of what it is worth, for earnings that contain a one-off tariff
benefit, into guided deceleration, with the Fed tightening. **Quality says 4. Price says 2.
Net: 3, and a clear "watch, do not buy."**

---
*Every figure above is sourced. Nothing is estimated except where explicitly labelled as our own
arithmetic (the fair-value band, TTM roll-ups, and ROIC), which is computed from the cited filing
figures using `code/valuation.py`. Prices come only from our Alpaca feed.*
