"""Check and toggle feature flags."""
from __future__ import annotations

from config.developer_flags import flags


def enabled(option: str) -> bool:
    return getattr(flags, option, False)
