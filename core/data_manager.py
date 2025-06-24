"""Data manager providing simple load/save helpers."""
from __future__ import annotations

from pathlib import Path
from utils.json_handler import load_json, save_json


class DataManager:
    """Load and save arbitrary JSON structures."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> dict | None:
        if self.path.exists():
            return load_json(self.path)
        return None

    def save(self, data: dict) -> None:
        save_json(self.path, data)
