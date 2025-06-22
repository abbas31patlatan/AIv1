"""Wrapper module orchestrating key components."""
from __future__ import annotations

from core.ai_core import AICore


def run(text: str) -> str:
    core = AICore()
    return core.interact(text)
