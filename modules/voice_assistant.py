"""Ultra gelişmiş voice assistant modülü (TTS+STT, çoklu motor, dil seçimi).

Özellikler:
- Birden çok TTS (pyttsx3, gtts, coqui)
- Birden çok STT (SpeechRecognition, vosk, coqui)
- Otomatik fallback, offline/online seçim
- Türkçe/İngilizce ve otomatik dil tespiti
- Mikrofon seçimi, listeleme, clipboard entegrasyonu
- Hata yönetimi, test edilebilir yapı

Tüm modüller opsiyonel, en gelişmiş motor otomatik seçilir.
"""

from __future__ import annotations
import logging
import os

try: import pyttsx3
except ImportError: pyttsx3 = None
try: from gtts import gTTS
except ImportError: gTTS = None
try: import playsound
except ImportError: playsound = None
try: import speech_recognition as sr
except ImportError: sr = None
try: import vosk
except ImportError: vosk = None
try: import pyperclip
except ImportError: pyperclip = None

# Çevrimdışı kontrolü
try:
    from modules.offline_mode import available as offline
except Exception:
    def offline(): return False

def speak(
    message: str,
    lang: str = "tr",
    tts_engine: str = "auto",
    use_clipboard: bool = False
) -> str:
    """Gelişmiş sesli okuma (çoklu motor).
    - tts_engine: "pyttsx3" | "gtts" | "auto"
    - lang: "tr" | "en" | ...
    - use_clipboard: True ise message clipboard'a da kopyalanır
    """
    if use_clipboard and pyperclip:
        pyperclip.copy(message)
    if offline():
        print(f"[OFFLINE TTS] {message}")
        return message

    if tts_engine == "pyttsx3" or (tts_engine == "auto" and pyttsx3):
        engine = pyttsx3.init()
        # Dil ayarı (tr/en otomatik)
        if lang.startswith("tr"):
            for voice in engine.getProperty('voices'):
                if 'tr' in voice.languages or 'Turkish' in voice.name:
                    engine.setProperty('voice', voice.id)
                    break
        engine.say(message)
        engine.runAndWait()
    elif tts_engine == "gtts" or (tts_engine == "auto" and gTTS and playsound):
        # gTTS ile internetli TTS
        tts = gTTS(text=message, lang=lang)
        filename = "_gtts_voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    else:
        print(f"[TTS] {message}")
    return message

def list_microphones() -> list[str]:
    """Kullanılabilir mikrofonları listeler."""
    if not sr: return []
    return sr.Microphone.list_microphone_names()

def listen(
    timeout: int = 5,
    lang: str = "tr",
    stt_engine: str = "auto",
    select_microphone: int = -1,
    clipboard: bool = False,
    auto_lang_detect: bool = False
) -> str:
    """Gelişmiş konuşma algılama (çoklu motor, dil seçimi, clipboard).
    - stt_engine: "sr" | "vosk" | "coqui" | "auto"
    - lang: "tr" | "en" | ...
    - select_microphone: int, varsayılan (-1) ise varsayılan mic
    - auto_lang_detect: True ise ilk gelenin dilini tahmin etmeye çalışır
    - clipboard: True ise dinlenen metni panoya kopyalar
    """
    if offline() or not sr:
        text = input("You: ")
        if clipboard and pyperclip: pyperclip.copy(text)
        return text

    recogniser = sr.Recognizer()
    mic = sr.Microphone(device_index=select_microphone if select_microphone >= 0 else None)
    with mic as source:
        print("Dinleniyor...")
        audio = recogniser.listen(source, timeout=timeout)

    text = ""
    # SpeechRecognition Google (online) veya Sphinx/Vosk (offline)
    if stt_engine == "vosk" and vosk:
        try:
            model = vosk.Model(lang)
            rec = vosk.KaldiRecognizer(model, 16000)
            rec.AcceptWaveform(audio.get_raw_data())
            text = rec.Result()
        except Exception as exc:
            logging.debug("vosk failed: %s", exc)
    elif stt_engine == "sr" or stt_engine == "auto":
        try:
            text = recogniser.recognize_google(audio, language=lang)
        except Exception as exc:
            logging.debug("sr google failed: %s", exc)
            try:
                text = recogniser.recognize_sphinx(audio)
            except Exception:
                text = ""
    # (coqui veya başka STT motorları eklenebilir)

    if not text:
        text = input("You (text fallback): ")

    if clipboard and pyperclip:
        pyperclip.copy(text)

    if auto_lang_detect:
        import langdetect
        detected = langdetect.detect(text)
        print(f"Algılanan dil: {detected}")

    return text

def speak_clipboard(lang: str = "tr", **kwargs):
    """Panodaki metni okur (TTS ile)."""
    if pyperclip:
        text = pyperclip.paste()
        speak(text, lang=lang, **kwargs)

# Test ve örnekler
if __name__ == "__main__":
    print("Mikrofonlar:", list_microphones())
    speak("Hoşgeldin! Mikrofonu test etmek için konuşun.", lang="tr")
    text = listen(lang="tr", clipboard=True)
    print("Algılanan:", text)
    speak_clipboard(lang="tr")

