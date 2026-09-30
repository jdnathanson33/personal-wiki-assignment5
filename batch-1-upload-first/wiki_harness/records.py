"""Save every run so a reader can inspect results without rerunning the model."""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from .system import internet_status


def stamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def slug(text: str, n: int = 6) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())[:n]
    return "-".join(words) or "run"


def run_context(settings, client, mode: str) -> dict:
    """Identity block stored at the top of every saved record."""
    ctx = {"mode": mode, "execution": "local", "model": client.model if client else None,
           "embed_model": client.embed_model if client else None,
           "internet_at_run_time": internet_status(), "timestamp": datetime.now().isoformat(timespec="seconds")}
    try:
        ctx["runtime"] = f"ollama {client.version()}"
        for m in client.list_models():
            if m.get("name") in (client.model, client.model + ":latest"):
                d = m.get("details", {})
                ctx["model_digest"] = m.get("digest", "")[:12]
                ctx["model_quantization"] = d.get("quantization_level")
                ctx["model_parameter_size"] = d.get("parameter_size")
                ctx["model_family"] = d.get("family")
    except Exception as e:
        ctx["runtime"] = f"unavailable ({str(e).splitlines()[0]})"
    return ctx


def save(folder: Path, name: str, record: dict, markdown: Optional[str] = None) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    base = folder / name
    base.with_suffix(".json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if markdown is not None:
        base.with_suffix(".md").write_text(markdown, encoding="utf-8")
    return base.with_suffix(".json")
