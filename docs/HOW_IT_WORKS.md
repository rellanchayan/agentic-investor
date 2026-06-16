# How it works — the big picture

This is a robot investor. It uses pretend money ("paper money") on a real-market simulator
called Alpaca. It tries to act like a sensible, patient human investor: buy good companies at
fair prices, hold them for a long time, and beat the overall market (SPY) over the years.

You don't have to do anything. It runs itself on a schedule. Everything it thinks and does is
written down in plain English so you can read along.

New to investing? Read `GLOSSARY.md` first — it explains every term used here.

## The team (each is a small specialist)
Think of it as a tiny investment firm:
- **Market-Weather Analyst** — every morning, checks the overall mood of the market and sets a
  posture: lean in (opportunistic), normal, or careful (cautious).
- **Research Analyst** — studies one company at a time and writes a deep, **sourced** report (a
  "thesis"): what the business is, why it's strong, what it's worth, and what would make us sell.
- **Candidate Scout** — once a week, looks for new high-quality companies to study.
- **Portfolio Manager** — the decision-maker. Each morning it reads the research and decides:
  buy a little, trim, sell, or (usually) just hold.
- **Risk Officer** — an independent checker. Before any order is sent, it says PASS or VETO.
- **Journal Writer** — after the close, writes the honest story of the day from what really happened.
- **Learning Coach** — turns experience into permanent lessons, and very carefully tweaks settings.

Behind them, plain code does the mechanical work: talking to Alpaca, enforcing the hard rules
(the "constitution"), and scoring us against SPY.

## The rhythm
- **Every weekday morning** (after the market opens): review everything, decide, place patient
  limit orders, and write `docs/decisions/<date>.md` explaining exactly what it did and why.
- **Every weekday after the close**: find out what actually filled, write an honest journal
  (`docs/journal/<date>.md`) and trade cards, and learn one small thing.
- **Every Saturday**: deep research — refresh the company reports, hunt for new names, and update
  the playbook of lessons.

## The rules it can never break (the "constitution")
- Paper money only. No options, shorts, margin, or crypto. Only safe LIMIT orders.
- Spend at most **$5,000 of new money per day** (so it buys slowly and never bets it all at once).
- Never more than 25% in one company, never more than 8 companies, never more than the cash on hand.
- Every purchase must be backed by a written, sourced thesis. No reason = no trade.

## Where to look
- `docs/decisions/<date>.md` — what it bought/sold/held today, at what price, and why.
- `docs/research/<TICKER>.md` — the deep report on each company (and post-mortems when we sell).
- `docs/journal/<date>.md` — the honest end-of-day recap.
- `docs/macro/<date>.md` — the day's market-weather read.
- `docs/PLAYBOOK.md` — the growing list of lessons it follows.
- `docs/STRATEGY.md` — exactly how it decides. `docs/RISK.md` — all the safety rules.

## How to stop it
Create a file named `.HALT_TRADING` in the project folder (or run the `/halt` skill). While that
file exists, it places no new orders. Only you can remove it.
