"""Very naive sarcasm detector.

This module uses a few heuristic rules to guess if a piece of text is written
sarcastically. It is by no means accurate but provides an example of how such a
component could be integrated into the dialogue pipeline.

Example
-------
>>> from nlp.sarcasm_detector import detect_sarcasm
>>> detect_sarcasm("yeah right, that will happen")
True
"""

from __future__ import annotations


_SARCASM_MARKERS = {
    "yeah right",
    "as if",
    "sure",
}


def detect_sarcasm(text: str) -> bool:
    """Return ``True`` if *text* appears sarcastic."""

    lowered = text.lower()
    return any(marker in lowered for marker in _SARCASM_MARKERS)

