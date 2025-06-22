"""Utilities for loading GGUF language models.

This module demonstrates how to load a GGUF formatted model using the
``llama_cpp`` package. The loader falls back gracefully when the
package is unavailable.

Example
-------
>>> from models.gguf_loader import GGUFModel
>>> model = GGUFModel('model.gguf')
>>> text = model.generate('Hello')
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional


class GGUFModel:
    """Wrapper around ``llama_cpp.Llama`` for GGUF models."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._llama = None
        logging.debug("GGUFModel created for %s", self.path)

    def load(self) -> None:
        """Load the model from disk."""
        try:
            from llama_cpp import Llama
        except Exception as exc:
            raise RuntimeError(
                "llama_cpp package is required to load GGUF models"
            ) from exc

        self._llama = Llama(model_path=str(self.path))
        logging.info("GGUF model loaded from %s", self.path)

    @property
    def ready(self) -> bool:
        """Return ``True`` if the underlying model is loaded."""
        return self._llama is not None

    def generate(self, prompt: str, max_tokens: int = 16) -> str:
        """Generate a text completion for *prompt*."""
        if not self._llama:
            self.load()
        result: Optional[dict] = self._llama(prompt, max_tokens=max_tokens)
        return result["choices"][0]["text"].strip()
