#!/bin/bash
# Double-click in Finder. Re-checks retrieval and chat after Claude's fixes (still ONLINE, about 8 min).
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1
OUT="evidence/rehearsal/fix-check-$(date +%Y%m%d-%H%M%S).txt"
{
run() { echo; echo "================================================================"; echo "\$ $*"; echo "================================================================"; "$@"; }
run ./wiki ingest --index-only
run ./wiki eval --retrieval-only
run ./wiki eval --only T3
run ./wiki chat --script tests/mode_checks_chat.txt
echo; echo "FIX CHECK DONE. Tell Claude 'done'."
} 2>&1 | tee "$OUT"
read -p "Press Return to close."
