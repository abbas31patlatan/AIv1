"""Real-time translation using our tiny translator."""
from __future__ import annotations

from nlp.translation_module import translate


def realtime(text: str, lang: str) -> str:
    return translate(text, lang)
