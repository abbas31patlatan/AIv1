"""Path helper functions."""

from __future__ import annotations

from pathlib import Path


def resolve_data_path(base: str | Path) -> Path:
    """Ensure the data directory exists and return the absolute path."""
    path = Path(base).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path
