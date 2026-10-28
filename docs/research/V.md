# Visa Inc. (V) — Research Thesis

- **Thesis ID:** V-2026Q4 · **As of:** fiscal Q4 / full-year FY2026 (year ended 2026-09-30)
- **Retrieved:** 2026-10-28 · **Refresh due:** 2027-01-27 (Q1 FY2027 results expected late January)
- **Price used:** $401.30 (Alpaca) · **Moat:** wide · **Conviction:** 4 / 5
- **Fair value band:** $259 (low) — **$307 (base)** — $358 (high)
- **Margin of safety: −30.7%. The stock is EXPENSIVE. Visa is a great business at the wrong price, so it is not a buy today. The gap widened since September.**

---

## 1. What the business actually does

Visa works like a toll booth, not a bank. It does not lend money or issue cards; your bank does
that. Visa runs VisaNet, the wiring that carries the "can this card pay?" message between the
shop's bank and your bank and then settles the money. It is paid in four ways:

- a small fee per transaction (**data processing**: $23.4B in FY2026, +17%),
- a fee on dollar volume (**service revenue**: $19.9B, +14%),
- a richer fee when money crosses borders (**international transaction revenue**: $15.3B, +8%),
- a fast-growing set of add-on services such as fraud tools, data and tokens (**other revenue**: $5.7B, +40%).

From these it subtracts **client incentives** ($18.3B, +16%), which are payments to banks and
partners to keep them issuing Visa cards. In FY2026 Visa handled **281.3 billion transactions**
(+9%) and earned **$45.9B of net revenue** (+15%).
([FY2026 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/q42026earningsrelease.htm))

## 2. Why the moat is wide

