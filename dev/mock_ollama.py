"""DEVELOPMENT ONLY: a fake Ollama server used to test the harness plumbing in an
environment without the real model. It is never used for evidence; every saved
record names the model that answered, and the real runs use gemma4 via Ollama.
"""
import hashlib
import json
import math
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

MODEL = "gemma4:e2b-it-qat"


def fake_vec(text, dim=64):
    v = [0.0] * dim
    for w in re.findall(r"[a-z]+", text.lower()):
        h = int(hashlib.md5(w.encode()).hexdigest(), 16)
        v[h % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1
    return [x / n for x in v]


def reply_for(messages):
    sys_p = messages[0]["content"] if messages and messages[0]["role"] == "system" else ""
    user = messages[-1]["content"]
    if "Ingest instructions" in sys_p:
        return ("SUMMARY: This is a mock summary of the subject. It exists only to test the harness.\n"
                "DETAILS:\n- First mock detail from the excerpts [E1]\n- Second mock detail [E2]\n- Third detail [E1, E3]")
    if "Research rules" in sys_p:
        if "grade" in user.lower():
            return "INSUFFICIENT EVIDENCE: the passages do not state a grade."
        m = re.search(r"\[S1\] \(.*?\)\n(.+?)(?:\n|$)", user)
        return f"Mock answer based on the first passage: {m.group(1)[:120] if m else ''} [S1]"
    if "reply with a title only" in sys_p.lower():
        return "Mock Auto Title"
    return "Mock chat reply." + (" Per your notes [N1]." if "[N1]" in user else "")


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, obj):
        b = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path == "/api/version":
            return self._json({"version": "mock-0.0"})
        if self.path == "/api/tags":
            return self._json({"models": [
                {"name": MODEL, "model": MODEL, "size": 4.3e9, "digest": "mockdigest000000",
                 "details": {"parameter_size": "4.6B", "quantization_level": "Q4_0", "family": "gemma4"}},
                {"name": "embeddinggemma:latest", "model": "embeddinggemma:latest", "size": 6.2e8, "digest": "mockembed",
                 "details": {"parameter_size": "300M", "quantization_level": "BF16"}}]})
        if self.path == "/api/ps":
            return self._json({"models": []})
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/api/embed":
            return self._json({"embeddings": [fake_vec(t) for t in body["input"]]})
        if self.path == "/api/show":
            return self._json({"details": {}})
        if self.path == "/api/chat":
            text = reply_for(body["messages"])
            final = {"model": MODEL, "done": True, "done_reason": "stop", "load_duration": 1e8,
                     "prompt_eval_count": 100, "prompt_eval_duration": 1e9, "eval_count": 20, "eval_duration": 2e9}
            if body.get("stream"):
                self.send_response(200)
                self.send_header("Content-Type", "application/x-ndjson")
                self.end_headers()
                for w in re.findall(r"\S+\s*", text):
                    self.wfile.write((json.dumps({"message": {"content": w}, "done": False}) + "\n").encode())
                self.wfile.write((json.dumps({**final, "message": {"content": ""}}) + "\n").encode())
                return
            return self._json({**final, "message": {"role": "assistant", "content": text}})
        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 11435), H).serve_forever()
