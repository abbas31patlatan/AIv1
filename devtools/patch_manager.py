"""Apply patches to modules dynamically."""
from __future__ import annotations

import importlib
from types import ModuleType


def apply_patch(module: str, name: str, value) -> None:
    mod: ModuleType = importlib.import_module(module)
    setattr(mod, name, value)
