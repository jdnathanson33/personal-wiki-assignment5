"""Device facts, internet check, and memory measurement for evidence records."""
from __future__ import annotations

import os
import platform
import shutil
import socket
import subprocess
from pathlib import Path
from typing import Optional


def internet_status(timeout: float = 1.5) -> str:
    """'offline' if public internet is unreachable, else 'ONLINE'.

    Tries TCP connections to two public DNS resolvers; saved with every run so
    the offline demonstration is visible in the evidence itself.
    """
    for host, port in (("1.1.1.1", 443), ("8.8.8.8", 53), ("github.com", 443)):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return "ONLINE"
        except OSError:
            continue
    return "offline"


def _run(cmd) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def device_info() -> dict:
    info = {"os": platform.platform(), "python": platform.python_version(), "machine": platform.machine()}
    if platform.system() == "Darwin":
        info["macos"] = _run(["sw_vers", "-productVersion"])
        info["model"] = _run(["sysctl", "-n", "hw.model"])
        info["cpu"] = _run(["sysctl", "-n", "machdep.cpu.brand_string"]) or _run(["sysctl", "-n", "hw.model"])
        info["cpu_cores"] = _run(["sysctl", "-n", "hw.physicalcpu"]) + " physical / " + _run(["sysctl", "-n", "hw.logicalcpu"]) + " logical"
        mem = _run(["sysctl", "-n", "hw.memsize"])
        info["ram_gb"] = round(int(mem) / 1024 ** 3, 1) if mem.isdigit() else None
        gpu = _run(["system_profiler", "SPDisplaysDataType"])
        info["gpu"] = "; ".join(l.strip() for l in gpu.splitlines() if "Chipset Model" in l or "VRAM" in l)
        vm = _run(["vm_stat"])
        page = 4096
        free = 0
        for line in vm.splitlines():
            if "page size of" in line:
                page = int("".join(ch for ch in line.split("page size of")[1] if ch.isdigit()) or 4096)
            if line.startswith(("Pages free", "Pages inactive", "Pages speculative")):
                free += int(line.split(":")[1].strip().rstrip("."))
        info["available_memory_gb_approx"] = round(free * page / 1024 ** 3, 1) if free else None
    else:
        try:
            with open("/proc/meminfo") as f:
                m = dict(l.split(":", 1) for l in f)
            info["ram_gb"] = round(int(m["MemTotal"].split()[0]) / 1024 ** 2, 1)
            info["available_memory_gb_approx"] = round(int(m["MemAvailable"].split()[0]) / 1024 ** 2, 1)
        except Exception:
            pass
        info["cpu"] = platform.processor()
        info["cpu_cores"] = str(os.cpu_count())
    du = shutil.disk_usage(str(Path.home()))
    info["disk_free_gb"] = round(du.free / 1024 ** 3, 1)
    return info


def ollama_process_rss_mb() -> Optional[float]:
    """Resident memory of all Ollama processes (server + model runner), in MB."""
    out = _run(["ps", "-axo", "rss=,comm="])
    total = 0
    for line in out.splitlines():
        parts = line.strip().split(None, 1)
        if len(parts) == 2 and "ollama" in parts[1].lower():
            try:
                total += int(parts[0])
            except ValueError:
                pass
    return round(total / 1024, 1) if total else None
