"""Dynamically load optional modules."""
from __future__ import annotations

import importlib
from types import ModuleType
from typing import Iterable, List


def build(mod_names: Iterable[str]) -> List[ModuleType]:
    mods = []
    for name in mod_names:
        mods.append(importlib.import_module(name))
    return mods
