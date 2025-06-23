"""Simple response generation based on intent and sentiment.

This module demonstrates how various NLP utilities can be combined to produce a
user facing response. It passes the input through the :mod:`slang_handler` and
the :mod:`politeness_filter` before analysing it with other components.

Example
-------
>>> from nlp.response_generator import generate_response
>>> generate_response("hi")
'Hello!'
"""

from __future__ import annotations

from typing import Optional

from models.gguf_loader import GGUFModel

from .intent_classifier import classify_intent
from .language_emotion import analyze_sentiment
from .politeness_filter import filter_text
from .sarcasm_detector import detect_sarcasm
from .slang_handler import normalize_slang
from .translation_module import translate


def generate_response(
    text: str, *, target_lang: Optional[str] = None, model: GGUFModel | None = None
) -> str:
    """Generate a reply string for *text* optionally translated or via LLM."""

    clean = normalize_slang(text)
    clean = filter_text(clean)
    intent = classify_intent(clean)
    sentiment = analyze_sentiment(clean)
    sarcastic = detect_sarcasm(clean)

    if model and model.ready:
        reply = model.generate(clean)
    elif intent == "greet":
        reply = "Hello!"
    elif intent == "bye":
        reply = "Goodbye!"
    elif sarcastic:
        reply = "I'll take that with a grain of salt."
    elif sentiment == "positive":
        reply = "I'm happy to hear that."
    elif sentiment == "negative":
        reply = "Oh, that's unfortunate."
    else:
        reply = "Tell me more."

    if target_lang:
        reply = translate(reply, target_lang)
    return reply

