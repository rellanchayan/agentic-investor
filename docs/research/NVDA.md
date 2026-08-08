# NVIDIA Corporation (NVDA) — Research Thesis

- **Written:** 2026-08-08
- **Numbers as of:** NVIDIA fiscal Q1 2027, the quarter ended **2026-04-26** (filings), plus FY2026 (ended 2026-01-25)
- **Price used:** **$223.93** (Alpaca close, 2026-08-07)
- **Fair-value band:** **$151 – $198 – $253**
- **Margin of safety:** **−13.0%** (the stock is *above* our base fair value)
- **Conviction:** **3 / 5** — outstanding business, uncomfortable price, real structural risks
- **Verdict today:** **Watch, don't buy yet.** Great company; no cushion at $224.
- **Refresh due:** **2026-08-27** — Q2 FY2027 earnings land 2026-08-26 and will move every number here.

---

## 1. What the company actually does, in plain words

NVIDIA sells the computers that artificial intelligence runs on.

It designs the chips but doesn't build them — TSMC does the manufacturing. NVIDIA's job is
the design plus, increasingly, the whole machine: the GPU, the NVLink cables that stitch
GPUs together, the InfiniBand/Spectrum-X networking that stitches racks together, and the
software that makes it all usable. It sells these as complete "AI factory" racks.

Who buys? A very short list of very large customers: cloud providers, AI labs, specialist
"neocloud" GPU renters, some enterprises and governments, plus a much smaller business
selling graphics and workstation chips.

**How concentrated is "short list"?** In the quarter ended 2026-04-26, **three direct
customers were 21%, 17% and 16% of total revenue — 54% between them**
([10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)).
A year earlier the top two were 16% and 14%. Concentration is getting *worse*, not better.

Since Q1 FY2027 NVIDIA reports two platforms:

| Platform | Q1 FY2027 revenue | Growth y/y |
|---|---|---|
| Data Center (Hyperscale + ACIE) | $75.2B | +92% |
| Edge Computing | $6.4B | +29% |
| **Total** | **$81.6B** | **+85%** |

