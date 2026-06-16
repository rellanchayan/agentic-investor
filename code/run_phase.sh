#!/usr/bin/env bash
# run_phase.sh — the DETERMINISTIC, mechanical part of each routine.
#
# The judgment (research, the buy/sell/hold decision, the journal, the lessons) is
# done by the Claude agents that the skills call. This script only does the steps
# that are identical every time, so they never drift.
#
#   bash code/run_phase.sh deps        # make sure python deps are installed
#   bash code/run_phase.sh morning     # gate, then reconcile + snapshot + build context
#   bash code/run_phase.sh eod         # reconcile fills + snapshot + day summary + record buys
#   bash code/run_phase.sh weekly      # refresh prices + screen the watchlist + calibration report
#
# Exit codes for `morning`: 0 = PROCEED (context built), 3 = EXIT (closed/halted/down).
set -uo pipefail
cd "$(dirname "$0")/.."

if [ -x ".venv/bin/python" ]; then PY=".venv/bin/python"; else PY="python3"; fi

ensure_deps() {
  if ! "$PY" -c "import alpaca, dotenv" >/dev/null 2>&1; then
    if ! "$PY" -m pip install -q -r requirements.txt >/dev/null 2>&1; then
      python3 -m venv .venv
      PY=".venv/bin/python"
      "$PY" -m pip install -q -r requirements.txt
    fi
  fi
}

PHASE="${1:-}"
ensure_deps

case "$PHASE" in
  deps)
    echo "deps ok"
    ;;

  morning)
    echo "== MORNING =="
    # Cheap safety gate first. If the market is closed / halted / Alpaca is down, stop here.
    "$PY" code/preflight.py
    RC=$?
    if [ "$RC" -ne 0 ]; then
      echo "preflight says do nothing today (code $RC)"
      exit $RC
    fi
    "$PY" code/alpaca_client.py --reconcile     # close the books on yesterday's still-open limits
    "$PY" code/alpaca_client.py --account        # writes state/account.json
    "$PY" code/alpaca_client.py --positions      # refresh portfolio.json + equity history
    "$PY" code/context.py                        # build state/day/<today>/context.json
    exit 0
    ;;

  eod)
    echo "== END OF DAY =="
    "$PY" code/alpaca_client.py --reconcile      # the ONLY source of fill truth
    "$PY" code/alpaca_client.py --positions      # snapshot equity for the history
    "$PY" code/metrics.py --summary              # write state/runs/<today>-summary.json
    "$PY" code/metrics.py || true                # long-run scorecard vs SPY (never blocks)
    "$PY" code/calibration.py --record           # log conviction of any new filled buys
    ;;

  weekly)
    echo "== WEEKLY RESEARCH =="
    "$PY" code/alpaca_client.py --positions      # fresh prices for calibration mark-to-market
    "$PY" code/screen.py                         # liquidity + trend snapshot of the watchlist
    "$PY" code/calibration.py --report           # are high-conviction buys actually winning?
    ;;

  *)
    echo "usage: bash code/run_phase.sh {deps|morning|eod|weekly}" >&2
    exit 2
    ;;
esac
