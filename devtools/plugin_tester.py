"""Framework for running plugin tests."""
from __future__ import annotations

from types import ModuleType


def run_test(plugin: ModuleType) -> bool:
    return hasattr(plugin, 'run')
