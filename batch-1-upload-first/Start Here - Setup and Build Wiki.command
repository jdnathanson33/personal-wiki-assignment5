#!/bin/bash
# Double-click this file in Finder. It runs the one-time setup, then builds the wiki.
cd "$(dirname "$0")"
export PYTHONUNBUFFERED=1
./scripts/setup_mac.sh || { echo; echo "Setup stopped. Tell Claude what the last lines say."; read -p "Press Return to close."; exit 1; }
echo; echo "== Building the wiki with local Gemma (30-60 min). Leave this window open."
./wiki ingest vault/raw 2>&1 | tee "evidence/setup/first-ingest.log"
echo; echo "ALL DONE. Tell Claude 'done'."
read -p "Press Return to close."
