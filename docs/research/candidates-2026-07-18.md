# Candidate Scout — 2026-07-18

*Paper money only. No orders. These are watchlist proposals only — no thesis exists yet
for any of these names. A full thesis (cited numbers, fair-value range, sell triggers) must
be written and stored in `state/theses/<TICKER>.json` before any buy is possible.*

---

## Gap Analysis

After reviewing the current watchlist (29 names across 8 sectors), three structural holes stood out:

1. **Communication / media** has only DIS, which is below both moving averages and down 13.9% over
   six months. No exposure to digital advertising or social networking.
2. **Real estate** is completely absent from the watchlist.
3. **Health care** covers managed care (UNH), pharma (JNJ, LLY, ABBV), but nothing in
   life-sciences instruments and services — a distinct sub-sector with very different
   cash-flow characteristics.

---

## Proposed Additions

### 1. META — Meta Platforms
**Sector:** Communication

Meta operates Facebook, Instagram, and WhatsApp — the world's largest social graph — monetising
through digital advertising. Q1 2026 revenue was $56.3 billion (+33% YoY); TTM free cash flow
approximately $48 billion. Net income Q1 2026: $26.8 billion.

**Moat:** Network effects at massive scale. Facebook alone has ~3 billion daily active users.
Morningstar: Wide Moat. Advertisers cannot reach this audience at scale anywhere else.

**Liquidity:** Market cap ~$1.7 trillion; daily volume ~21 million shares. No concern.

**Red flag to watch:** 2026 capex guidance $125–145 billion (AI infrastructure) is enormous and
compresses near-term FCF. Research analyst should assess whether this is durable competitive
investment or empire-building.

*Sources: Meta Q1 2026 8-K (StockTitan); GuruFocus FCF; CompaniesMarketCap*

---

### 2. AMT — American Tower Corporation
**Sector:** Real Estate

American Tower owns and leases space on ~150,000 communications towers and data-centre sites
across the US, Europe, Latin America, Africa, and Asia. Carriers sign multi-year,
inflation-linked contracts to place antennas on these towers.

**Moat:** Essential infrastructure with local-market concentration. Tower permitting is slow and
expensive; carriers have no practical alternative but to renew leases. Classic switching-cost /
asset-scarcity moat.

**Financials:** Market cap ~$84–86 billion. Q1 2026 AFFO $1.324 billion (+2.6% YoY). TTM FCF
~$3.8 billion. Revenue growing 3–5% on a cash basis.

**Red flag to watch:** Very high leverage (~$45 billion total debt, debt/equity ~4.45). Structurally
normal for infrastructure REITs, but interest-rate sensitive with little margin for AFFO decline.
Research analyst must model debt-service coverage carefully before writing a buy thesis.

*Sources: AMT Q1 2026 results (BusinessWire); StockAnalysis statistics; FinanceCharts FCF*

---

### 3. TMO — Thermo Fisher Scientific
**Sector:** Health care (life-sciences instruments)

Thermo Fisher manufactures analytical instruments, reagents, consumables, and software that
pharma, biotech, academic, and government labs depend on for research and production. Q1 2026
revenue $11.01 billion (+6% YoY); 2026 revenue guidance ~$47–48 billion.

**Moat:** High switching costs reinforced by consumables lock-in. Once a drug-maker validates a
Thermo Fisher reagent in a regulated manufacturing process, switching requires re-validating every
process — a multi-year, multi-million-dollar undertaking. GuruFocus Moat Score: 8 (Wide Moat).

**Financials:** Market cap ~$198 billion. Q1 2026 FCF ~$830 million (after $370M capex).
ROIC approximately 7.6–8.9%.

**Red flag to watch:** 2023–2024 post-COVID hangover (pandemic testing/vaccine revenue evaporated).
Revenue recovering at mid-single digits; research analyst should confirm growth is durable,
not a base-effect. Also assess whether acquisitions (PPD, PPI) diluted organic ROIC.

*Sources: Thermo Fisher Q1 2026 IR press release; GuruFocus moat score; StockAnalysis market cap;
Q1 2026 earnings transcript (Motley Fool)*

---

## Names Considered but Not Proposed

- **AXP** (American Express): Would add a fourth payments/credit name; sector already has V, MA, JPM. Deprioritised — no new sector coverage.
- **DE** (Deere): Would add to industrials, which already has CAT, HON, UNP. Deprioritised similarly.
- **ORCL** (Oracle): Technology already has seven names. Worth revisiting in a future cycle.

---

## Summary

| Ticker | Sector | Moat Type | Market Cap | TTM FCF | Key Risk |
|--------|--------|-----------|-----------|---------|----------|
| META | Communication | Network effects | ~$1.7T | ~$48B | AI capex surge |
| AMT | Real Estate | Asset scarcity / switching | ~$85B | ~$3.8B | High leverage |
| TMO | Health care | Switching costs | ~$198B | ~$3.3B+ | Post-COVID growth recovery |

All three added to `state/watchlist.txt` and `state/sectors.json`. Next step for any of these is
a full research-analyst thesis before they can be considered for purchase.
