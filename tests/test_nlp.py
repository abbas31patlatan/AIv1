from nlp.intent_classifier import classify_intent
from nlp.language_emotion import analyze_sentiment
from nlp.politeness_filter import filter_text
from nlp.slang_handler import normalize_slang
from nlp.sarcasm_detector import detect_sarcasm
from nlp.sentence_analyzer import classify_sentence
from nlp.translation_module import translate
from nlp.response_generator import generate_response


def test_intent():
    assert classify_intent("hello") == "greet"
    assert classify_intent("bye now") == "bye"
    assert classify_intent("something else") == "unknown"


def test_sentiment():
    assert analyze_sentiment("it is great") == "positive"
    assert analyze_sentiment("it is bad") == "negative"


def test_politeness():
    assert filter_text("you idiot") == "you ****"


def test_slang():
    assert normalize_slang("u r cool") == "you are cool"


def test_sarcasm():
    assert detect_sarcasm("yeah right")


def test_sentence_classification():
    assert classify_sentence("Hello!") == "exclamation"
    assert classify_sentence("How are you?") == "question"


def test_translation():
    assert translate("hello", "es") == "hola"


def test_response_generation():
    assert generate_response("hi") == "Hello!"
