"""Sentence form analysis utilities.

The :func:`classify_sentence` function inspects punctuation to roughly
categorise a sentence as ``question``, ``exclamation`` or ``statement``.

Example
-------
>>> from nlp.sentence_analyzer import classify_sentence
>>> classify_sentence("How are you?")
'question'
"""

from __future__ import annotations


def classify_sentence(text: str) -> str:
    """Return a label describing the *text* sentence type."""

    stripped = text.strip()
    if stripped.endswith("?"):
        return "question"
    if stripped.endswith("!"):
        return "exclamation"
    return "statement"

