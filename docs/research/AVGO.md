# Broadcom Inc. (AVGO) — research thesis

**Written:** 2026-08-08 · **Period covered:** FY2026 Q2 (quarter ended 2026-05-03) · **Refresh due:** 2026-11-06
**Conviction: 4 / 5** — a wonderful business. **But the price is not sensible today.**
**Verdict: WATCH, do not buy at $427.57.** Our fair-value band is $257 – $321 – $396. The stock trades ~33% above the base.

---

## 1. What the company actually does

Broadcom sells two very different things and staples them together.

**(1) Semiconductor Solutions — $15,009M of the $22,187M of Q2 FY2026 revenue (68%)**
- **Custom AI accelerators ("XPUs").** Broadcom does not sell an off-the-shelf AI chip like NVIDIA. It sits down with a handful of gigantic customers (Google, Meta, and now OpenAI and Apple) and co-designs a chip specifically for that customer's models. Broadcom supplies the hard parts — the high-speed interconnect (SerDes), the packaging, the physical design — and the customer supplies the architecture.
- **AI networking.** The Ethernet switch chips (Tomahawk, Jericho) that wire tens of thousands of accelerators into one cluster. This is arguably the better business, because it earns money no matter whose accelerator wins.
- **Everything else:** broadband/set-top, wireless (it is a long-standing Apple supplier), storage, industrial.

**(2) Infrastructure Software — $7,178M of Q2 FY2026 revenue (32%)**
- **VMware**, bought in November 2023 for roughly $69B, repackaged into the "VMware Cloud Foundation" subscription bundle. This is the software that runs most large companies' private data centres.
- Plus **CA** mainframe software, **Symantec/Carbon Black** security, and **Brocade** storage networking.

**How the money is made:** Broadcom is *fabless* — TSMC actually manufactures the chips. So Broadcom spends almost nothing on factories: **$860M of capex on $75.5B of trailing revenue.** That is why 43 cents of every revenue dollar falls out as free cash flow. Software is sold on multi-year contracts. Chips are sold on multi-year design cycles.

---

## 2. The moat — **wide**

A "moat" is a lasting advantage that keeps competitors away. Broadcom has three real ones:

- **Switching costs on the silicon.** Once a hyperscaler designs a Broadcom XPU into a data-centre generation, they are committed for years. Re-doing that design with a rival means 18–24 months and a lot of risk. The OpenAI "Jalapeño" chip took nine months from design to tape-out — that only happens with deep, sticky co-engineering.
- **Switching costs on the software.** Migrating off VMware or off a CA mainframe product means re-platforming the operations of the whole company. Broadcom has raised VMware prices aggressively and customers have largely paid — that is what pricing power looks like.
- **Scale and IP in networking.** Broadcom's SerDes and switch silicon are the merchant standard. Being the only credible alternative to NVIDIA's proprietary networking is a structurally strong position.

**How the moat could crack:** custom ASIC work is winnable by Marvell, Alchip or MediaTek, and hyperscalers can bring designs in-house. NVIDIA is pushing NVLink/Spectrum hard against Broadcom's Ethernet. The moat is wide but it is not permanent.

---

## 3. The numbers (every one is cited)

Trailing twelve months = FY2025 full year − first half FY2025 + first half FY2026. Every component comes from a filing; the arithmetic was done in a script, not in my head.

| Measure | Value (TTM to 2026-05-03) | What it means |
|---|---|---|
| Revenue | **$75,465M** | up from $63,887M for FY2025 |
| Revenue growth | **+24.4% CAGR FY2022→FY2025**; **+47.9% YoY in Q2 FY2026** | growth is *accelerating*, not fading |
| Gross margin | **68.3%** | strong pricing power |
| Operating margin | **43.4%** | |
| Adjusted EBITDA margin | **68.0%** ($51,292M) | |
| GAAP diluted EPS | **$6.01** | the honest, all-costs-included number |
| Non-GAAP diluted EPS | **$8.13** | excludes ~$8.8B of stock comp and intangible amortisation |
| Free cash flow | **$32,762M (43.4% of revenue)** | real cash, and it is very large |
| FCF per share | **$6.72** | ($4.92 if you subtract stock comp — see the caveat below) |
| ROIC | **~22.4%** | profit per dollar invested — comfortably above the 10–15% "good" bar, *and this charges the full $97.8B of acquisition goodwill against capital* |
| Net debt / EBITDA | **0.88x** ($45,279M net debt) | low and falling fast, despite the $69B VMware deal |
| Capex | **$860M** | fabless = capital-light |

