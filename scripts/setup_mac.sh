#!/bin/bash
# One-time setup on the Mac (run while ONLINE). Logs everything to evidence/setup/.
#   cd ~/Documents/personal-wiki-assignment5 && ./scripts/setup_mac.sh
set -u
cd "$(dirname "$0")/.."
mkdir -p evidence/setup
LOG="evidence/setup/setup-$(date +%Y%m%d-%H%M%S).log"
exec > >(tee -a "$LOG") 2>&1
MODEL=gemma4:e2b-it-qat
EMBED=embeddinggemma

echo "== Device"
sw_vers
echo "Chip/CPU: $(sysctl -n machdep.cpu.brand_string 2>/dev/null)  ($(sysctl -n hw.physicalcpu) physical / $(sysctl -n hw.logicalcpu) logical cores)"
echo "Model:    $(sysctl -n hw.model)"
echo "RAM:      $(( $(sysctl -n hw.memsize) / 1073741824 )) GB"
system_profiler SPDisplaysDataType 2>/dev/null | grep -E "Chipset Model|VRAM|Metal" | sed 's/^ */GPU:      /'
echo "Disk:     $(df -h ~ | tail -1 | awk '{print $4 " free of " $2}')"
MACOS_MAJOR=$(sw_vers -productVersion | cut -d. -f1)
if [ "$MACOS_MAJOR" -lt 14 ]; then
  echo "!! Ollama needs macOS 14 (Sonoma) or newer; this Mac has $(sw_vers -productVersion). Stop here and tell Claude."
  exit 1
fi

echo; echo "== Python"
if ! command -v python3 >/dev/null; then
  echo "!! python3 not found. Run:  xcode-select --install   then re-run this script."; exit 1
fi
python3 --version

echo; echo "== Ollama"
if ! command -v ollama >/dev/null && [ ! -d /Applications/Ollama.app ]; then
  echo "Ollama is not installed. Downloading the official app from https://ollama.com/download/Ollama.dmg ..."
  curl -fL --progress-bar -o /tmp/Ollama.dmg https://ollama.com/download/Ollama.dmg || { echo "!! download failed"; exit 1; }
  hdiutil attach -nobrowse -quiet /tmp/Ollama.dmg -mountpoint /tmp/ollama-dmg
  cp -R /tmp/ollama-dmg/Ollama.app /Applications/ && hdiutil detach -quiet /tmp/ollama-dmg
  echo "Installed /Applications/Ollama.app"
fi
OLLAMA=$(command -v ollama || echo /Applications/Ollama.app/Contents/Resources/ollama)
if ! curl -s http://127.0.0.1:11434/api/version >/dev/null; then
  echo "Starting Ollama ..."; open -a Ollama; for i in $(seq 1 30); do sleep 1; curl -s http://127.0.0.1:11434/api/version >/dev/null && break; done
fi
echo "Ollama: $("$OLLAMA" --version 2>&1 | tail -1)"

echo; echo "== Models (downloaded once, then used offline)"
"$OLLAMA" pull "$MODEL" && "$OLLAMA" pull "$EMBED" || { echo "!! pull failed"; exit 1; }
"$OLLAMA" list
"$OLLAMA" show "$MODEL" | head -25

echo; echo "== Harness check"
./wiki status --save
echo; echo "Setup log saved to $LOG"
