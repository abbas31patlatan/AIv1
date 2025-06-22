"""Politeness filter to sanitize user input.

This module provides :func:`filter_text` which replaces any words deemed
impolite with a replacement string. The implementation is intentionally simple
and relies on a small hard coded list of profane terms. In a real system this
would be replaced with a more robust solution or external service.

Example
-------
>>> from nlp.politeness_filter import filter_text
>>> filter_text("you fool")
'you ****'
"""

from __future__ import annotations

import re
from typing import Iterable

PROFANITIES: set[str] = {
    "fool",
    "idiot",
    "dumb",
}


def _word_re(words: Iterable[str]) -> re.Pattern[str]:
    pattern = r"\b(" + "|".join(map(re.escape, words)) + r")\b"
    return re.compile(pattern, flags=re.IGNORECASE)


_PROFANITY_RE = _word_re(PROFANITIES)


def filter_text(text: str, replacement: str = "****") -> str:
    """Return *text* with profanities replaced by *replacement*."""

    return _PROFANITY_RE.sub(replacement, text)