**Segments (first half FY2026):** Semiconductor Solutions $27,524M revenue / $16,784M operating income; Infrastructure Software $13,974M revenue / $5,647M operating income (a 40.4% segment margin).

**The AI line specifically:** Q1 FY2026 AI semiconductor revenue **$8.4B (+106% YoY)** → Q2 FY2026 **$10.8B (+143% YoY)** → Q3 FY2026 **guided to $16.0B (+over 200% YoY)** on total revenue guided to ~$29.4B.

**Price and trend (from our own Alpaca feed, not the web):** last close **$427.57** (2026-08-07); 50-day average $395.01; 200-day average $367.57. The stock is above both averages — an uptrend. 250-session range $289.60–$481.91; six-month return +28.6%.

Sources: [Q2 FY2026 8-K press release](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000051/avgo-05032026x8kxex99.htm) · [Q2 FY2026 10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm) · [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm) · [FY2025 Q4 8-K press release](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm) · [Q1 FY2026 8-K press release](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm) · [SEC XBRL company facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0001730168.json)

---

## 4. Fair value — and why we think it is expensive

Fair value = a sensible estimate of what the business is worth. Margin of safety = how far the price sits below it.

We ran `code/valuation.py` **twice with identical multiples**, changing only the earnings anchor, so nobody can accuse us of tuning the multiples to reach a convenient answer.

**Multiples used (both runs):** P/E of **28 / 35 / 42x**, and FCF target yields of **3.5% / 2.8% / 2.2%**.
*Why:* 28x is what a wide-moat, 68%-EBITDA-margin business growing mid-teens deserves. 35x (base) credits durable AI custom-silicon growth. 42x assumes the OpenAI and Apple ramps land as advertised. These are already generous for a semiconductor-led company.

| Anchor | P/E band | FCF-yield band | **Blended fair value** |
|---|---|---|---|
| **A. Trailing twelve months** (EPS $8.13, FCF/sh $6.72) — the conservative check | $228 / $285 / $341 | $192 / $240 / $305 | **$210 / $262 / $323** |
| **B. Q2 FY2026 actuals annualised** (EPS $9.76, FCF/sh $8.42) — *our headline* | $273 / $342 / $410 | $241 / $301 / $383 | **$257 / $321 / $396** |

**We use band B ($257 low / $321 base / $396 high)** because Q2 is the most recent hard, filed quarter and better reflects the current run-rate.

**At $427.57 the margin of safety is −33%.** The stock sits *above the high end* of even the more generous band. In plain terms: on today's price you pay **71x trailing GAAP earnings, 53x non-GAAP earnings and 64x free cash flow.** That is a price that only works if the AI ramp continues at close to the guided pace for several more years.

**An important honesty caveat.** Both free cash flow and non-GAAP EPS add back **$8,785M of stock-based compensation** (about $1.80 per share). Diluted share count has risen from 4,778M (FY2024) to 4,876M (Q2 FY2026) despite $8.45B of buybacks in the first half. FCF per share net of stock comp is only **$4.92**, which would make the stock look considerably more expensive still.

**What we did *not* do:** we did not build a forward EPS forecast. Broadcom guides revenue and EBITDA margin for Q3 but not EPS, and inventing a forward number would be exactly the kind of guess this process forbids.

---

## 5. The bull case, honestly stated

1. AI semiconductor revenue is compounding at a rate very few large businesses ever achieve: $8.4B → $10.8B → guided $16.0B over three quarters.
2. Two enormous named programmes are still ahead of the numbers: the **OpenAI collaboration for 10 gigawatts** of OpenAI-designed accelerators, deploying from H2 2026 to end-2029, and a new **Apple custom-ASIC agreement running through 2031** (disclosed in an 8-K on 2026-07-06).
3. AI networking earns money regardless of which accelerator architecture wins — a genuine hedge inside the AI trade.
4. The economics are exceptional and verifiable: 68% gross margin, 43% operating margin, 22% ROIC *after* charging goodwill.
5. Almost no capital required: $860M capex on $75B revenue.
6. The balance sheet has been repaired remarkably fast — 0.88x net debt/EBITDA only ~2.5 years after a $69B acquisition — while still paying $6.2B of dividends and buying back $8.5B of stock in the first half.

