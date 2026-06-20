# NVIDIA Corporation (NVDA) — Research Thesis

*As of 2027-Q1 (latest reported quarter ended Apr 26 2026). Price as of 2026-06-20. Refresh due 2026-09-18.*

## What the company does (plain English)
NVIDIA makes the chips and systems that train and run artificial-intelligence models.
Its **Data Center** business — GPUs (Blackwell), plus the networking (NVLink, Spectrum-X,
InfiniBand) and software (CUDA) that tie them together — is now ~92% of the company. The
buyers are the big cloud companies (Microsoft, Amazon, Google, Meta), specialist "AI clouds,"
governments, and enterprises. NVIDIA also sells gaming GPUs (GeForce), professional graphics,
and automotive chips. It earns money by selling very high-performance hardware at very high
margins, while its CUDA software keeps developers locked into its platform.

## Why it has a moat (wide)
- **CUDA software lock-in:** nearly two decades of developer tools and libraries make NVIDIA
  the default platform for AI. The switching cost is the software, not just the chip.
- **Full-stack systems:** NVIDIA sells integrated compute + networking + software, which
  merchant-silicon rivals cannot easily match.
- **Scale and brand:** it is the name AI buyers reach for first, funding the R&D that keeps it ahead.

## The key numbers (all cited)
- **Revenue growth:** FY2024 $60.922B → FY2025 $130.497B (+114%) → **FY2026 $215.938B (+65%)**;
  latest quarter Q1 FY2027 **+85% YoY** to a record $81.6B. [NVIDIA IR / SEC 8-K]
- **Gross margin:** **71.1%** GAAP for FY2026; **74.9%** in Q1 FY2027. [NVIDIA IR / SEC 8-K]
- **Profit:** FY2026 GAAP net income **$120.067B**, diluted EPS **$4.90**; ~55.6% net margin.
- **Free cash flow:** FY2026 operating cash flow **$102.718B** minus capex **$6.042B** ≈
  **$96.676B FCF**. Positive and enormous. [NVIDIA IR]
- **Balance sheet:** **net cash** — $62.556B cash & marketable securities vs only $8.468B debt
  at Jan 25 2026, so net-debt/EBITDA is effectively negative (~−0.4x). [NVIDIA IR]
- **Capital returns:** dividend raised from $0.01 to $0.25/quarter and +$80B buyback
  authorization in Q1 FY2027; ~$20B returned that quarter. [SEC 8-K]
- **Price/trend:** $210.38 close, ~11% above the 200-day average, just above the 50-day. [Alpaca]

## Fair value (how I got it)
Computed with `code/valuation.py`, two methods blended:
- **P/E:** TTM diluted EPS ≈ **$6.53** (FY2026 $4.90 − Q1 FY26 $0.76 + Q1 FY27 $2.39) ×
  **28 / 38 / 48**. The multiples are a premium but below NVDA's own recent history,
  reflecting 65–85% growth and 71%+ gross margins, discounted for cycle and concentration risk.
- **FCF yield:** FCF/share (~$4.92 TTM) at **3.0% / 2.4% / 1.8%** target yields.

**Fair value band: low $173 · base $227 · high $293.**
At $210.38 that is a **~7% margin of safety** to the base case — "fair, leaning cheap."

## The real risks (as hard as the bull case)
- **Customer concentration:** ~half of Data Center revenue is a few hyperscalers; if they cut
  AI capex, revenue can drop quickly.
- **AI-cycle / digestion:** today's growth assumes the AI build-out keeps going. Semis are
  cyclical; an overbuild or pause would hit both earnings and the rich multiple.
- **Valuation:** ~32x TTM EPS and a low FCF yield leave little room for disappointment.
- **China / export controls:** already caused a $4.5B H20 charge in Q1 FY2026; rules can tighten.
- **Competition:** AMD MI-series and custom hyperscaler chips (TPU, Trainium, Maia) target the margins.
- **Supply chain:** dependent on TSMC for leading-edge manufacturing.

## Sell triggers (what would break the thesis)
1. Revenue declines YoY for **two consecutive quarters**.
2. GAAP gross margin **below 60% for two consecutive quarters**.
3. Data Center revenue declines **sequentially two quarters** with no temporary export-control cause.
4. Balance sheet flips to meaningful net debt (**net-debt/EBITDA > 1.0x**).
5. A major hyperscaler publicly shifts most new AI training to in-house or competitor silicon.
6. Any serious accounting red flag, restatement, or pull-forward/channel-stuffing evidence.
7. Price runs far above fair value (**> ~$293**) with no durable earnings upgrade — trim on overvaluation.

## Conviction: 4 / 5
A wide-moat, cash-gushing leader of the defining technology build-out, available near its
50-day average with a modest margin of safety. Held back from a 5 by genuine cyclicality,
customer concentration, and a valuation that needs continued elite execution.

## Sources
- [NVIDIA Q4 & Fiscal 2026 results (IR)](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)
- [NVIDIA Q1 FY2027 press release (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm)
- [NVIDIA Q1 FY2026 CFO commentary (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581025000115/q1fy26cfocommentary.htm)
- [NVIDIA Q4 & FY2024 results (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000028/q4fy24pr.htm)
- Price/trend: Alpaca paper market-data feed
