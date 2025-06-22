"""Natural language processing utilities used by the AI system."""

from .intent_classifier import classify_intent
from .language_emotion import analyze_sentiment
from .politeness_filter import filter_text
from .slang_handler import normalize_slang
from .sarcasm_detector import detect_sarcasm
from .sentence_analyzer import classify_sentence
from .translation_module import translate
from .response_generator import generate_response
from .humanity import is_human_like
