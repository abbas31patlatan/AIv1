"""File helper functions."""
from __future__ import annotations

from pathlib import Path


def touch(path: str | Path) -> None:
    Path(path).touch()
