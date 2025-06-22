"""Verify model files exist."""
from __future__ import annotations

from pathlib import Path


def check(path: str | Path) -> bool:
    return Path(path).exists()
