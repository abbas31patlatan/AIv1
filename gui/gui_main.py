"""Simple tkinter based GUI with theme and voice support."""
from __future__ import annotations

import tkinter as tk

from config.gui_preferences import prefs
from modules.voice_assistant import speak

from .gui_elements import button, entry, label
from .themes import apply_theme, THEMES


class DummyRoot:
    """Minimal stand-in for :class:`tkinter.Tk` in headless environments."""

    def __init__(self) -> None:
        self._config: dict[str, str] = {}
        self._title = "AIv1"

    def configure(self, **opts: str) -> None:
        self._config.update(opts)

    def cget(self, key: str) -> str:
        return self._config.get(key, "")

    def winfo_children(self):
        return []

    def title(self, value: str | None = None) -> str:
        if value is not None:
            self._title = value
        return self._title

    def destroy(self) -> None:
        pass

    def mainloop(self) -> None:
        pass


class AppGUI:
    """Interactive window that echoes user input using voice."""

    def __init__(self) -> None:
        try:
            self.root = tk.Tk()
            self._headless = False
        except tk.TclError:  # no DISPLAY
            self.root = DummyRoot()
            self._headless = True

        self.root.title("AIv1")
        apply_theme(self.root, prefs.theme)

        if not self._headless:
            label(self.root, "Say something:")
            self.text_entry = entry(self.root)
            button(self.root, "Send", self._on_send)
            self.output = label(self.root, "")
        else:
            self.text_entry = None
            self.output_text = ""

    @property
    def theme(self) -> dict[str, str]:
        return THEMES.get(prefs.theme, THEMES["light"])

    def _on_send(self) -> None:
        if self._headless:
            return
        text = self.text_entry.get()
        self.output.config(text=text)
        if prefs.voice_enabled:
            speak(text)

    def run(self) -> None:
        self.root.mainloop()


def run() -> str:
    """Convenience wrapper used by tests."""
    app = AppGUI()
    if not isinstance(app.root, DummyRoot):
        app.root.update()
        title = app.root.title()
        app.root.destroy()
    else:
        title = app.root.title()
    return title

