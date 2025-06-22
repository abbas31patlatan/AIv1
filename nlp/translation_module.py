"""Tiny rule based translation module.

Only a very small dictionary between English and Spanish is provided for
illustration purposes. Real applications should of course rely on dedicated
translation APIs or models.

Example
-------
>>> from nlp.translation_module import translate
>>> translate("hello", target_lang="es")
'hola'
"""

from __future__ import annotations

from typing import Dict


_EN_ES: Dict[str, str] = {
    "hello": "hola",
    "goodbye": "adios",
    "thanks": "gracias",
}


def translate(text: str, target_lang: str) -> str:
    """Return a translated version of *text* if possible."""

    if target_lang == "es":
        return " ".join(_EN_ES.get(word.lower(), word) for word in text.split())
    raise ValueError(f"unsupported language: {target_lang}")

