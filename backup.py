"""Utility for persisting memory to disk."""

from __future__ import annotations

import asyncio
from pathlib import Path

from config.settings import settings
from utils.json_handler import save_json
from utils.path_resolver import resolve_data_path
from memory_ import Memory


class BackupManager:
    """Persist memory contents at regular intervals."""

    def __init__(self, memory: Memory, data_dir: str | Path | None = None) -> None:
        self.memory = memory
        self.path = resolve_data_path(data_dir or settings.data_path) / "memory.json"

    async def backup(self) -> None:
        entries = {eid: entry.text for eid, entry in self.memory._entries.items()}
        save_json(self.path, entries)
