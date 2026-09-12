# Microsoft (MSFT) — Research Thesis

**Thesis ID:** MSFT-2026Q4 · **As of:** FY2026 (year ended 2026-06-30) · **Retrieved:** 2026-09-12 · **Refresh due:** 2026-12-12
**Conviction:** 4 / 5 · **Moat:** Wide · **Data quality:** filing-backed
**Price (Alpaca, 2026-09-11 close):** $495.58 · **Fair value band:** $370 – $426 – $491 · **Margin of safety:** −16.3% (expensive)

---

## What changed since the June 2026 thesis

The June thesis was written on FY2025 numbers. Microsoft has since reported its **full FY2026 year** (ended 30 June 2026, announced 29 July 2026) and made a **major reporting-structure announcement** on 2 September 2026. Three things matter:

1. **Growth got better.** Revenue grew 17.8% in FY2026, faster than FY2025's 15%. Azure passed **$100 billion of annual revenue for the first time**.
2. **Cash generation got worse.** Free cash flow actually *fell* — from $71.6B to $67.0B — even though net income jumped 31%. The reason is capital spending: $115.9B in one year.
3. **The accounting is getting friendlier to itself.** From FY2027 Microsoft is stretching datacenter useful lives from 15 to 25 years and shifting leases from finance to operating. Both make reported profit look better. This is legal and disclosed, but it is the kind of thing we write down and watch.

The stock rose ~26% (from $393.54 to $495.58) while our estimate of what the business is worth rose far less. **It is now above the top of our fair-value range.**

---

## What the company does, in plain words

Microsoft sells the software and computing that businesses run on. Three ways it earns money in FY2026:

| Segment | FY2026 revenue | What it is |
|---|---|---|
| Productivity & Business Processes | $140.0B | Microsoft 365/Office subscriptions, Teams, LinkedIn, Dynamics |
| Intelligent Cloud | $137.8B | Azure cloud, server software, GitHub |
| More Personal Computing | $54.1B | Windows, Xbox, Surface, Bing ads |

Most of that is **recurring subscription money**, which is why it is predictable.

**From FY2027 this changes.** Microsoft is collapsing to two segments: **Agents and Infra** ($268.1B restated FY2026) and **Devices and Consumer** ($63.7B restated FY2026). Helpfully, Microsoft will for the first time **report Azure revenue in actual dollars** instead of only a growth percentage.

### Why the moat is wide
A "moat" is a lasting advantage that keeps competitors out. Microsoft's is unusually strong:
- **Switching costs.** A company that runs its email, files, identity logins, and databases on Microsoft cannot leave without a multi-year, multi-million-dollar migration.
- **Network effects.** Teams and LinkedIn get more useful as more people use them.
- **Scale.** Very few companies on earth can spend $116B a year building datacenters.
- **Distribution for AI.** Copilot passed **30 million paid seats** — Microsoft can sell AI to a customer base it already owns.

---

## The key numbers (all cited)

| Measure | FY2026 | Comment |
|---|---|---|
| Revenue | **$331.839B**, +17.8% | 3-yr CAGR 16.1% from FY2023's $211.9B ([8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm)) |
| Gross margin | **67.9%** ($225.465B / $331.839B) | Down ~0.9pp from 68.8%; AI infrastructure is lower-margin |
| Operating income | **$155.237B** (46.8% margin) | +21% |
| Net income | **$133.749B** | Includes **$4.963B of one-off OpenAI investment gains** |
| Diluted EPS | **$17.95 GAAP / $17.28 non-GAAP** | The $0.67 gap is the OpenAI gain |
| Operating cash flow | **$182.935B** | Very strong |
| Capex | **$115.948B** | Up from $64.6B in FY2025 |
| **Free cash flow** | **$66.987B** | **DOWN from $71.6B in FY2025** |
| FCF conversion | **50.1%** of net income | Was 70.3% in FY2025 |
| ROIC | **~26.5%** (ending) / ~30.9% (average) | Was ~36% in FY2025 |
| Net debt / EBITDA | **0.16x** incl. finance leases | Still very safe |