Source: [Q1 FY2027 press release (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm).

So: this is a Data Center company with a small graphics side-business attached.

---

## 2. The moat — why competitors have struggled to take it

**Rating: wide — with an asterisk.**

A "moat" is a durable advantage. NVIDIA has three real ones:

1. **CUDA.** For nearly twenty years NVIDIA has given away the software layer — libraries,
   compilers, frameworks — that makes GPUs programmable. Millions of developers learned on
   it; virtually every AI framework targets it first. Moving off CUDA is not a purchase
   decision, it's an engineering re-platforming measured in engineer-years. That is a
   **switching cost**, the stickiest kind of moat.
2. **Full-stack systems.** NVIDIA no longer competes chip-vs-chip. A rival must match the
   GPU *and* the interconnect *and* the networking *and* the software, all at once, at rack
   scale. Beating one piece isn't enough.
3. **Supply scale.** TSMC's advanced packaging (CoWoS) and high-bandwidth memory are the
   real bottlenecks in AI hardware. NVIDIA's volume gives it first call on both.

**The asterisk.** Unlike a consumer brand, this moat has to be *re-earned roughly every
twelve months* by staying at the technology frontier. And NVIDIA's biggest customers are
also its most motivated attackers — Google (TPU), Amazon (Trainium), Meta (MTIA) are all
funding in-house silicon precisely to escape this dependence, while AMD and open software
layers attack CUDA from below. We rate the moat wide, but with a shorter durability horizon
than we'd assign to, say, a payments network.

---

## 3. The numbers (every one linked to a filing)

### Growth — extraordinary, and still accelerating

| Fiscal year (ends late Jan) | Revenue | Growth |
|---|---|---|
| FY2023 | $26.974B | — |
| FY2024 | $60.922B | +126% |
| FY2025 | $130.497B | +114% |
| FY2026 | $215.938B | +65% |
| Q1 FY2027 (one quarter) | $81.615B | +85% y/y |
| Q2 FY2027 (company guidance) | $91.0B ±2% | — |

That's a **100.1% three-year compound growth rate** from FY2023 to FY2026.
Sources: [FY2026 press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm),
[SEC XBRL revenue history](https://data.sec.gov/api/xbrl/companyconcept/CIK0001045810/us-gaap/OperatingIncomeLoss.json),
[Q1 FY2027 press release](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm).

### Profitability — close to the best anywhere

- **Gross margin:** 71.1% for FY2026, **74.9%** in Q1 FY2027. (FY2026 was dragged down by
  the $4.5B H20 export write-off taken in Q1 FY2026, when gross margin fell to 60.5%.)
- **Operating margin FY2026:** 60.4% (operating income $130.387B on $215.938B revenue).
- **ROIC ~137%** (our arithmetic, from filed inputs): NOPAT = $130.387B operating income ×
  (1 − 15.1% effective tax) = $110.7B, over invested capital of roughly $81B. It is this
  high because the business is fabless — FY2026 capex was only **$6.042B, 2.8% of revenue**.
  Treat the exact percentage as an estimate; the *order of magnitude* is the point.

### Cash — real, and enormous

- FY2026 operating cash flow **$102.718B**, capex **$6.042B** → **free cash flow ~$96.7B**.
- Trailing twelve months to 2026-04-26: **~$119.1B FCF**, about **$4.88 per diluted share**
  (24.391B diluted shares).
- FCF converts at ~87% of core operating profit. Cash is much harder to fake than earnings.

### Balance sheet — a fortress

At 2026-04-26: total debt **$8.470B** against cash + marketable debt securities of
**$50.335B** → roughly **$41.9B net cash**, i.e. net-debt-to-EBITDA of about **−0.3x**.
The company bought back **$19.312B** of stock in the quarter and the board authorised
another **$80.0B** on 2026-05-18. The dividend was raised from $0.01 to $0.25 per quarter.

---

## 4. What we're worth-checking against: the fair-value band

We used `code/valuation.py` so the arithmetic isn't done by hand. Two methods, both on
**trailing twelve-month** numbers so they're anchored to things that have actually been
filed:

**Method 1 — Price-to-earnings.**
Trailing GAAP diluted EPS = **$6.53** (FY2026 $4.90 − Q1 FY2026 $0.76 + Q1 FY2027 $2.39,
all from filings). Multiples **25 / 33 / 42**.
*Why those?* A business growing 65–85% with 70%+ gross margins, >100% ROIC and net cash has
historically earned 30–45× earnings; but semiconductor demand is cyclical and 54% of revenue
sits with three customers, which justifies a 25× downside case.
→ **$163.25 / $215.49 / $274.26**

**Method 2 — Free-cash-flow yield.**
Trailing FCF per share **$4.88**, target yields **3.5% / 2.7% / 2.1%**.
→ **$139.43 / $180.74 / $232.38**

**Blended band: low $151.34 · base $198.12 · high $253.32.**
At $223.93 the margin of safety is **−13.0%** — we would be paying *above* fair value.

### Two honest caveats, pulling in opposite directions

**The trailing EPS is flattered.** Q1 FY2027's GAAP net income ($58.321B) was *higher than
its operating income* ($53.536B) because of **$16.0B of unrealized gains on equity
investments** ($13.4B public, $2.6B private). FY2026 similarly carried $11.063B of
non-operating income. Strip those out and core trailing EPS is closer to **$5.61**. That
argues the band above is, if anything, generous.

**The trailing EPS is also stale.** A company growing 85% year-over-year is not well
described by last year's earnings. Annualising the company's *own* Q2 FY2027 guidance —
$91.0B revenue × 74.9% gross margin − $8.5B operating expenses = ~$59.7B quarterly
operating income, plus ~$0.44B net interest, taxed at 17%, over ~24.3B shares — gives about
**$2.05 a quarter, ~$8.2 annualised**. At $223.93 that's **~27× forward earnings**, which is
not obviously expensive. Sell-side consensus for FY2027 is $9.00 EPS
([StockAnalysis, aggregator](https://stockanalysis.com/stocks/nvda/forecast/)).

We deliberately publish the **conservative trailing band** and treat the forward case as
*evidence of upside*, not as our base case. Paying up for peak-cycle earnings is exactly how
investors have historically lost money in semiconductors.

**Trend check (Alpaca, our own feed):** last close $223.93, 50-day average $206.06, 200-day
average $193.97, 250-day range $165.18–$235.78, ~6-month return +20.9%. The stock is in an
uptrend and near the top of its own range — momentum is with it, price is not.

---

## 5. The bull case

- CUDA is the deepest software moat in computing infrastructure; switching is measured in
  engineer-years.
- NVIDIA sells whole AI factories, so a competitor must beat the entire rack, not one chip.
- Economics near best-in-class anywhere: 74.9% gross margin, 60%+ operating margin,
  ROIC >100%, capex under 3% of sales.
- ~$41.9B net cash, $19.3B of buybacks in one quarter, $80B more authorised.
- Demand is still *accelerating*: +85% y/y, guided to $91B next quarter — and management
  said that guidance assumes **zero** China Data Center compute revenue. China is upside
  optionality, not an embedded assumption.
- ~$119B of trailing free cash flow. That's real money.

## 6. The risks — stated as hard as the bull case

1. **Customer concentration is severe and worsening.** Three customers = 54% of revenue.
   Losing one is a double-digit revenue event.
2. **Those customers are the competition.** Google, Amazon and Meta are all shipping their
   own accelerators specifically to reduce NVIDIA dependence.
3. **This is a capex cycle, not an annuity.** NVIDIA's revenue is a handful of companies'
   budget line. Semis have always overshot and then corrected hard.
4. **Quality of earnings is degrading.** GAAP net income now exceeds operating income
   because of mark-to-market gains on equity stakes. Those marks reverse.
5. **Circular financing.** Non-marketable securities jumped from $22.251B to $43.364B in one
   quarter ($18.582B of purchases); marketable equity holdings went $12.886B → $30.237B.
   NVIDIA is increasingly investing in the companies that buy its chips. If those companies
   can't fund themselves independently, the investment *and* the revenue vanish together.
6. **China is effectively closed.** The FY2026 10-K states NVIDIA was *"effectively
   foreclosed from competing in China's data center computing/compute market."* H200 licences
   granted from February 2026 had produced **zero** revenue as of the Q1 filing, carry a 25%
   US import tariff, and US officials have signalled an expectation of taking 15%+ of
   licensed China revenue. In August 2026 a US agency began reviewing Chinese firms' offshore
   access to NVIDIA chips via rented overseas compute
   ([Bloomberg, news — not a filing](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs)).
7. **Inventory is building.** Inventories rose $21.403B → $25.797B in one quarter, with
   $3.121B of accrued excess-inventory purchase obligations. The Q1 FY2026 $4.5B H20
   write-off is the template for what a demand or policy shock does here.
8. **No valuation cushion.** ~34× trailing earnings, ~46× trailing free cash flow, ~13%
   above our base fair value, ~15% above the 200-day average.
9. **Single-supplier dependence** on TSMC and a concentrated HBM supply base — geopolitical
   risk NVIDIA does not control.

---

## 7. Sell triggers — the rules we agree to *now*, in calm weather

If any of these fire, we sell (or trim where noted), regardless of how the story sounds:

1. **Data Center revenue falls year-over-year in two consecutive quarters.**
2. **Total revenue falls year-over-year in two consecutive quarters.**
3. **GAAP gross margin below 65% for two consecutive quarters.**
4. **Inventory + excess-purchase-obligation charges above $5B in any single quarter**, or
   inventories growing faster than revenue for three consecutive quarters.
5. **Trailing-twelve-month free cash flow below 50% of trailing operating income** for two
   consecutive quarters (earnings stop turning into cash).
6. **The ~$41.9B net cash position turns into net debt**, or net-debt-to-EBITDA exceeds 1.0×.
7. **Strategic equity investments exceed 30% of total assets** (they were 28.3% at
   2026-04-26: $43.364B + $30.237B of $259.474B), or the company discloses that
   vendor-financed customers materially drive revenue growth — the circular-revenue red flag.
8. **Top-three direct-customer share rises above 70% while revenue growth falls below 20%
   y/y**, or NVIDIA discloses the loss of a >10% customer.
9. **A major customer publicly commits the majority of a new cluster generation to
   non-NVIDIA silicon.**
10. **Any restatement, material control weakness, or disputed auditor change.**
11. **TRIM only:** price exceeds $253.32 (top of band) without a filing-evidenced increase
    in earnings power.

---

## 8. What we're watching next

- **2026-08-26 — Q2 FY2027 results.** Guidance is $91.0B. The *H2 guidance shape* matters
  more than the print: still accelerating, or first sign of a plateau?
- Rubin-generation ramp and whether the annual cadence holds against AMD and in-house ASICs.
- Any *revenue-producing* reopening of China under the H200 licence regime (currently zero).
- Execution of the $80B buyback at these price levels.
- **The buy trigger we actually want:** a market-wide AI de-rating or a hyperscaler capex cut
  that pulls the price toward **$151–$180**. That is where this becomes a genuinely
  attractive purchase rather than a full-price one.

---

## 9. Bottom line

NVIDIA is one of the highest-quality businesses we have looked at: a wide software moat,
75% gross margins, triple-digit ROIC, $119B of trailing free cash flow, and a net-cash
balance sheet. It is also a cyclical business whose fortunes rest on three customers who are
actively trying to replace it, whose reported earnings are increasingly inflated by paper
investment gains, and which is now funding its own customers.

At $223.93 we are being asked to pay ~13% above our base fair value for all of that.
**Quality: yes. Fair price: not yet.** Conviction 3/5 — a name to own, at a better price.

*Machine-readable version: `state/theses/NVDA.json` (validated: `python3 code/thesis.py --check NVDA` → PASS).*
