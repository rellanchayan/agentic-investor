# Visa Inc. (V) — Research Thesis

*As of 2026-09-16 — fiscal data through Q3 FY2026 (quarter ended 2026-06-30). Visa's fiscal year ends Sept 30.*
*This replaces the 2026-Q2 thesis dated 2026-06-16.*

**Bottom line: still a wonderful business, still too expensive. Price $374.04 vs base fair value
$300.49 — a margin of safety of **-24.5%**. No buy at this price.**

---

## What the business does (plain English)

Visa runs the biggest electronic-payments network in the world (VisaNet). It is **not** a bank and
**not** a lender. Banks issue the Visa-branded cards; Visa just moves the messages that say "this
shopper is good for this purchase" between the shopper's bank and the merchant's bank, then settles
the money. For doing that Visa takes a tiny fee on each swipe and on the dollar volume crossing the
network — plus much richer fees on **cross-border** (international) payments.

Three revenue lines do the work (three months ended 2026-06-30):

| Line | What it is | Q3 FY2026 |
|---|---|---|
| Data processing | Fee per transaction switched | $6,042M |
| Service revenue | Fee on payments volume | $4,922M |
| International transaction | Cross-border / FX — the richest line | $3,853M |
| Other | Value-added services, consulting | $1,496M |
| *Client incentives* | *Paid back to banks to win/keep their business* | *$(4,680)M* |
| **Net revenue** | | **$11,633M** |

Because the network is already built, almost every extra transaction is nearly pure profit. Visa
grows with (a) global consumer spending and (b) the decades-long shift from cash and cheques to
cards and digital wallets.

**What's new since June:** payments volume passed **$4 trillion in a single quarter** for the first
time, and Visa is pushing hard into stablecoins (it launched the Visa Stablecoin Platform in July
2026) and B2B — funded partly by cutting **2,600 jobs, about 7% of staff**, announced 2026-07-28.

## Moat — **wide** (unchanged)

- **Network effect:** more cardholders make Visa more valuable to merchants; more accepting
  merchants make it more valuable to cardholders. The flywheel is extremely hard to copy.
- **Scale and duopoly:** with Mastercard, Visa dominates global card rails. A new entrant cannot
  replicate the acceptance footprint, the fraud systems, or the trust.
- **High switching costs:** banks, acquirers and merchants are all wired into the rails.
- **Honest caveat:** the moat protects the *rails*, not the *fee level*. Regulators and courts —
  not competitors — are the real threat to Visa's economics. See risks.

## The key numbers (all cited)

TTM = trailing twelve months to 2026-06-30, computed as FY2025 minus 9M FY2025 plus 9M FY2026,
all from the two SEC 8-K earnings releases linked below.

| Metric | Value | Period | Source |
|---|---|---|---|
| Net revenue | $44.488B | TTM | [Q3 FY26 8-K][q3] + [FY25 8-K][fy25] |
| Net revenue growth | **+15.3%** (9M FY26 $33.764B vs 9M FY25 $29.276B) | 9M y/y | [Q3 FY26 8-K][q3] |
| 3-yr revenue CAGR | 10.9% (FY22 $29.310B → FY25 $40.000B) | FY22–FY25 | [SEC XBRL][xbrl] |
| Operating income | $26.996B → **60.7% operating margin** | TTM | [Q3 FY26 8-K][q3] + [FY25 8-K][fy25] |
| GAAP net income | $22.592B | TTM | same |
| GAAP diluted EPS | **$11.75** | TTM | same |
| Non-GAAP diluted EPS | $12.77 | TTM | same |
| Operating cash flow | $22.580B | TTM | same |
| Capex | $1.567B | TTM | same |
| **Free cash flow** | **$21.013B** (positive) | TTM | same |
| ROIC | ~38% (net income ÷ equity + total debt); ~50% net of cash | TTM | [Q3 FY26 8-K][q3] |
| Net debt / EBITDA | ~0.35x (net debt $10.066B) | 2026-06-30 | [Q3 FY26 8-K][q3] |
| Processed transactions | 71.7 billion (+10%) | Q3 FY26 | [Q3 FY26 8-K][q3] |
| Cross-border volume | +13% constant-dollar | Q3 FY26 | [Q3 FY26 8-K][q3] |
| Buybacks + dividends | $16.4B + $3.9B | 9M FY26 | [Q3 FY26 8-K][q3] |
| Price / 50d MA / 200d MA | $374.04 / $366.29 / $335.60 | 2026-09-16 | Alpaca |

