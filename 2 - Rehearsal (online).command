#!/bin/bash
# Double-click in Finder. Practice run of every test while still ONLINE (not the graded offline run).
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1
mkdir -p evidence/rehearsal
OUT="evidence/rehearsal/rehearsal-$(date +%Y%m%d-%H%M%S).txt"
{
run() { echo; echo "================================================================"; echo "\$ $*"; echo "================================================================"; "$@"; }
run ./wiki ingest --index-only
run ./wiki lint
run ./wiki ingest vault/raw/assignments/pacman-dqn-README.md
run ./wiki search "hardware used to train the agent" -k 4
run ./wiki eval
run ./wiki chat --script tests/mode_checks_chat.txt
run ./wiki ask "Did I train the Pac-Man agent on a GPU?"
run ./wiki measure
echo; echo "REHEARSAL DONE. Tell Claude 'done'."
} 2>&1 | tee "$OUT"
read -p "Press Return to close."
