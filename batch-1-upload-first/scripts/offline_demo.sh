#!/bin/bash
# Offline demonstration. Turn Wi-Fi OFF (and unplug Ethernet) first, then:
#   cd ~/Documents/personal-wiki-assignment5 && ./scripts/offline_demo.sh
# Every command starts a fresh CLI process; the transcript is saved to evidence/offline/.
set -u
cd "$(dirname "$0")/.."
export PYTHONUNBUFFERED=1
STAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p evidence/offline
OUT="evidence/offline/offline-demo-$STAMP.txt"
exec > >(tee -a "$OUT") 2>&1

run() { echo; echo "================================================================"; echo "\$ $*"; echo "================================================================"; "$@"; }

echo "Offline demo started $(date)"
NET=$(python3 -c 'import sys; sys.path.insert(0,"."); from wiki_harness.system import internet_status as s; print(s())')
echo "Internet check: $NET"
if [ "$NET" != "offline" ] && [ "${1:-}" != "--rehearsal" ]; then
  echo "!! The internet is still reachable. Turn Wi-Fi off and run this again (or pass --rehearsal for a practice run)."
  exit 1
fi
run networksetup -getairportpower en0
run ping -c 1 -t 2 github.com

# Restart the local model server so nothing cached from an online session is reused.
echo; echo "Restarting Ollama ..."
osascript -e 'quit app "Ollama"' 2>/dev/null; pkill -x ollama 2>/dev/null; sleep 2
open -a Ollama; for i in $(seq 1 30); do sleep 1; curl -s http://127.0.0.1:11434/api/version >/dev/null && break; done

run ./wiki --help
run ./wiki status --save
run ./wiki ingest vault/raw/assignments/pacman-dqn-README.md --force
run ./wiki lint
run ./wiki search "hardware used to train the agent" -k 4
run ./wiki eval --retrieval-only
run ./wiki eval
run ./wiki chat --script tests/mode_checks_chat.txt
run ./wiki ask "Did I train the Pac-Man agent on a GPU?"
run ./wiki measure
echo; echo "Offline demo finished $(date). Transcript: $OUT"
