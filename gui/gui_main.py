"""Entry point for the text-based GUI.

The GUI in this sample project is intentionally simple.  It exposes a text
based menu that allows the user to tweak a handful of preferences such as the
active theme, whether voice feedback is enabled and if the application should
operate in offline mode.  ``run`` can be executed in non-interactive mode for
testing, where it simply returns a placeholder button.

Example
-------
>>> from gui.gui_main import run
>>> run()  # returns the start button for unit tests
'[button]Start AIv1'
>>> run(interactive=False)
'[button]Start AIv1'
"""
from __future__ import annotations

from .gui_elements import button
from config.gui_preferences import prefs
from config.themes_config import themes
from modules.offline_mode import OfflineMode
from modules.voice_assistant import speak
from config import consciousness

def _display_menu(off: OfflineMode) -> None:
    """Print current settings to the console."""
    print(f"Theme: {prefs.theme} | Voice: {prefs.voice_enabled} | Offline: {off.active}")
    print("1) Toggle voice")
    print("2) Change theme")
    print("3) Toggle offline mode")
    print("0) Exit")


def run(*, interactive: bool = False) -> str:
    """Return a start button or launch the interactive menu."""
    screen = button("Start AIv1")
    if not interactive:
        return screen

    offline = OfflineMode()
    speak("Welcome to AIv1")
    while True:
        _display_menu(offline)
        choice = input("> ").strip()
        if choice == "1":
            prefs.toggle_voice()
            consciousness.think("voice toggled")
            speak(f"Voice {'on' if prefs.voice_enabled else 'off'}")
        elif choice == "2":
            print("Available:", ", ".join(themes.themes))
            t = input("Theme: ").strip()
            if t in themes.themes:
                prefs.set_theme(t)
                consciousness.think(f"theme set to {t}")
                speak(f"Theme {t}")
            else:
                print("Unknown theme")
        elif choice == "3":
            offline.force(not offline.active)
            consciousness.think(f"offline {'enabled' if offline.active else 'disabled'}")
            speak(f"Offline {'on' if offline.active else 'off'}")
        elif choice == "0":
            break
    prefs.save()
    return screen
