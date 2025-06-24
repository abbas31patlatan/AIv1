"""Reusable tkinter helper functions."""
from __future__ import annotations

import tkinter as tk
from typing import Callable


def button(parent: tk.Widget, label: str, command: Callable[[], None]) -> tk.Button:
    """Return a standard ``Button`` widget."""
    btn = tk.Button(parent, text=label, command=command)
    btn.pack(padx=5, pady=5)
    return btn


def label(parent: tk.Widget, text: str) -> tk.Label:
    lbl = tk.Label(parent, text=text)
    lbl.pack(padx=5, pady=5)
    return lbl


def entry(parent: tk.Widget) -> tk.Entry:
    ent = tk.Entry(parent)
    ent.pack(padx=5, pady=5, fill=tk.X)
    return ent

