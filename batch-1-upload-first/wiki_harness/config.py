"""Load settings and resolve project paths.

Everything the harness reads or writes is addressed through this module, so the
separation between originals (vault/raw), reviewed notes (vault/wiki), machine
state (state/), and saved outputs (runs/) lives in one place.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = ROOT / "config" / "settings.json"


class Settings:
    def __init__(self, data: dict):
        self.data = data
        # Environment overrides make it easy to try another model without editing files.
        self.model = os.environ.get("WIKI_MODEL", data["model"])
        self.embed_model = os.environ.get("WIKI_EMBED_MODEL", data["embed_model"])
        self.ollama_url = os.environ.get("WIKI_OLLAMA_URL", data["ollama_url"]).rstrip("/")
        self.num_ctx = int(data["num_ctx"])
        self.keep_alive = data.get("keep_alive", "15m")
        self.temperature = data["temperature"]
        self.chunk_chars = int(data["chunk_chars"])
        self.chunk_overlap = int(data["chunk_overlap_chars"])
        self.top_k = int(data["top_k"])
        self.max_per_file = int(data.get("max_passages_per_file", 0))
        self.ask_context_chars = int(data["ask_context_chars"])
        self.ingest_source_chars = int(data["ingest_source_chars"])
        self.chat_history_turns = int(data["chat_history_turns"])
        self.chat_history_chars = int(data["chat_history_chars"])
        p = data["paths"]
        self.vault = ROOT / p["vault"]
        self.raw = ROOT / p["raw"]
        self.wiki = ROOT / p["wiki"]
        self.index_md = ROOT / p["index_md"]
        self.catalog_md = ROOT / p["catalog_md"]
        self.plan = ROOT / p["plan"]
        self.instructions = ROOT / p["instructions"]
        self.state = ROOT / p["state"]
        self.runs = ROOT / p["runs"]
        self.drafts = ROOT / p["drafts"]

    # Machine files live outside the vault so Obsidian only shows curated notes.
    @property
    def chunks_file(self) -> Path:
        return self.state / "index" / "chunks.jsonl"

    @property
    def embeddings_file(self) -> Path:
        return self.state / "index" / "embeddings.json"

    @property
    def catalog_file(self) -> Path:
        return self.state / "catalog.json"

    def rel(self, path: Path) -> str:
        """Project-relative POSIX path used in citations and saved records."""
        try:
            return Path(path).resolve().relative_to(ROOT).as_posix()
        except ValueError:
            return str(path)

    def vault_rel(self, path: Path) -> str:
        """Vault-relative path, the form Obsidian links use."""
        return Path(path).resolve().relative_to(self.vault.resolve()).as_posix()


def load_settings() -> Settings:
    with open(SETTINGS_FILE, encoding="utf-8") as f:
        return Settings(json.load(f))


def read_instruction(settings: Settings, name: str) -> str:
    """Instructions are plain Markdown files the harness loads per mode.

    The model never reads project files on its own; the harness puts the text
    of the relevant file into the system prompt.
    """
    path = settings.instructions / name
    if not path.exists():
        raise FileNotFoundError(f"Missing instruction file: {settings.rel(path)}")
    return path.read_text(encoding="utf-8").strip()