**Sources:** [Microsoft FY26 Q4 press release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) · [FY2026 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm) · [8-K Exhibit 99.1 financial statements](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm) · [SEC XBRL balance-sheet data](https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/FinanceLeaseLiability.json) · cross-checked against [StockAnalysis.com](https://stockanalysis.com/stocks/MSFT/financials/)

### The balance sheet changed character
Microsoft used to be straightforwardly **net cash**. It still is if you only count bonds: $76.8B of cash and short-term investments against $40.3B of debt = **$36.5B net cash**. But **finance lease obligations jumped from $46.2B to $66.6B in a single year** — these are datacenter commitments that behave like debt. Counting them, Microsoft has roughly **$30B of net debt**, or 0.16x EBITDA. Still very safe; just no longer "net cash."

---

## How we got the fair value

We used the same two methods as June, run through `code/valuation.py` so the arithmetic is checked:

1. **Price-to-earnings.** 28x / 32x / 36x applied to **non-GAAP EPS of $17.28**. We use non-GAAP here because GAAP EPS contains $0.67 of non-cash OpenAI mark-to-market gains that may reverse. We deliberately kept the *same multiples as June* so any change in fair value comes from the business, not from us moving the goalposts. → **$483.84 / $552.96 / $622.08**
2. **Free-cash-flow yield.** 3.5% / 3.0% / 2.5% applied to **FCF per share of $8.99** ($66.987B ÷ 7,453M diluted shares). → **$256.86 / $299.67 / $359.60**

**Blended (equal weight): low $370.35 · base $426.31 · high $490.84.**

**The two methods now disagree violently** — $553 versus $300 at the midpoint. That gap *is the thesis question*. If the $116B of capex is building assets that will throw off cash for a decade, the P/E method is right. If it is an arms race that never earns its cost of capital, the FCF method is right. We do not know yet, so we keep the wide band and stay humble.

At **$495.58**, the price sits **above the high end**. Margin of safety is **−16.3%**. In plain terms: we would be paying more than we think the business is worth.

---

## The risks — written as hard as the bull case

- **We would be overpaying today.** The single biggest risk is the price, not the company.
- **Capital intensity has exploded.** Capex: $44.5B → $64.6B → $115.9B over three years, with **Q1 FY2027 alone guided above $50B** and calendar-2026 investment expectations around **$175B** ([Directions on Microsoft, Q4 FY26 call](https://www.directionsonmicrosoft.com/microsoft-expect-capacity-constraints-capex-acceleration-to-continue/)). Free cash flow went *down* while profit went *up*. That is the warning sign.
- **Earnings-quality yellow flag.** Extending datacenter useful lives **from 15 to 25 years** lowers annual depreciation and raises reported profit — right as the depreciation wave from the AI build was about to hit. Moving leases from finance to operating also moves obligations off the debt line. Neither is wrongdoing; both make FY2027 numbers less conservative and less comparable.
- **Returns on capital are falling**, ~36% → ~26–31%. If AI demand plateaus, Microsoft owns an enormous depreciating asset base.
- **Leverage is creeping in through leases**, not bonds.
- **Comparability breaks in FY2027** with the segment change.
- **Azure must eventually slow** from a $100B+ base; AWS and Google Cloud compete hard.
- **Regulators** continue to look at cloud bundling and the OpenAI relationship.

---

## Sell triggers — the exact rules

We sell (or trim) if any of these happen. These are written now, in calm conditions, so we follow them later:

1. Total revenue declines year-over-year for **two consecutive fiscal years**.
2. **Azure revenue growth falls below 15%** for two consecutive quarters. *(Raised from the old 10% trigger, because from FY2027 Microsoft reports Azure in dollars, so we can measure it directly — and because 15% is the honest line for a business priced for AI leadership.)*
3. Company-wide **gross margin falls below 60%** for two consecutive quarters.
4. **Free cash flow declines year-over-year for two consecutive fiscal years**, OR **FCF/net-income conversion falls below 35%** for a full year. *(FY2026 was 50.1% — this trigger is now live and close.)*
5. **Net debt / EBITDA (including finance and operating leases) rises above 2.0x.**
6. **ROIC falls below 15%** on a sustained multi-year basis.
7. Management **further extends asset useful lives** or makes another depreciation/lease reclassification that materially boosts EPS without clear operational justification — treat as an earnings-quality red flag.
8. A serious **accounting restatement** or material governance red-flag event.

---

## What would make us buy

- A pullback into the **$370–$426** band, which would finally give us a margin of safety.
- The **first dollar-level Azure disclosure in late October 2026 (Q1 FY2027)** showing the AI spend is converting to profitable revenue.
- Capex growth normalising so free cash flow re-converges toward net income.

## Why conviction is 4, not 5
The business is genuinely world-class and the moat got *stronger* this year. But two things hold it back from a 5: the **unresolved question of whether $116B/year of capex earns its cost of capital**, and the **accounting changes that flatter earnings** just as that question becomes urgent. A 4 means: we want to own this — at a better price.

## Trend check (Alpaca only)
Last close **$495.58**, above its 50-day average ($453.68) and 200-day average ($431.24). 250-day range $352.42–$542.43. The trend is up; the valuation is not attractive.
