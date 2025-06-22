"""Track version numbers of dependencies."""
from __future__ import annotations

import importlib


def get_version(package: str) -> str | None:
    try:
        mod = importlib.import_module(package)
        return getattr(mod, '__version__', None)
    except Exception:
        return None
