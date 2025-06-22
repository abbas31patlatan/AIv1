"""Text cleanup helpers."""
from __future__ import annotations

import re


def strip_urls(text: str) -> str:
    return re.sub(r"https?://\S+", "", text)
