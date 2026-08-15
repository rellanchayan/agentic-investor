# Candidate Scout — Weekly Proposal (2026-08-15)

> Paper money only. This document proposes names for research; no orders are placed.
> Every number is cited. These names have no thesis document yet; the research analyst
> must write `state/theses/TICKER.json` before any name can be considered for a buy.

---

## Context and Watchlist Gaps Identified

The existing watchlist had 30 names across 9 buckets. Two sectors were entirely absent:
**Real Estate** and **Utilities**. Communication/Media had only one name (DIS). Financials
had payments and one big bank but nothing in asset management. The SaaS/software
sub-category beyond CRM and ADBE was also flagged as a gap.

Five candidates were reviewed. Three passed; two were dropped.

---

## Proposed Addition 1 — META (Meta Platforms)

**Sector added:** Communication/Media (DIS was the only name; now two)

**The business:** Meta owns Facebook, Instagram, and WhatsApp. It sells advertising against
a combined audience of more than three billion daily active users across the family of apps
(as of 2025).

**The moat:** Network effects. Each additional user makes the platform more valuable to
every other user and to advertisers who need reach. Social graphs and contacts are not
portable, so switching costs are high. Replicating the scale is effectively impossible;
no competitor has come close.

**Quality check:**

| Metric | Value | Source |
|---|---|---|
| Price | $589.85 | StockAnalysis / CNN, Aug 15 2026 |
| Market cap | ~$1.5 trillion | StockAnalysis |
| Trailing P/E | ~20.1x | GuruFocus, Aug 13 2026 |
| LTM operating cash flow | $130.3B | StockAnalysis |
| LTM capex | $89.3B | StockAnalysis |
| LTM free cash flow | ~$40.98B | StockAnalysis |
| ROIC | 25.4% | StockAnalysis |
| Gross margin | 81.75% | StockAnalysis |
| Operating margin | 38.1% | StockAnalysis |

FCF is genuinely large and positive even after very heavy AI infrastructure spending.
ROIC above 25% with a P/E near 20 is unusual for a business of this quality.

**Main risk:** Regulatory fragmentation of the platforms, or a structural shift away from
social advertising.

---

## Proposed Addition 2 — INTU (Intuit)

**Sector added:** Technology/SaaS (distinct from hardware, semiconductors, or enterprise CRM)

**The business:** Intuit makes TurboTax (DIY tax filing), QuickBooks (SMB accounting/payroll),
and Credit Karma (personal finance). Small businesses and individuals run their financial
lives through Intuit products and renew year after year.

**The moat:** Switching costs. TurboTax holds roughly 70% of the DIY tax-preparation market;
QuickBooks holds roughly 80% of the SMB accounting market (source: Morningstar moat report).
A small business running payroll, invoicing, and books in QuickBooks does not switch lightly.
Tax-return history locked inside TurboTax creates annual re-purchase behaviour.

**Quality check:**

| Metric | Value | Source |
|---|---|---|
| Price | $345.66 | StockAnalysis, Aug 14 2026 |
| Market cap | $94.55B | StockAnalysis |
| Trailing P/E | 21.1x | StockAnalysis |
| LTM FCF | ~$7.76B | GuruFocus FCF/share $27.80 × ~279M diluted shares |
| LTM operating cash flow | ~$7.89B | GuruFocus |
| LTM capex | ~$133M | GuruFocus |
| FCF yield at current price | ~8% | Trefis, July 2026 |
| Analyst 12-month consensus target | $451 (~30% upside) | Analyst consensus |

**Caution:** The stock is down roughly 52% from recent highs (source: StockAnalysis).
Earnings are due August 25, 2026. The research analyst must understand what drove the
de-rating before forming a view on fair value. Business fundamentals (market share, FCF,
switching costs) appear intact, but the price move demands explanation.

---

## Proposed Addition 3 — PLD (Prologis)

**Sector added:** Real Estate — this sector was entirely absent from the watchlist.

**The business:** Prologis is the world's largest industrial/logistics REIT. It owns and
leases warehouse and distribution centres near major population centres and transport hubs.
Tenants include the companies fulfilling e-commerce orders and managing supply chains
(Amazon, FedEx, and equivalents globally).

