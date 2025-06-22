"""Heuristic checks for human-like text.

The :func:`is_human_like` function uses a minimal set of rules to guess whether
the supplied text appears to be written by a human. This is obviously limited
but demonstrates the concept.

Example
-------
>>> from nlp.humanity import is_human_like
>>> is_human_like("I can't wait!")
True
"""

from __future__ import annotations


def is_human_like(text: str) -> bool:
    """Return ``True`` if *text* appears human-like."""

    lowered = text.lower()
    if "http" in lowered or "bot" in lowered:
        return False
    if any(pronoun in lowered for pronoun in ("i", "you", "we")):
        return True
    return False

