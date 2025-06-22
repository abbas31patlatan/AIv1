"""Simple module reload helper."""
from __future__ import annotations

import importlib


def reload(module_name: str) -> None:
    importlib.reload(importlib.import_module(module_name))
