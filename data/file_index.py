"""Index file paths for quick lookup."""
from __future__ import annotations

from pathlib import Path


class FileIndex:
    """Map names to file paths."""

    def __init__(self) -> None:
        self.index: dict[str, Path] = {}

    def add(self, name: str, path: str | Path) -> None:
        self.index[name] = Path(path)

    def resolve(self, name: str) -> Path | None:
        return self.index.get(name)
