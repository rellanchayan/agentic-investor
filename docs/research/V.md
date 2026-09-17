# Visa Inc. (V) — Research Thesis

- **Thesis ID:** V-2026Q3 · **As of:** fiscal Q3 2026 (quarter ended 2026-06-30)
- **Retrieved:** 2026-09-17 · **Refresh due:** 2026-10-17 (FY2026 full-year results land late October)
- **Price used:** $369.51 · **Moat:** wide · **Conviction:** 4 / 5
- **Fair value band:** $246 (low) — **$292 (base)** — $340 (high)
- **Margin of safety: −26.7% → the stock is EXPENSIVE. This is a "great business, wrong price" — not a buy today.**

---

## 1. What the business actually does

Visa is a toll booth, not a bank. It does not lend you money and it does not issue your card —
your bank does that. Visa owns and operates VisaNet, the wiring that carries the "can this card
pay?" message from the shop's bank to your bank and back, and then settles the money. It gets paid
four ways:

1. **Service revenue** — a fee on the dollar volume that ran over the network last quarter ($4.922B in Q3 FY2026, +14%).
2. **Data processing revenue** — a small fee per transaction switched ($6.042B, +17%).
3. **International transaction revenue** — the juiciest fees, charged when the card and the merchant are in different countries ($3.853B, +6%).
4. **Other revenue** — value-added services: fraud tools, tokenisation, consulting, Visa Direct ($1.496B, **+45%**).

From that it subtracts **client incentives** — the money it pays banks to keep issuing Visa cards
($4.680B in Q3, +18%). What's left is "net revenue": **$11.633B in Q3 FY2026, up 14%**.
([Q3 FY2026 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000103/q32026earningsrelease.htm))

In the June quarter Visa switched **71.7 billion transactions (+10%)** and payments volume crossed
**$4 trillion in a single quarter for the first time**. Because the network is already built, almost
every extra transaction drops straight to profit.

## 2. Why the moat is wide (in plain words)

A "moat" is a lasting reason competitors can't take the business away. Visa has several stacked:

- **Network effect.** Merchants accept Visa because billions of people carry it; people carry it
  because everyone accepts it. Each side makes the other side more valuable. A new network has to
  solve both at once, which nobody has managed at global scale.
- **Scale.** 200+ countries, 71.7 billion transactions a quarter, and only ~$1.6B a year of capex to
  run it. Nobody can undercut that cost per transaction.
- **Switching costs and trust.** Banks, acquirers and merchants have plumbing wired into VisaNet.
  Ripping it out is expensive and risky.