## 6. The risks, stated just as hard

1. **Valuation is the biggest risk.** 33% above our base fair value. We would be paying in full, today, for growth that has not happened yet.
2. **Customer concentration is severe.** The FY2025 10-K says the **top five end customers were ~40% of net revenue**, and 48% of revenue moved through distributors. Losing one hyperscaler AI programme would be material.
3. **One end market now dominates.** AI semiconductors were $10.8B of $22.2B total Q2 revenue — roughly **half the company**, versus ~20% a year earlier. Semiconductors are historically cyclical, and Broadcom has never been this concentrated on a single cycle.
4. **The software leg is limping.** Infrastructure Software grew only **9% YoY** in Q2 FY2026. The market reacted badly to the 3 June 2026 print on soft software sales. Aggressive VMware repricing has created customer resentment and regulatory attention in Europe.
5. **Debt and interest.** $64,907M total debt; $1,577M of interest expense in the first half alone.
6. **GAAP is a lot worse than the headline.** $8.8B of annual stock comp and $3.9B of half-year intangible amortisation. GAAP EPS $6.01 vs non-GAAP $8.13.
7. **A very low tax rate (9.1%)** that could normalise upward.
8. **Goodwill is $97,801M — 55% of total assets ($179,158M).** An AI demand shock or a VMware stumble could produce a large impairment, which would also be an admission that the acquisition price was wrong.
9. **Competition:** Marvell, Alchip, MediaTek in custom ASICs; NVIDIA's NVLink/Spectrum against Broadcom's Ethernet; and hyperscalers insourcing design.

## 7. What we deliberately do NOT claim

- Full-year FY2025 AI revenue is not a line item in the 10-K or the press release (management gave it on the call), so we cite only the quarterly AI figures that appear in filed 8-K exhibits.
- The widely quoted **"$73B AI backlog"** comes from earnings-call commentary, not a filed document we could verify. It is **excluded** from this thesis.
- Broadcom does not break out AI revenue by customer, so we cannot independently size the OpenAI or Apple programmes.

---

## 8. Sell triggers — the rules we follow, written in calm times

If any of these happen, the reason to own Broadcom has broken and the portfolio manager should act:

1. **AI semiconductor revenue declines year-over-year in any two consecutive quarters.**
2. **Total revenue declines year-over-year for two consecutive quarters.**
3. **GAAP gross margin falls below 60% for two consecutive quarters** (68.3% today) — pricing power eroding.
4. **Adjusted EBITDA margin falls below 55% for two consecutive quarters** (68.0% today).
5. **Net-debt-to-EBITDA rises above 3.0x** (0.88x today), including via a debt-funded acquisition.
6. **Free cash flow falls below 25% of revenue for a full fiscal year** (43.4% today), or turns negative in any quarter.
7. **ROIC falls below 12% on a trailing basis** (22.4% today).
8. **Infrastructure Software revenue declines year-over-year for two consecutive quarters** — the VMware installed base breaking.
9. **Top-five end-customer concentration disclosed above 55% of net revenue** (40% in FY2025), or a named hyperscaler publicly cancels or insources a Broadcom XPU programme.
10. **A material goodwill impairment on VMware**, or any restatement, disputed auditor change, or SEC enforcement action.
11. **Diluted share count rises more than 3% year-over-year while buybacks are suspended** — dilution with no offset.

## 9. What we are waiting for

- **Q3 FY2026 results, expected early September 2026.** Guidance is ~$29.4B revenue (+84%) and $16.0B AI revenue (+over 200%). A beat and a raised FY2027 outlook confirms the thesis; a miss on either is a serious warning.
- **First revenue from the OpenAI 10-gigawatt programme**, which is targeted to start deploying in the second half of 2026 — it should start appearing in the numbers now.
- **A pullback toward $396 (our high) or $321 (our base).** That is the condition under which we would begin buying, slowly. Missing a buy costs nothing; overpaying costs money.

---

*Data quality: filing-backed. All fundamentals are from Broadcom's SEC filings (10-K, 10-Q, 8-K exhibits) and the SEC XBRL API. Price and trend are from our own Alpaca feed. Arithmetic was performed by `code/valuation.py` and a checked script, not estimated. Machine-readable thesis: `state/theses/AVGO.json` (validated with `python3 code/thesis.py --check AVGO` → PASS).*
