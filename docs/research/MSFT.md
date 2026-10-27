# Microsoft Corporation (MSFT) — research thesis

- **Thesis ID:** MSFT-2026Q4 · **As of:** FY2026 Q4 (fiscal year ended 30 June 2026)
- **Written:** 2026-09-17 · **Refreshed:** 2026-10-27 · **Next refresh due:** 2026-10-30 (right after
  Q1 FY2027 results, which come out after the close on **Wed 28 Oct 2026**)
- **Moat:** wide · **Conviction:** 3 / 5
- **Price used:** $533.78 (Alpaca) · **Our fair value:** $342.93 low / **$399.67 base** / $460.24 high
- **Margin of safety: −33.6% (NEGATIVE).** On our own framework, **Microsoft is overvalued today.**
  This is a wonderful business at a price we do not want to pay. **Do not buy at $533.78.**

### What changed in the 2026-10-27 refresh (and what did not)
- **No new financial period exists yet.** EDGAR shows no 10-Q or earnings 8-K since 2 Sep 2026; the
  latest filings are the proxy (DEF 14A) and annual report (ARS) on 21 Oct
  ([EDGAR filing index](https://data.sec.gov/submissions/CIK0000789019.json)). Q1 FY2027 results are
  due **after the close on 28 Oct 2026**
  ([Microsoft IR event page](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1)).
- We **re-checked** the FY2026 10-K figures (revenue, gross profit, operating income, net income,
  EPS, operating cash flow, capex, diluted shares) against SEC XBRL today. All match.
- The Fed's range is still **3.75–4.00%** (hiked 17 Sep 2026; no later 2026 decision listed on the
  [Fed's page](https://www.federalreserve.gov/monetarypolicy/openmarket.htm)).
- **Fair value is unchanged on purpose.** Our playbook says: don't move fair value unless a business
  number actually changed. None did. The only thing that changed is the **price, up about 7%**
  ($497.58 → $533.78), which makes the stock *more* expensive, not more valuable.
- Because results land in two days, this refresh is a holding pattern. **The real refresh is due by
  30 Oct**, using the Q1 FY2027 numbers.

---

## 1. What the company actually does

Microsoft sells software and computing power, mostly to businesses, mostly on subscription.
Three things pay the bills:

| Segment (FY2026) | Revenue | What it is |
|---|---|---|
| Productivity & Business Processes | **$140.0B** | Microsoft 365 (Word, Excel, Outlook), Teams, LinkedIn, Dynamics |
| Intelligent Cloud | **$137.8B** | Azure (renting computers over the internet), server software, GitHub |
| More Personal Computing | **$54.1B** | Windows, Xbox, Surface devices, Bing advertising |

Total FY2026 revenue was **$331.839B, up 18%** from $281.724B.
([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm),
[Q4 press release](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm))

**Heads-up on reporting:** from FY2027 Microsoft collapses these three into two — *Agents and Infra*
($268.1B of FY2026 revenue, restated) and *Devices and Consumer* ($63.7B). Azure and Windows will be
harder to track separately from now on.
([8-K, 2 Sep 2026](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526380280/d291965dex991.htm))

## 2. Why it has a moat (a lasting advantage)

A moat is anything that keeps competitors from taking your customers. Microsoft has several, stacked:

- **Switching costs.** A 50,000-person company cannot casually move off Microsoft 365, Windows and
  Azure. Retraining staff, rewriting software and migrating data costs more than the licences do.
- **Network effects.** Teams, LinkedIn and GitHub get more useful as more people use them.
- **Scale.** Very few companies on earth can afford to spend $116B a year building datacentres.
- **Contracted backlog.** The hardest number to argue with: **commercial remaining performance
  obligation rose 84% to $678B** — customers have already signed contracts for that much future
  revenue. That is over two years of total company revenue booked in advance.

Rating: **wide**.

## 3. The key numbers (all from the FY2026 10-K unless noted)

| Metric | FY2026 | Comment |
|---|---|---|
| Revenue | **$331.839B** (+17.8%) | 3-year CAGR **16.1%** from FY2023's $211.915B |
| Gross margin | **67.9%** ($225.465B) | Of every dollar of sales, 68c survives direct costs. Strong pricing power. |
| Operating margin | **46.8%** ($155.237B) | Exceptional for a company this size |
| Net income | **$133.749B** (+31% GAAP) | Non-GAAP $128.786B (+22%) — the GAAP figure is flattered |
| Diluted EPS | **$17.95 GAAP / $17.28 non-GAAP** | 7,453M diluted shares |
| ROIC (our estimate) | **~31%** | NOPAT $125.1B on avg. invested capital ~$405B. Derived by us, not reported. |
| Free cash flow | **$66.987B** | OCF $182.935B − capex $115.948B. **Down from $71.611B in FY2025.** |
| Net debt / EBITDA | **~0.15x** | Net *cash* of $36.5B excluding leases; $30.0B net debt once $66.6B of finance leases count |

Sources: [SEC XBRL company facts (FY2026 10-K)](https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json),
[Q4 FY26 press release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast).

### The one number that changed everything this year

**Free cash flow went DOWN while revenue went UP 18%.**

Free cash flow is the real cash left over after running and maintaining the business. It fell from
$71.6B to $67.0B because **cash capital spending nearly doubled, from $64.551B to $115.948B** — and
that understates it, because Microsoft also took on **$24.608B of new finance leases** (datacentres
rented under long contracts, which are debt in all but name) that never appear in the capex line.
Finance-lease liabilities have gone $27.1B → $46.2B → **$66.6B** in two years.

For scale: capex of $115.9B is **3.4x** the $34.3B depreciation charge Microsoft books today. That
means current profits do *not* yet carry the cost of the asset base being built. When they do, margins
fall unless the revenue arrives.

## 4. What it's worth, and how we got there

We used two methods and averaged them, with the arithmetic done by `code/valuation.py` (not by hand):

**Method 1 — Price/earnings.** 26x / 30x / 34x on FY2026 non-GAAP EPS of $17.28 → **$449 / $518 / $588.**
30x is roughly where a wide-moat business growing 18% with 47% operating margins has historically
traded. We cut every multiple by one turn versus our June 2026 thesis (28/32/36x) because the Fed has
since hiked to 3.75–4.00% — when safe cash pays more, growth is worth less.

**Method 2 — Free cash flow yield.** Target yields of 3.8% / 3.2% / 2.7% on FCF per share of $8.99
($66.987B ÷ 7,453M shares) → **$237 / $281 / $333.** Again ~0.3pp stricter than June, for the same
rate reason.

**Blended band: $342.93 low / $399.67 base / $460.24 high.**
At $533.78 the margin of safety is **−33.6%** — we would be paying about a third *more* than we
think it's worth. To reach our 12% minimum cushion on the base value, the price would need to be
about **$351.71 or lower** (about 34% below today).

### Being honest: the two methods disagree, badly

They should not be papered over.

- On **earnings**, MSFT trades at 29.7x trailing GAAP / 30.9x non-GAAP — a little above our 30x
  base. A P/E-only view says $449–$588 (base $518), i.e. roughly *fair* (−3% margin of safety).
- On **cash**, the free-cash-flow yield at $533.78 is **1.68%**. The Fed pays 3.75–4.00% on cash.
  You are accepting less cash yield from Microsoft than from a Treasury bill, and taking equity risk
  to get it.

Which is right depends entirely on a question nobody can answer yet: **does $116B a year of AI capex
earn a good return?** If yes, today's depressed FCF is temporary and the P/E view wins. If no, the
cash-flow view wins and the stock has a long way to fall. Because we genuinely do not know, we keep
both methods in and accept a wide, humble band — and a band whose top end is still below today's price.

**Trend check (Alpaca only, 2026-10-27):** last close $532.71 (quote $532.61 / $532.87), 50-day
average $510.22, 200-day average $437.03. The price is above both — a strong uptrend, ~22% above the
200-day line and close to its 250-day high. The 250-day closing range is $352.42–$543.51, so a
pullback to our band is not fantasy; it happened within the last year.

## 5. The bull case

1. **$678B of contracted future revenue, up 84%.** Customers are committing years ahead.
2. **Azure passed $100B of annual revenue and still grew 43%** in Q4 — with guidance of **44–45%
   constant currency for Q1 FY2027**. Accelerating at that scale is rare.
3. **Elite economics:** 67.9% gross margin, 46.8% operating margin, ~31% ROIC, net cash ex-leases.
4. **AI is earning revenue, not just costing money:** Microsoft 365 Copilot passed **30 million paid
   seats**, sold into a base Microsoft already owns.
5. **Balanced:** Productivity ($140.0B) and Intelligent Cloud ($137.8B) are now similar in size, so
   no single product carries the company.

## 6. The risks (written as hard as the bull case)

1. **The price.** At $533.78 we are 34% above our base value and 16% above the top of our band. The
   gap has grown since September with no new business facts. This is the single biggest risk.
2. **Earnings in two days.** Results land after the close on 28 Oct. With the stock near its high,
   a miss on Azure (guided 44–45%) or capex well above $50B could move it hard either way.
3. **Free cash flow is shrinking**, and Q1 FY2027 capex alone is guided at **over $50B**. FY2027 FCF
   could fall again.
4. **The AI capex bet is unproven and gigantic.** Capex at 3.4x depreciation means future depreciation
   will bite hard. If demand disappoints, both margins and ROIC fall a long way.
5. **Debt-like obligations are building quietly.** $66.6B of finance leases do not appear in the
   headline "net cash" figure investors quote.
6. **Earnings quality.** GAAP net income of $133.7B included a **$3.2B one-off gain on the Anthropic
   stake**. Marking up a private AI stake is not repeatable operating profit. Non-GAAP was $128.8B.
7. **Rates and macro.** Fed at 3.75–4.00%, inflation 3.4%. Higher rates compress what investors pay
   for long-duration growth, and an IT spending slowdown hits cloud consumption directly.
8. **Regulation.** Antitrust scrutiny in the US and EU over cloud bundling, the OpenAI relationship,
   and AI market power.
9. **Less transparency** after the FY2027 segment change.

## 7. Sell triggers — the exact rules

If any of these happen, the reason we own Microsoft has broken and we sell (or trim):

1. Azure constant-currency growth **below 20% for two consecutive quarters** (guided 44–45% today).
2. Total company revenue **declines year over year for two consecutive quarters**.
3. Gross margin **below 60% for two consecutive quarters** (67.9% today).
4. Operating margin **below 38% for two consecutive quarters** (46.8% today) — the sign that AI
   depreciation is overwhelming the P&L.
5. Free cash flow **declines year over year for a third straight fiscal year**, or turns negative for
   a full year. *FY2025 → FY2026 is already decline number one.*
6. Net-debt-to-EBITDA **including finance leases rises above 1.5x** (0.15x today), or finance-lease
   liabilities **exceed $150B**.
7. Estimated **ROIC below 15%** on a sustained multi-year basis (~31% today).
8. **Commercial RPO declines year over year.**
9. Any **accounting restatement, SEC enforcement action or governance red flag** — in particular any
   restatement of datacentre asset useful lives, or of revenue recognised on AI-related related-party
   deals.

## 8. What would make us buy

- A pullback to **$400 or below** (our base), ideally toward **$343** (our low), for a real cushion.
- Capex growth normalising toward depreciation, which would make reported free cash flow jump and
  settle the earnings-vs-cash argument in the bulls' favour.
- Evidence in the Q1 FY2027 report (28 Oct 2026) that cloud operating margin holds up *while* the
  new depreciation starts hitting.

## 9. Conviction: 3 / 5 — and why it fell from 4

The **business** deserves a 4 or 5: wide moat, ~31% ROIC, 68% gross margin, 18% growth, net cash.
The **thesis at this price** does not. Three things pulled it down since the June refresh:

- the margin of safety went from −4% to −24.5% (Sep) to **−33.6%** (27 Oct, price-driven only);
- free cash flow **fell** for the first time in this thesis's life, and the capex driving it doubled;
- finance-lease obligations grew another **$20B**, and the Fed **hiked**, raising the bar for every
  long-duration asset.

A 3 means: excellent company, **keep it on the bench, wait for the price.** A missed buy costs
nothing; an overpriced buy costs money.

---

### Data quality
**filing-backed.** All financial-statement figures come from the FY2026 Form 10-K (filed 29 July 2026,
accession 0001193125-26-323660) via SEC EDGAR XBRL, the Q4 FY2026 8-K earnings release, and the
2 September 2026 8-K guidance update. Price and moving averages come only from our Alpaca feed.

**Numbers we derived rather than read off a filing** (inputs cited, arithmetic ours): ROIC ~31%,
EBITDA ~$199.6B, net-debt/EBITDA ~0.15x, free cash flow $66.987B, FCF per share $8.99, 3-year revenue
CAGR 16.1%.

**Verification status (2026-10-27):** fed funds 3.75–4.00% was checked against the Federal Reserve's
page. CPI 3.4% was passed in by an earlier morning cycle and remains **unverified**.

**Conviction stays at 3** (below our buy threshold of 4). Nothing about the business got worse, but
nothing got better either, and the key open question — whether AI capex earns its return — will get
fresh evidence on 28 Oct. We should not raise conviction the day before the data that could answer it.