The moat is a **network effect**. Shoppers carry Visa because almost every merchant accepts it,
and merchants accept it because almost every shopper carries it. A newcomer would have to sign up
billions of cardholders and tens of millions of merchants at the same time. Add decades of brand
trust and deep plumbing inside thousands of banks, which makes switching costly. Visa and Mastercard
together control roughly 77% of US credit cards
([Payments Dive](https://www.paymentsdive.com/news/ccca-seeks-new-path-to-passage/813789/)).
Each extra transaction costs Visa almost nothing, which is why operating margins sit around 60%.

## 3. The key numbers (from SEC filings unless noted)

| Metric | Value | Source |
|---|---|---|
| Net revenue FY2026 | $45.903B (+15%) | [Q4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/q42026earningsrelease.htm) |
| 3-year revenue growth | 12.0%/yr (FY2023 $32.653B → FY2026) | [FY23 8-K](https://www.sec.gov/Archives/edgar/data/1403161/000140316123000092/q42023earningsrelease.htm), Q4 FY26 8-K |
| Quarterly revenue growth FY2026 | +15%, +17%, +14%, +13% (slowing) | Q1–Q4 FY26 8-Ks |
| GAAP operating margin | 61.2% FY2026; 59.8% in Q4 | Q4 FY26 8-K |
| GAAP diluted EPS | $12.32 (+21%); non-GAAP $13.27 (+16%) | Q4 FY26 8-K |
| ROIC | ~40% (NOPAT ~$23.5B / equity+debt ~$58.2B) | derived from Q4 FY26 8-K |
| Free cash flow | ~$22.06B ($23.728B OCF − $1.671B capex) = ~$11.57/share | Q4 FY26 8-K |
| Net debt / EBITDA | ~0.27x (net debt ~$7.9B / EBITDA ~$29.5B) | Q4 FY26 8-K |
| Capital returned FY2026 | $20.5B buybacks + $5.1B dividends; $24.4B authorisation left | Q4 FY26 8-K |
| Dividend | raised 16% to $0.780/quarter (~0.78% yield) | Q4 FY26 8-K |
| Client incentives growth vs net revenue | Q1 12% vs 15%; Q2 14% vs 17%; **Q3 18% vs 14%; Q4 21% vs 13%** | [Q1](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000044/q12026earningsrelease.htm), [Q2](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000077/q22026earningsrelease.htm), [Q3](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000103/q32026earningsrelease.htm), Q4 8-Ks |
| Price / trend | $401.30; 50-day avg $379.50; 200-day avg $341.39 (uptrend) | Alpaca |

**FY2027 guidance** (from the call; [transcript](https://www.fool.com/earnings/call-transcripts/2026/10/28/visa-v-q4-2026-earnings-call-transcript/), an aggregator):
adjusted revenue growth in the "low double digits", lowest in Q2. Adjusted EPS growth "low double digits to low
teens". The tax rate rises to ~19% from ~16%. The CFO said to expect "a higher volume of incentives in '27"
because ~25% of payments volume comes up for contract renewal.

## 4. Fair value: how we got the band

We used `code/valuation.py` with two methods and averaged them:

1. **P/E:** FY2026 GAAP EPS $12.32 × 24 / 28 / 32 = $296 / $345 / $394. A steady wide-moat
   compounder growing low double digits deserves a premium multiple, but not an unlimited one.
2. **Free-cash-flow yield:** FCF/share $11.57 at a required 5.2% / 4.3% / 3.6% = $223 / $269 / $321.

**Band: $259 / $307 / $358.** At $401.30, the margin of safety is −30.7%.

**What changed since 2026-09-17 (base $292 → $307, +5.2%)?** Only the inputs. The full year
is now reported, so GAAP EPS went from $11.76 (TTM) to $12.32 and FCF/share from $10.93 to $11.57.
We did **not** change the multiples or required yields. The Fed's last move was a hike to 3.75–4.00%,
and the October FOMC decision lands after this refresh, so there is no new reason to change them
(per the playbook rule against upward drift without a named cause).

**Cross-check:** on *non-GAAP* EPS ($13.27) the same multiples give $318 / $372 / $425. Even on that
friendlier measure the stock sits ~8% above the base. Wall Street targets after the report
cluster around $425–$480 ([Investing.com](https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-visa-stock-price-target-on-stable-earnings-growth-93CH-4978693)).
They assume roughly 27x *2028* earnings, which is more optimism than our framework allows.

**Buy zone:** about $270 (12% margin of safety) or about $252 (cautious 18% rule). That is a 33–37%
fall from here. At ~11–13% EPS growth, it would take roughly 2–3 years of a flat price for value to catch up.

## 5. What's changed since the September thesis

- Full-year FY2026 is reported: revenue +15%, GAAP EPS +21%, FCF ~$22.1B.
- Growth is **slowing** quarter by quarter (17% → 14% → 13%), and FY2027 is guided lower again.
- **Client incentives are now growing faster than revenue for 2 quarters in a row**, and management
  expects more in FY2027. This is the most important new fact.
- Dividend +16%; net debt fell to ~0.27x EBITDA.
- New option value: China domestic-processing preparations approved; stablecoin settlement run rate
  above $25B annualised ([BigGo summary](https://finance.biggo.com/news/US_V_2026-10-27), an aggregator).
- The price went up ~8.6% (from $369.51 to $401.30) while fair value rose ~5.2%, so the stock got *more* expensive.

## 6. The real risks

1. **Valuation.** 32.6x GAAP earnings for a business guiding 11–13% EPS growth. If the multiple fell
   back to ~25x, the stock would lose about a quarter of its value even with the business doing fine.
2. **Take-rate squeeze.** Banks are demanding bigger incentives at renewal time, and FY2027 has more
   renewals than FY2026.
3. **Slowing growth.** Revenue growth has decelerated three quarters running, and the tax rate is rising.
4. **Rates.** The Fed is hiking; long-duration compounders lose multiple when rates rise.
5. **Regulation.** The Credit Card Competition Act is still alive (presidential endorsement, new
   cosponsors), and the MDL settlement lets merchants surcharge and decline premium cards.
6. **Disruption.** Real-time bank rails (FedNow, UPI, Pix), stablecoins and Big Tech wallets.
7. **Cyclicality and geopolitics.** Cross-border revenue grew only 8%; CEMEA conflict and FX are named drags.
8. **Noisy GAAP.** Litigation provisions recur every year ($1.7B in FY2026).

## 7. Sell triggers: the exact rules

1. GAAP operating margin below 55% for two consecutive quarters (now 59.8%).
2. Net revenue shrinks YoY for two consecutive quarters outside a recession.
3. Client incentives grow faster than net revenue for four consecutive quarters. **Now 2 of 4.** Watch Q1 and Q2 FY2027.
4. Net debt / EBITDA above 2.0x (now ~0.27x).
5. FCF negative for a full year, or more than 25% below the prior year absent a one-off.
6. A law, ruling or settlement that caps fees or mandates alternative routing in a major market and is expected to cut net revenue >15%.
7. Cross-border volume growth near zero or negative for four straight quarters outside a recession.
8. Processed-transaction growth below 3% for two straight quarters while consumer spending grows.
9. A serious accounting red flag, restatement or material weakness.

## 8. Bottom line

Visa remains one of the best businesses in the world: a wide moat, ~40% ROIC, ~$22B of free cash and
a strong balance sheet. Conviction stays at **4/5**. It is **not a buy at $401**: the price is ~31%
above our base fair value, and the gap widened this quarter. The new watch item is client
incentives. If they keep outgrowing revenue through Q2 FY2027, the incentives sell trigger fires,
and conviction should then be cut.
