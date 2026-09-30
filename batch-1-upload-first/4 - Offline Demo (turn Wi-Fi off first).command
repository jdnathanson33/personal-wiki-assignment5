#!/bin/bash
# The graded offline run. Turn Wi-Fi OFF first, then double-click this in Finder (about 20 min).
cd "$(dirname "$0")"
./scripts/offline_demo.sh
echo; echo "OFFLINE DEMO DONE. Take a screenshot of this window, turn Wi-Fi back on, and tell Claude 'done'."
read -p "Press Return to close."