- **Near-duopoly.** Visa and Mastercard control roughly 77% of the US credit-card market
  ([Payments Dive](https://www.paymentsdive.com/news/credit-card-network-legilsation-marshall-durbin-stablecoin-payments/750802/)).

## 3. The key numbers (all from SEC filings)

All figures are trailing-twelve-months (TTM) through 2026-06-30 unless stated, built from the
[Q3 FY2026 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000103/q32026earningsrelease.htm)
and the [FY2025 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316125000077/q42025earningsrelease.htm).

| Measure | Value | How we got it |
|---|---|---|
| TTM net revenue | **$44.488B** | Q4 FY25 $10.724B + Q1 $10.901B + Q2 $11.230B + Q3 $11.633B |
| 3-year revenue CAGR | **10.9%** | FY2022 $29.310B ([FY23 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316123000092/q42023earningsrelease.htm)) → FY2025 $40.000B |
| Recent growth | **+15.3%** | 9M FY2026 $33.764B vs 9M FY2025 $29.276B |
| TTM operating margin | **60.7%** | $26.996B operating income ÷ $44.488B |
| Q3 FY2026 operating margin | 59.1% (was 60.7% a year ago) | $6.877B ÷ $11.633B — **slipping** |
| TTM GAAP diluted EPS | **$11.76** | $2.62 + $3.03 + $3.14 + $2.97 |
| TTM non-GAAP EPS | **$12.78** | $2.98 + $3.17 + $3.31 + $3.32 |
| TTM free cash flow | **~$21.0B** | OCF $22.580B − capex $1.567B |
| TTM FCF per share | **~$10.93** | ÷ 1,923M average diluted class A (as-converted) shares |
| ROIC | **~38%** | NOPAT $22.6B ÷ invested capital $59.0B (equity $35.178B + debt $23.858B) |
| Net debt / EBITDA | **~0.35x** | net debt $9.9B ÷ EBITDA ~$28.3B |
| Buyback firepower left | **$28.4B** | authorisation remaining at 2026-06-30 |
| Dividend | $0.670/quarter → ~0.73% yield | declared 2026-07-28 |

**Gross margin** isn't a meaningful concept for a network, so we use operating margin instead.
At ~61% it is among the best of any large company on earth. **ROIC of ~38%** means every dollar the
business has tied up earns about 38 cents a year — far above the ~10-15% bar for a compounder.
The balance sheet is a fortress: net debt is about four months of EBITDA.

One honest note: net debt rose from ~$2.4B a year ago to ~$9.9B, because Visa bought back
**$16.430B** of its own stock in nine months and paid **$3.852B** of dividends. That is a choice,
not distress — but it is worth watching.

## 4. Fair value — how we got the band

We used two methods and averaged them (arithmetic done by `code/valuation.py`, not by hand):

**Method 1 — Price/Earnings.** TTM GAAP EPS of **$11.76** × **24 / 28 / 32** = **$282 / $329 / $376**.
Visa has historically traded around 28-32x earnings. We trimmed roughly one turn off last quarter's
25/29/33 because **the Fed has just hiked to 3.75-4.00%** — when safe cash yields more, investors pay
less for far-off profits.

**Method 2 — Free-cash-flow yield.** TTM FCF/share of **$10.93** at required yields of
**5.2% / 4.3% / 3.6%** = **$210 / $254 / $304**. We raised the required yields ~0.2pp for the same
rate reason.

**Average → low $246.22, base $291.73, high $339.97.**
At $369.51 that is a margin of safety of **−26.7%**: the price is above even the top of our band.

**The honest cross-check.** GAAP EPS is depressed by things that aren't really "operations": a
**$1.290B litigation provision** and **$563M of severance** in the last nine months. On TTM *non-GAAP*
EPS of **$12.78**, the same 24/28/32 multiples give **$307 / $358 / $409** — on that basis the stock
is roughly *fair*, not wildly expensive. We publish the GAAP-based band as the headline because GAAP
is harder to flatter, but a reader should know the answer is sensitive to that choice. Either way,
**there is no margin of safety at $369.51.**

**What price would make it a buy?** Our rule needs a 12% margin of safety (18% in a cautious market
posture). That is roughly **$257**, or **$239** under the cautious rule — about 30-35% below today.
A normal correction alone probably won't get us there; fair value also has to grow into the price.
As a market check: the stock is above both its 50-day ($366.66) and 200-day ($335.76) moving
averages, so we would be buying into an uptrend, not a fall (Alpaca, 250 daily closes).

## 5. What's changed since the June 2026 thesis

- Q3 FY2026 delivered: revenue +14%, GAAP EPS +10%, non-GAAP EPS +11%. Nine-month growth is 15.3%.
- **The big lawsuit is largely settled.** On **2026-06-09 the court approved** the ~$38B US merchant
  interchange settlement: credit interchange trimmed by 10 basis points for five years, a 1.25% cap
  on standard consumer cards for eight years, and merchants gain the right to decline some premium
  and commercial cards and to surcharge
  ([Payments Dive](https://www.paymentsdive.com/news/court-approves-visa-mastercard-settlement/822440/)).
  Interchange is paid to *issuing banks*, not to Visa, so the direct revenue hit is small — the real
  risk is mix, if merchants push customers off high-value premium cards.
- **Costs are running hot.** Q3 GAAP operating expenses +19% vs revenue +14%; personnel expense +40%.
  Operating margin slipped from 60.7% to 59.1%. Interest expense jumped to $194M from $39M.
- **Macro turned against the multiple.** First Fed hike since 2023, to 3.75-4.00%, inflation 3.4%.
- Price is up ~12% since our June review ($329.91 → $369.51) while our base fair value barely moved.
  The gap got worse, not better.

## 6. The real risks (written as hard as the bull case)

1. **Price.** 31.4x GAAP / 28.9x non-GAAP TTM earnings with a 0.73% yield. At this price we are
   paying for perfection. This is the dominant risk and it is entirely self-inflicted if we buy.
2. **Rising rates.** Higher risk-free rates directly compress what anyone will pay for a
   long-duration compounder — and they raise Visa's own interest bill.
3. **Margin drift.** Expenses growing faster than revenue for a "payments hyperscaler" build-out.
   If 59% becomes 55%, the earnings base we valued shrinks.
4. **Client incentives +18% vs revenue +14%.** Visa is paying banks more to stay in the wallet. A
   slow bleed on the take rate.
5. **Regulation.** The Credit Card Competition Act — forcing a second, non-Visa routing option — is
   still alive in Congress. Plus the new merchant rights to decline premium cards and surcharge.
6. **Disruption.** FedNow, UPI, Pix, stablecoins and Big Tech wallets can in principle route around
   the card rails. Visa is investing to be inside that shift rather than outside it, but the outcome
   is genuinely uncertain over 10 years.
7. **Cyclicality.** Cross-border travel spend is the highest-margin line and the first to fall in a
   recession. Management's own Q4 FY2026 commentary flags tougher FX comps, Middle East uncertainty
   and less FIFA-related revenue.
8. **GAAP noise.** The $1.76B gap between TTM GAAP and non-GAAP profit is large enough that the
   valuation conclusion partly depends on which one you believe.

## 7. Sell triggers — the exact rules

If we ever own it, we sell (or at minimum re-underwrite from scratch) when any of these happen:

1. GAAP operating margin falls **below 55% for two consecutive quarters** (it is 59.1% now).
2. Net revenue **shrinks year-over-year for two consecutive quarters** outside a clear recession.
3. **Client incentives grow faster than net revenue for four consecutive quarters.**
4. **Net debt / EBITDA rises above 2.0x** (it is ~0.35x).
5. **Free cash flow turns negative for a full fiscal year**, or TTM FCF falls >25% YoY absent a one-off.
6. A ruling, statute (e.g. the Credit Card Competition Act passing) or settlement that structurally
   caps network fees or mandates alternative routing in a major market and is expected to cut net
   revenue by **more than ~15%**.
7. **Cross-border volume growth stalls structurally** — negative or near-zero constant-dollar growth
   for four consecutive quarters outside a recession.
8. **Processed transaction growth falls below 3% YoY for two consecutive quarters** while global
   consumer spending is still growing — the clearest early warning of disintermediation.
9. Any **serious accounting red flag, restatement, or disclosed material weakness**.

## 8. Bottom line

Visa is close to the ideal business: a wide-moat toll booth on global consumer spending, ~61%
operating margins, ~38% ROIC, $21B of real cash profit, almost no debt, growing revenue at 15%, and
its biggest legal overhang now settled. **Conviction 4/5 on the business.**

But conviction is about quality, not price. At **$369.51 the stock sits ~27% above our base fair
value of $292** and above the top of our band. Our own playbook says a missed buy costs nothing and
an overpriced buy costs money. **Recommendation to the portfolio manager: do not buy V at this
price. Watch it. Revisit at the FY2026 results in late October, or if the price approaches the
mid-$250s.**

---

*Every number above is cited to a Visa SEC filing, to Alpaca for price, or to a named news source.
Nothing is estimated except where the arithmetic is shown. Validated with
`python3 code/thesis.py --check V` → PASS.*
