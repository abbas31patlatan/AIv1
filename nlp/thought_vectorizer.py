"""Utility for converting text into numeric vectors.

This simplified implementation counts token occurrences based on a provided
vocabulary. It can be used to feed simple machine learning models or as an
illustration of how feature extraction might be built.

Example
-------
>>> from nlp.thought_vectorizer import vectorize
>>> vectorize("hello world", vocabulary=["hello", "world", "foo"])
[1, 1, 0]
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, List


def vectorize(text: str, vocabulary: Iterable[str]) -> List[int]:
    """Return a bag-of-words vector for *text* based on *vocabulary*."""

    counts = Counter(text.lower().split())
    return [counts.get(word.lower(), 0) for word in vocabulary]

