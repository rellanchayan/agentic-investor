# Alphabet Inc. (GOOGL) — Research Thesis

*As of 2026-Q1 data · written 2026-06-27 · refresh due 2026-09-25 · conviction 3/5 · moat: wide*

## What the company does (plain English)
Alphabet is the parent company of Google. Most of its profit comes from **Google Services** —
ads shown next to **Search** results (the single biggest money-maker), ads on **YouTube**, the
ad network, plus subscriptions and devices (YouTube Premium, Google One, Pixel). The
fast-growing second engine is **Google Cloud**, which rents computing, data, and AI services to
businesses. A small "Other Bets" unit (e.g. Waymo self-driving) still loses money. In one line:
Alphabet earns money by placing ads against the world's searches and videos, and increasingly by
renting out its huge AI/compute infrastructure.

## Why it has a moat (wide)
- **Search is a near-monopoly** (~90% global share). More users produce more data, which makes
  results better, which attracts more users — a self-reinforcing loop.
- **YouTube** is an unmatched two-sided network of creators and viewers.
- **AI/infrastructure edge**: custom AI chips (TPUs), DeepMind/Gemini research, and global data
  centers. Distribution through Android, Chrome, and default-search deals reinforces the lead.

## The key numbers (all cited)
| Metric | Value | Period | Source |
|---|---|---|---|
| Revenue | $402.8B (+15% YoY) | FY2025 | [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| Operating income / margin | $129.0B / ~32% | FY2025 | [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| Net income / diluted EPS | $132.2B / $10.81 | FY2025 | [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| 3-yr revenue CAGR | 12.5% (FY22 $282.8B → FY25 $402.8B) | FY2022–FY2025 | [SEC](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) + [stockanalysis](https://stockanalysis.com/stocks/GOOGL/financials/) |
| Gross margin | 60.37% | TTM to Mar 2026 | [stockanalysis](https://stockanalysis.com/stocks/GOOGL/financials/) |
| ROIC (est.) | ~23% | FY2025 | computed from [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| Net debt / EBITDA | -0.53x (net cash ~$80B) | end-2025 | computed from [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| Free cash flow | +$73.3B (OCF $164.7B − capex $91.4B) | FY2025 | [SEC FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000012/googexhibit991q42025.htm) |
| Q1 2026 revenue / op margin | $109.9B (+22%) / 36.1% | Q1 2026 | [SEC Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm) |
| Q1 2026 Google Cloud | $20.0B (+63%) | Q1 2026 | [SEC Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm) |
| Cloud backlog | >$460B (nearly doubled QoQ) | Q1 2026 | [CNBC](https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html) |
| FY2026 capex guidance | $180–190B | FY2026 | [SEC Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm) |

Balance sheet is a fortress: ~$126.8B cash + marketable securities vs $46.5B long-term debt at
end-2025 (~$80B net cash). The company also pays a growing dividend ($0.22/qtr, +5% in Apr 2026)
and buys back stock (diluted shares ~12.24B in Q1 2026 vs ~12.29B a year earlier).

## Fair value and how we got it
Current price (Alpaca, 2026-06-27): **$335.79** (below the 50-day average $369.26, above the
200-day $313.85; 6-month return ~+6.9%).

We used two methods via `code/valuation.py`:
- **P/E**: normalized EPS ~$9.50 (FY2025 reported EPS $10.81 is inflated by large one-off equity
  gains, so we strip the volatile portion) × multiples of 24 / 28 / 33. A high-quality compounder
  like this has historically traded in the high-20s P/E.
- **FCF yield**: normalized FCF/share ~$7.86 at 4.0 / 3.4 / 2.8% target yields. **Important:**
  reported FCF is temporarily depressed by an extraordinary AI capex super-cycle (capex $91B in
  FY2025, guided $180–190B in FY2026), so we normalized capex toward ~17% of revenue rather than
  using the spike year. This is a judgment call and widens our uncertainty.

Resulting fair-value band: **low $212 / base $249 / high $297**.

**Honest conclusion:** at $335.79 the stock trades **~35% above our base fair value and above the
top of our band** — there is **no margin of safety** today. The price already bakes in continued
AI/cloud success. This is a wonderful business at a full (arguably expensive) price.

## The real risks (taken as seriously as the bull case)
1. **AI disruption to Search.** ChatGPT, Perplexity, Copilot and AI answer-engines could shrink
   the search queries and ad clicks that fund most of Alphabet's profit. Search & other runs at
   roughly $54B/quarter, so even a few points of lost share/monetization is large in dollars.
2. **Antitrust.** A U.S. court ruled Google illegally monopolized search; remedies could limit or
   ban default-search distribution deals or force divestitures, weakening the moat. Ad-tech cases
   are also live.
3. **Capex super-cycle.** $180–190B planned in FY2026 (rising in FY2027). If AI/cloud returns
   disappoint, this crushes free cash flow and ROIC for years.
4. **Valuation.** No cushion at today's price; a growth disappointment could de-rate the multiple.
5. **Earnings noise.** Headline EPS is distorted by unrealized swings on equity stakes (a ~$37.7B
   gain in Q1 2026 alone), so don't anchor on reported EPS.

## Sell triggers (what would break the thesis)
- Google Search & other (ad) revenue **declines YoY for two consecutive quarters**.
- Google Cloud growth **falls below ~20% YoY for two consecutive quarters AND backlog stops growing**.
- A final antitrust remedy **forces divestiture of a core asset (Chrome/Android) or bans default-search deals**.
- Consolidated **operating margin below 25% for two consecutive quarters** (vs ~32% now).
- **Net cash turns to net debt with net-debt/EBITDA above 1.0x**, or a serious accounting red flag.
- **Annual free cash flow stays negative/near-zero for a full year** as capex outruns cash with no revenue payoff.

## Catalysts to watch
- Q2 2026 earnings (~late July 2026): Cloud growth/backlog and Search ad resilience vs AI.
- Antitrust remedy/appeal outcomes.
- Evidence Gemini/AI monetization (AI Overviews ads, Gemini subs, enterprise AI) is **additive**.
- Signs the capex buildout is converting into durable cloud revenue and better returns.

## Bottom line
Wide-moat, cash-rich, growing — a genuinely high-quality business (conviction 3/5). But it is
priced for success today with no margin of safety, and it faces two serious, hard-to-quantify
overhangs (AI disruption of Search, antitrust). **Quality: yes. Price: not yet.** Patience until
the price approaches our fair-value band, or until the AI-Search question resolves more clearly.
