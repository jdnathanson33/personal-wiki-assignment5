"""Minimal client for the local Ollama server (http://127.0.0.1:11434).

Only the Python standard library is used, so the harness has no pip
dependencies. Every call goes to localhost: nothing leaves the machine.
"""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from typing import Callable, Dict, List, Optional


class ModelUnavailable(RuntimeError):
    """Raised with a user-facing explanation when the local model can't be used."""


# Gemma 4 small models can emit an (empty) thought block even with thinking off.
_THOUGHT_PATTERNS = [
    re.compile(r"<think>.*?</think>", re.S),
    re.compile(r"<\|channel\|?>thought.*?<channel\|>", re.S),
    re.compile(r"<\|think\|>", re.S),
]


def strip_thoughts(text: str) -> str:
    for pat in _THOUGHT_PATTERNS:
        text = pat.sub("", text)
    return text.strip()


class OllamaClient:
    def __init__(self, base_url: str, model: str, embed_model: str, num_ctx: int, keep_alive: str = "15m"):
        self.base_url = base_url
        self.model = model
        self.embed_model = embed_model
        self.num_ctx = num_ctx
        self.keep_alive = keep_alive

    # ---------- low-level HTTP ----------
    def _request(self, path: str, payload: Optional[dict] = None, timeout: float = 600):
        url = self.base_url + path
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"},
                                     method="POST" if payload is not None else "GET")
        try:
            return urllib.request.urlopen(req, timeout=timeout)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code == 404 and "not found" in body.lower():
                raise ModelUnavailable(
                    f"Ollama is running but a model is missing ({body.strip()}).\n"
                    f"  While online, run:  ollama pull {self.model}  and  ollama pull {self.embed_model}")
            raise ModelUnavailable(f"Ollama returned HTTP {e.code}: {body.strip()}")
        except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
            raise ModelUnavailable(
                f"Cannot reach the local Ollama server at {self.base_url} ({e}).\n"
                "  Start it with the Ollama app, or run:  ollama serve")

    # ---------- status ----------
    def version(self) -> str:
        with self._request("/api/version", timeout=5) as r:
            return json.load(r).get("version", "?")

    def list_models(self) -> List[dict]:
        with self._request("/api/tags", timeout=5) as r:
            return json.load(r).get("models", [])

    def running(self) -> List[dict]:
        with self._request("/api/ps", timeout=5) as r:
            return json.load(r).get("models", [])

    def show(self, model: str) -> dict:
        with self._request("/api/show", {"model": model}, timeout=30) as r:
            return json.load(r)

    def has_model(self, name: str) -> bool:
        names = {m.get("name") for m in self.list_models()} | {m.get("model") for m in self.list_models()}
        return name in names or (name + ":latest") in names

    # ---------- generation ----------
    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.2,
             on_token: Optional[Callable[[str], None]] = None, max_tokens: int = 700) -> dict:
        """Send a message list to Gemma and return {'text', 'stats'}.

        If on_token is given, tokens are streamed to it as they arrive (useful on
        a CPU-only machine where a full answer takes a while).
        """
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": on_token is not None,
            "think": False,
            "keep_alive": self.keep_alive,
            "options": {"temperature": temperature, "num_ctx": self.num_ctx, "num_predict": max_tokens},
        }
        t0 = time.time()
        try:
            resp = self._request("/api/chat", payload)
        except ModelUnavailable as e:
            # Older runtimes reject the "think" field; retry once without it.
            if "think" in str(e).lower():
                payload.pop("think")
                resp = self._request("/api/chat", payload)
            else:
                raise
        parts: List[str] = []
        final: dict = {}
        with resp:
            if on_token is None:
                final = json.load(resp)
                parts.append(final.get("message", {}).get("content", ""))
            else:
                in_thought = False
                for line in resp:
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    piece = obj.get("message", {}).get("content", "")
                    if piece:
                        parts.append(piece)
                        # Hide any thought markup from the live stream.
                        if "<think>" in piece or "<|channel" in piece:
                            in_thought = True
                        if not in_thought:
                            on_token(piece)
                        if "</think>" in piece or "<channel|>" in piece:
                            in_thought = False
                    if obj.get("done"):
                        final = obj
        wall = time.time() - t0
        text = strip_thoughts("".join(parts))
        ns = 1e9
        stats = {
            "model": final.get("model", self.model),
            "wall_seconds": round(wall, 2),
            "load_seconds": round(final.get("load_duration", 0) / ns, 2),
            "prompt_tokens": final.get("prompt_eval_count"),
            "prompt_seconds": round(final.get("prompt_eval_duration", 0) / ns, 2),
            "output_tokens": final.get("eval_count"),
            "output_seconds": round(final.get("eval_duration", 0) / ns, 2),
            "tokens_per_second": round(final["eval_count"] / (final["eval_duration"] / ns), 2)
            if final.get("eval_count") and final.get("eval_duration") else None,
            "done_reason": final.get("done_reason"),
        }
        return {"text": text, "stats": stats}

    # ---------- embeddings ----------
    def embed(self, texts: List[str], batch: int = 16) -> List[List[float]]:
        out: List[List[float]] = []
        for i in range(0, len(texts), batch):
            payload = {"model": self.embed_model, "input": texts[i:i + batch], "keep_alive": self.keep_alive}
            with self._request("/api/embed", payload) as r:
                out.extend(json.load(r)["embeddings"])
        return out