**Jargon, briefly.** *ROIC* = profit per dollar the business has invested; above 10–15% is good, so
Visa's ~38% is exceptional. *Net debt / EBITDA* = how many years of cash earnings it would take to
pay off debt; under 1x is very safe. *Free cash flow* = real cash left after running and maintaining
the business — harder to fake than "earnings."

### Two things got worse, and they matter

1. **Costs are growing faster than sales.** Q3 GAAP operating expenses rose **19%** while revenue
   rose **14%**. GAAP net income grew only **7%** against 14% revenue growth. That gap is a $563M
   severance charge plus a $237M litigation provision — but a wide-moat compounder should not need
   to shrink its workforce by 7% to fund growth.
2. **Cash conversion slipped.** TTM operating cash flow of **$22.580B is below FY2025's $23.059B**
   even though TTM net income *rose* to $22.592B. One year does not make a trend, but free cash flow
   is the number we actually value the company on, and it stopped growing.

Also worth noting: net debt rose from ~$2.4B to **~$10.1B** in nine months, because $16.4B of
buybacks plus $3.9B of dividends exceeded the $16.3B of cash the business generated. Leverage is
still trivial, but Visa is now returning more than it earns.

## Fair value — how we got there

We used **two methods and averaged them**, with the arithmetic done by `code/valuation.py` (not by
hand). Critically, **we kept the exact same assumptions as the June thesis** — so the whole change
in fair value comes from updated fundamentals, not from quietly raising our multiples to justify a
higher price. That discipline matters: re-rating your assumptions every time a stock goes up is how
you talk yourself into overpaying.

1. **P/E** — TTM GAAP EPS **$11.75** × 25 / 29 / 33 = **$293.75 / $340.75 / $387.75**.
   Why those multiples: Visa has spent most of the past decade in the high-20s to low-30s times
   earnings. 29x is roughly its normal rating; 25x is a mild de-rating; 33x is an optimistic one.
   We use **GAAP** (not adjusted) EPS deliberately — Visa's litigation provisions recur almost every
   year, so excluding them flatters the business.
2. **FCF yield** — TTM FCF per share **$10.93** at 5.0% / 4.2% / 3.5% = **$218.60 / $260.24 / $312.29**.
   (FCF per share uses TTM implied diluted shares of 1.9227B = TTM net income ÷ TTM EPS.)
   This leg is deliberately harsh: Visa has not traded at a 5% FCF yield in over a decade. Treat the
   low end as a genuine "severe de-rating" scenario rather than a forecast.

| | Low | Base | High |
|---|---|---|---|
| P/E method | $293.75 | $340.75 | $387.75 |
| FCF-yield method | $218.60 | $260.24 | $312.29 |
| **Average (our band)** | **$256.18** | **$300.49** | **$350.02** |

**Price today $374.04 → margin of safety −24.5%.** The stock is above even the *high* end of the band.

**Sensitivity, stated honestly.** If you use non-GAAP EPS of $12.77 and tighter FCF yields
(4.5 / 3.8 / 3.2%), the base rises to **$328.98** and the shortfall narrows to **−13.7%**. The P/E leg
alone on GAAP EPS gives a base of **$340.75** (−9.8%). **Under no reasonable set of assumptions we
tried does $374 look cheap.** The most generous framing makes it roughly fair; the conservative
framing makes it 25% expensive.

Fair value *did* rise since June (base $296.91 → $300.49) because earnings grew — but the price rose
faster ($329.91 → $374.04), so the gap widened rather than closed.

## Trend check (from our own Alpaca feed, not the web)

Price $374.04 sits above the 50-day average ($366.29) and well above the 200-day ($335.60). The
250-day range is $293.91–$385.535, so we are near the top of the last year. Momentum is with the
stock — which is exactly why patience is required, not a reason to buy.

## The real risks

- **Valuation is the biggest risk.** At 31.8x TTM GAAP earnings and a 2.96% free-cash-flow yield,
  a de-rating to a normal multiple alone costs 15–25% even if the business performs perfectly.
- **DOJ antitrust suit** (filed Sept 2024) over alleged monopolisation of US debit network services
  is active, with major courtroom activity expected through 2026. A bad outcome could force
  structural change to the debit business.
- **Merchant interchange litigation.** The proposed US credit-interchange settlement was still
  awaiting court approval after an April 2026 hearing. Visa booked another $237M litigation provision
  in Q3 FY2026 alone. This is a chronic cost, not a one-off.
- **Cost discipline.** 19% opex growth vs 14% revenue growth, and a 7% workforce cut, suggest a
  business in transition — spending heavily to defend its position in stablecoins, AI and B2B.
