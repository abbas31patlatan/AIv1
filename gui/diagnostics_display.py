"""Display diagnostics information."""
from __future__ import annotations


def render(info: dict) -> str:
    return " | ".join(f"{k}:{v}" for k, v in info.items())
