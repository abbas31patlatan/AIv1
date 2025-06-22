"""Simplified voice assistant supporting TTS and STT.

`pyttsx3` and `speech_recognition` are optional dependencies.  When they are not
available or fail the assistant gracefully falls back to printing output and
capturing text via ``input``.

Example
-------
>>> speak('Hello world!')
'Hello world!'
"""
from __future__ import annotations

import logging

try:  # pragma: no cover - optional dependency
    import pyttsx3
except Exception:  # pragma: no cover - missing pkg
    pyttsx3 = None

try:  # pragma: no cover - optional dependency
    import speech_recognition as sr
except Exception:  # pragma: no cover - missing pkg
    sr = None


def speak(message: str) -> str:
    """Vocalise *message* if possible and return it."""
    if pyttsx3:
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
    else:
        print(f"[TTS] {message}")
    return message


def listen(timeout: int = 5) -> str:
    """Capture a short utterance and return it as text."""
    if sr:
        recogniser = sr.Recognizer()
        with sr.Microphone() as source:  # pragma: no cover - hardware
            audio = recogniser.listen(source, timeout=timeout)
        try:
            return recogniser.recognize_google(audio)
        except Exception as exc:  # pragma: no cover - network/hardware
            logging.debug("speech recognition failed: %s", exc)
    return input("You: ")