**The moat:** Location and scale. Logistics sites near dense urban areas and
port/rail infrastructure are physically irreplaceable — you cannot build a new warehouse
next to an airport in a major city. Prologis has roughly 1.2 billion square feet across
19 countries, giving it bargaining power with tenants that no single-market owner can match.
As e-commerce continues to take share from physical retail, demand is structurally supported.

**Quality check:**

| Metric | Value | Source |
|---|---|---|
| Price | $141.03 | Digrin / Yahoo Finance, Aug 14 2026 |
| Market cap | ~$134B | StockAnalysis |
| 52-week range | $105.42–$153.35 | Yahoo Finance |
| LTM FCF | ~$4.3B | StockAnalysis |
| Price-to-FFO | 24.4x | GuruFocus (FFO is the standard REIT metric) |
| Trailing P/E (GAAP) | 35.1x | GuruFocus (elevated due to non-cash depreciation; FFO is the correct lens) |

**Caution:** The stock has returned roughly 42% over the past year (source: StockAnalysis),
so it may not be cheap. Prologis has announced an $18.8B acquisition of Segro (UK
industrial/data-centre REIT); integration risk is real. The research analyst should build a
proper FFO-based fair-value model before considering any entry.

---

## Names Reviewed But Not Proposed This Week

### NEE (NextEra Energy)
Wide moat (31 consecutive years of dividend growth, dominant in regulated utilities and
renewables), but trailing free cash flow is **negative at -$15.4B LTM** (source:
StockAnalysis), because the company is investing $27.7B/year in new renewable capacity.
Our criteria require genuinely positive FCF. Revisit if the capex cycle moderates.

### BLK (BlackRock)
Excellent business — $15 trillion AUM, Aladdin platform that competitor firms pay to use,
30% operating margins. But FCF yield is only **2.3%** with price-to-FCF of 46.6x (source:
FinanceCharts, Feb 2026). Too expensive today for a "quality at a fair price" discipline.
Worth continuing to watch.

---

## Changes Made to State Files

- `state/watchlist.txt` — added META, INTU, PLD with brief sector comments
- `state/sectors.json` — added `META: "communication"`, `INTU: "technology"`, `PLD: "real_estate"`

---

## Next Steps for Research Analyst

These three names are watchlist additions only. Before any can be considered for a buy:
1. Build a full thesis: `state/theses/META.json`, `state/theses/INTU.json`, `state/theses/PLD.json`
2. Every number in the thesis must be cited; `python3 code/thesis.py --check TICKER` must pass
3. Establish fair-value range (low/base/high) with sell triggers
4. Confirm margin of safety at the time of the buy decision

---

## Sources

- [Meta Platforms (META) — StockAnalysis](https://stockanalysis.com/stocks/meta/)
- [Meta Platforms Statistics & Valuation — StockAnalysis](https://stockanalysis.com/stocks/meta/statistics/)
- [META PE Ratio — GuruFocus](https://www.gurufocus.com/term/pe-ratio/META)
- [Meta Platforms PE Ratio 2026 — FinanceCharts](https://www.financecharts.com/stocks/META/value/pe-ratio)
- [Intuit (INTU) Stock Price & Overview — StockAnalysis](https://stockanalysis.com/stocks/intu/)
- [Intuit FCF per Share — GuruFocus](https://www.gurufocus.com/term/free-cash-flow-per-share/INTU)
- [The Cash Machine The Market Put On Sale: INTU — Trefis, July 2026](https://www.trefis.com/stock/intu/articles-v3/608356/the-cash-machine-the-market-put-on-sale-intu/2026-07-22)
- [Intuit's Wide Moat — Morningstar](https://www.morningstar.com/company-reports/1267137-intuits-dominant-market-position-ensures-high-switching-costs-that-support-its-wide-moat)
- [Prologis (PLD) Stock Price & Overview — StockAnalysis](https://stockanalysis.com/stocks/pld/)
- [Prologis Price-to-FFO — GuruFocus](https://www.gurufocus.com/term/price-to-ffo/PLD)
- [Prologis Stock Price History — Yahoo Finance](https://finance.yahoo.com/quote/PLD/history/)
- [BlackRock FCF Yield — FinanceCharts](https://www.financecharts.com/stocks/BLK/value/fcf-yield)
- [NextEra Energy Statistics — StockAnalysis](https://stockanalysis.com/stocks/nee/statistics/)
