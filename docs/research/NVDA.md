# NVIDIA Corporation (NVDA) — Research Thesis

**As of:** FY2027-Q1 (quarter ended 2026-04-26) · **Written:** 2026-08-06 · **Refresh due:** 2026-09-04
**Price used:** $218.98 (Alpaca) · **Fair value band:** $142.96 / $183.83 / $233.97
**Margin of safety:** −19.1% (price is ABOVE our base fair value) · **Conviction:** 3 / 5
**Verdict: great business, wrong price. WATCH — do not buy here.**

---

## 1. What the company actually does

NVIDIA sells the computers that artificial intelligence runs on.

It designs the chips (GPUs) but owns no factories — TSMC and its partners do the manufacturing.
Increasingly NVIDIA does not even sell a chip; it sells a whole rack: GPUs, the NVLink and
InfiniBand/Spectrum-X networking that stitches thousands of them into one giant machine, and the
CUDA software that developers write against.

Who buys it: the giant cloud companies, AI labs, "neocloud" GPU landlords, big enterprises and
governments building AI capacity.

How concentrated is it? Very. In fiscal 2026 (ended 2026-01-25), Data Center was **$193.7B of
$215.9B** total revenue — roughly 90% of the company. Gaming was $16.0B, Professional
Visualization $3.2B, Automotive $2.3B.
([Q4/FY2026 press release, SEC](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm))

In the most recent quarter (Q1 FY2027, ended 2026-04-26): revenue **$81.615B, up 85% year over
year**; Data Center **$75.2B** (compute $60.4B, networking $14.8B). Management guided the current
quarter to **$91.0B ± 2%**.
([Q1 FY2027 press release, SEC](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm))

---

## 2. The moat — why competitors can't just copy it (rating: **wide**)

A "moat" is a lasting advantage. NVIDIA's is not the silicon by itself:

- **CUDA and the software stack.** Twenty years of libraries, kernels and frameworks are tuned for
  NVIDIA first. Moving a serious AI workload to another vendor means rewriting and re-validating
  it. That is a **high switching cost**.
- **Systems, not chips.** The networking (NVLink, InfiniBand, Spectrum-X) is what makes 50,000 GPUs
  behave like one machine. A rival selling only a chip is not competing on the same axis.
- **Scale and supply priority.** NVIDIA gets first call on leading-edge TSMC capacity and HBM memory.
- **Cadence.** An annual architecture refresh that rivals have not matched.

**Where the moat is genuinely thin:** the customers who account for most of the revenue are the
same companies designing their own alternatives (Google TPU, Amazon Trainium, Microsoft Maia).
That is an unusual and uncomfortable structure — your biggest buyers are also your most credible
future competitors.

---

## 3. The key numbers (all from SEC filings)

| Measure | Value | Period |
|---|---|---|
| Revenue growth (3-yr CAGR) | **100.0%** ($26.974B FY2023 → $215.938B FY2026) | FY2023–FY2026 |
| Latest quarter revenue | **$81.615B**, +85% y/y | Q1 FY2027 |
| Gross margin | **74.1% trailing 12m**; 71.1% FY2026; 74.9% in Q1 FY2027 | TTM to 2026-04-26 |
| ROIC | **~91%** (conservative measure) | TTM |
| Free cash flow | **~$119.1B** TTM (OCF $125.648B − capex $6.572B); **positive** | TTM |
| Net debt / EBITDA | **−0.27x (net cash of $44.0B)** | at 2026-04-26 |
| Diluted shares | 24,391 million | Q1 FY2027 |

Sources: [SEC XBRL company facts, CIK 1045810](https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json) ·
[FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) ·
[Q1 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)

**How ROIC was computed** (our own arithmetic, from filed numbers): TTM operating income $162.285B
× (1 − FY2026 effective tax rate of 15.1%) = NOPAT ~$137.8B. Invested capital = equity $195.474B +
debt $8.470B − cash $13.237B − available-for-sale debt securities $39.233B = $151.5B. 137.8 / 151.5
= **91%**. If we also strip out the ~$72.6B of non-operating equity stakes, ROIC is ~175%. Either
way: this business earns a spectacular return on the capital it employs.

**Balance sheet:** total debt is only $8.470B against $13.237B of cash and $39.233B of bonds. It is
a **net-cash** company. Debt is not a risk here.

**One thing to be careful about:** GAAP earnings in Q1 FY2027 were flattered by **$15.929B of
non-operating gains on equity securities** — investments, not chip sales. That is why GAAP EPS was
$2.39 but non-GAAP EPS was $1.87. We used the lower, cleaner figure for valuation.

---

## 4. Fair value — how we got the band

Run through `code/valuation.py` so the arithmetic is not hand-waved.

**Method 1 — P/E on trailing non-GAAP earnings.** TTM non-GAAP diluted EPS = $4.77 (FY2026) −
$0.78 (Q1 FY2026) + $1.87 (Q1 FY2027) = **$5.86**.

| Multiple | Why | Value |
|---|---|---|
| 25× (low) | An AI-digestion or share-loss year, where today's earnings turn out to be near a cycle peak | $146.50 |
| 33× (base) | A very high-return franchise still compounding, discounted for semiconductor cyclicality and customer concentration | $193.38 |
| 42× (high) | Growth stays close to the current trajectory | $246.12 |

**Method 2 — Free-cash-flow yield.** TTM FCF per share = $119.076B / 24,391M shares = **$4.88**.
At a 3.5% / 2.8% / 2.2% demanded yield → **$139.43 / $174.29 / $221.82**.

