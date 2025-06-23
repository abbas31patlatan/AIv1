"""Slang normalisation helpers.

The :func:`normalize_slang` function converts a few common slang or shorthand
terms into their formal equivalents. This is useful prior to running other NLP
analysis so that downstream modules operate on standard language.

Example
-------
>>> from nlp.slang_handler import normalize_slang
>>> normalize_slang("u r awesome")
'you are awesome'
"""

from __future__ import annotations


_SLANG_MAP: dict[str, str] = {
    "u": "you",
    "r": "are",
    "ya": "you",
    "pls": "please",
    "thx": "thanks",
}


def normalize_slang(text: str) -> str:
    """Return *text* with slang terms replaced by their formal counterparts."""

    words = text.split()
    normalized = [
        _SLANG_MAP.get(word.lower(), word) for word in words
    ]
    return " ".join(normalized)

