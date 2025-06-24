"""Predefined GUI themes and helpers.

This module exposes a small collection of colour themes and a helper function
which can apply them to a :class:`tkinter.Tk` instance.  Themes are simple
dictionaries mapping widget options to colour values.
"""
from __future__ import annotations

from typing import Dict
import tkinter as tk

# Mapping of theme names to configuration dictionaries
THEMES: Dict[str, Dict[str, str]] = {
    "light": {"bg": "#ffffff", "fg": "#000000", "highlight": "#d3d3d3"},
    "dark": {"bg": "#222222", "fg": "#eeeeee", "highlight": "#555555"},
    "solar": {"bg": "#fdf6e3", "fg": "#586e75", "highlight": "#b58900"},
    "blue": {"bg": "#eaf6fb", "fg": "#104e8b", "highlight": "#cfe2f3"},
    "pink": {"bg": "#fde8f0", "fg": "#822659", "highlight": "#ffcfe2"},
}

def apply_theme(root: tk.Tk, name: str) -> None:
    """Apply the theme *name* to *root* if available."""
    theme = THEMES.get(name, THEMES["light"])
    root.configure(bg=theme["bg"])
    for widget in root.winfo_children():
        try:
            widget.configure(bg=theme["bg"], fg=theme["fg"])
        except tk.TclError:
            # Not all widgets support both options
            try:
                widget.configure(bg=theme["bg"])
            except Exception:
                pass

# Eğer dışarıdan temalar da okunacaksa burada "themes" dict'ini de dışa aktarabilirsin:
themes = THEMES