**Blended fair value: low $142.96 · base $183.83 · high $233.97.**

At $218.98 the margin of safety is **−19.1%**. We are being asked to pay about 37× trailing
non-GAAP earnings and a 2.2% free-cash-flow yield. That is inside the *high* end of our band, not
below the base. For a "quality at a fair price" investor, that is not a buy — it is a watch.

**Honest caveat in the other direction:** we valued NVDA on *trailing* numbers for a company
guiding to +85% growth next quarter. If fiscal 2027 lands anywhere near guidance, this band will
look far too conservative in hindsight. We accept that risk deliberately: our discipline is to buy
below a defensible band, not to underwrite a boom continuing.

**Trend check (Alpaca, 2026-08-06):** last close $219.37, 50-day average $205.84, 200-day average
$193.77, 250-day range $165.18–$235.78. The stock is above both averages — an uptrend, and near the
top of its year. Momentum is not a reason to buy; it is a reason to be patient.

---

## 5. The bull case

1. Wide moat from CUDA + networking + full-rack systems; developers are locked in.
2. Extraordinary economics: 74% gross margin, ~91% ROIC, ~$119B trailing free cash flow, net cash.
3. Growth is still accelerating (+85% y/y last quarter), with $91B guided for the current quarter.
4. Asset-light for its size: FY2026 capex was $6.042B against $102.718B of operating cash flow.
   NVIDIA does *not* consume the cash it earns — unlike its customers.
5. Huge capital returns: $41.1B in FY2026, ~$20.0B in Q1 FY2027 alone, $80B added to the buyback,
   dividend raised from $0.01 to $0.25 per quarter.

---

## 6. The risks — written as hard as the bull case

1. **Price.** ~19% above our base fair value. No cushion at all.
2. **Customer concentration is severe.** In Q1 FY2027 **three direct customers were 21%, 17% and
   16% of total revenue — about 54% combined**. A year earlier the top two were 16% and 14%, so
   concentration is getting *worse*, not better. The filing also notes one AI research and
   deployment company contributed a meaningful amount of revenue indirectly.
   ([10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm))
3. **Circular financing.** NVIDIA holds **$30.237B of marketable equity securities and $42.336B of
   non-marketable equity investments** (~$72.6B) largely in AI-ecosystem companies that are also
   its customers, and booked a $15.929B gain on them last quarter. If the AI funding cycle turns,
   those marks reverse *and* the demand they support fades. These two risks are correlated, not
   independent. This is the single thing most likely to make the reported numbers look worse than
   they seem.
4. **Peak-earnings risk.** This is a semiconductor company selling into a capex boom. Hyperscaler
   AI spending cannot compound at this rate forever. Paying 37× *peak* earnings is how people lose
   money in semis.
5. **Customers building their own chips.** TPU, Trainium, Maia, AMD Instinct — designed by the same
   companies that are 54% of revenue.
6. **Geopolitics.** China export restrictions removed a large market and can change again without
   notice. Essentially all supply depends on TSMC in Taiwan and a handful of HBM vendors.
7. **Working capital.** Inventory went from $10.080B (2025-01-26) to $25.797B (2026-04-26);
   receivables are $40.710B. Normal for a ramp — ugly if demand pauses.
8. **We already own it indirectly.** NVDA is a very large weight inside SPY, our benchmark. Buying
   it adds less diversification than it appears to.

---

## 7. Sell triggers — the exact rules

If we ever own this, we sell (or trim) when any of these is true:

1. Total revenue declines year over year for **two consecutive quarters**.
2. GAAP gross margin falls **below 60% for two consecutive quarters**.
3. Data Center revenue declines year over year in any quarter, or falls below 70% of total revenue
   because of lost share.
4. Free cash flow turns **negative for a full fiscal year**, or net debt / EBITDA rises **above 1.0x**.
5. Trailing-twelve-month ROIC falls **below 25%**.
6. Top-three direct customers rise **above 65%** of revenue, or any single customer **exceeds 30%**.
7. Inventory grows faster than revenue for two consecutive quarters, or an inventory writedown
   **above $5B** is taken.
8. A material accounting restatement, SEC enforcement action, or a formal finding on
   circular/round-trip revenue involving NVIDIA's equity-investee customers.
9. An export-control or supply shock removing **more than 20%** of forecast Data Center revenue for
   more than two quarters.

---

## 8. What we're waiting for

- **Q2 FY2027 results, expected late August 2026**, against the $91.0B ± 2% guide. A beat-and-raise
  extends the runway; a miss is the first real crack. (This is why `refresh_due` is 2026-09-04.)
- **A pullback toward $183 or below.** That is where a real margin of safety starts.
- **Evidence that inference — recurring production workloads — is now the majority of demand.**
  That would make revenue durable rather than project-driven and would justify a higher base multiple.
- **Customer concentration falling back below 40%.**

## 9. Why conviction is 3 and not 5

The business quality argues for 5. The price (−19% margin of safety), the 54% top-three customer
concentration, the $72.6B of equity stakes in its own customers, and the fact that we are late in a
capital-spending boom argue for less. A 3 means: *we would happily own this at the right price;
this is not that price.*

**Data quality: filing-backed.** Every number above comes from SEC EDGAR filings or NVIDIA's
SEC-furnished earnings releases, except the price and moving averages, which come from our own
Alpaca feed, and the ROIC / EBITDA / TTM figures, which are our own arithmetic on filed inputs
(shown above so it can be checked).