- **Cash conversion.** TTM operating cash flow fell year-on-year despite higher profit. Watch it.
- **Disruption over a decade.** Account-to-account and real-time rails (FedNow, Pix, UPI-style
  systems), stablecoins and Big Tech wallets could route volume around the card networks. Visa's own
  stablecoin push is partly defensive — an admission the threat is real.
- **Cyclicality.** Consumer spending, and especially the high-margin cross-border travel line, fall
  in recessions.

## Sell triggers (the exact rules)

We wrote these in calm conditions. If one fires, we act — we do not renegotiate with ourselves.

1. GAAP operating margin below **50%** for two consecutive quarters (base today: 60.7%).
2. Net revenue shrinks year-over-year for **two consecutive quarters** outside a clearly identified
   macro recession.
3. Processed-transaction growth below **3% y/y** for two consecutive quarters while global card
   spending is still growing (share loss).
4. Constant-dollar cross-border volume growth turns **negative** for two consecutive quarters
   outside a travel shock.
5. Net-debt-to-EBITDA rises above **2.0x** (today ~0.35x).
6. Free cash flow negative for a full fiscal year, **or** TTM FCF below **60% of TTM net income**
   for two consecutive quarters.
7. A final, non-appealable ruling or settlement structurally capping interchange/network fees in the
   US or EU expected to cut net revenue by more than **~15%**.
8. An adverse final judgment in the DOJ debit case forcing divestiture or mandated unbundling.
9. GAAP operating expenses grow faster than net revenue for **four consecutive quarters**
   (currently 19% vs 14% — one quarter in).
10. A serious accounting red flag or restatement.

## Conviction: 4 / 5

Four, not five. The business quality genuinely deserves a five — wide moat, 60% margins, ~38% ROIC,
$21B of free cash flow, accelerating revenue. We hold it at four because the numbers are strong but
two of them (cost growth, cash conversion) moved the wrong way this quarter, and because the price
offers no cushion at all.

**This is a watch, not a buy.** The band says we would start to get interested near the high end of
fair value (~$350) and would want to buy meaningfully closer to the base (~$300) — roughly 6% and 20%
below today's price. A missed buy costs nothing; an overpriced buy costs money.

## What to watch next

- **Q4 / full-year FY2026 earnings, expected late October 2026** — does opex growth re-converge with
  revenue growth? Does operating cash flow recover?
- Court decisions on the merchant interchange settlement and the DOJ debit case.
- Whether the Visa Stablecoin Platform wins volume or cannibalises it.
- Continued share-count reduction from buybacks.

## Data quality

**Filing-backed.** Every financial figure above comes from Visa's own SEC 8-K earnings releases. Two
exceptions are flagged honestly:
- The **FY2022 revenue** figure used for the 3-year CAGR is carried forward from the June thesis. The
  SEC XBRL company-concept API returned an empty result when re-fetched on 2026-09-16, so it was not
  independently re-verified today.
- The **layoff count** (2,600 / 7%) and the **litigation status** items come from trade press, not
  filings. The related **$563M severance charge** and **$237M litigation provision** *are*
  filing-backed. No dollar amount in the valuation depends on a non-filing source.

---

### Sources

[q3]: https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm
[fy25]: https://www.sec.gov/Archives/edgar/data/1403161/000140316125000077/q42025earningsrelease.htm
[xbrl]: https://data.sec.gov/api/xbrl/companyconcept/CIK0001403161/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax.json

- [Visa Inc. Form 8-K — Q3 FY2026 earnings release (quarter ended 2026-06-30), SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm)
- [Visa Inc. Form 8-K — Q4 / FY2025 earnings release (year ended 2025-09-30), SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1403161/000140316125000077/q42025earningsrelease.htm)
- [Visa revenue history — SEC EDGAR XBRL company-concept API](https://data.sec.gov/api/xbrl/companyconcept/CIK0001403161/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax.json)
- [Visa cuts 2,600 tech jobs to fund stablecoin and B2B growth — PYMNTS.com](https://www.pymnts.com/visa/2026/visa-cuts-2600-tech-jobs-to-fund-stablecoin-and-b2b-growth/)
- [DOJ presses Visa antitrust case — Payments Dive](https://www.paymentsdive.com/news/doj-presses-visa-antitrust-case/808859/)
- [Visa/Mastercard 2026 interchange settlement status and timeline — Brookside Payments](https://brooksidepayments.com/visa-mastercard-2026-settlement/)
- Price and moving averages: Alpaca market data via `code/alpaca_client.py --quote V` and `--bars V --days 250`, retrieved 2026-09-16.
