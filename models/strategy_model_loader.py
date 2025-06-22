"""Load reinforcement models."""
from __future__ import annotations

from pathlib import Path


def load(path: str | Path) -> str:
    return f"strategy model {path}"
