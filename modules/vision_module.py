"""Very small vision module with dummy detection and captioning."""
from __future__ import annotations

import os

try:  # pragma: no cover - optional dependency
    from PIL import Image
except Exception:  # pragma: no cover - missing pkg
    Image = None


_KEYWORDS = {
    "cat": ["cat"],
    "dog": ["dog"],
}


def detect_objects(image_path: str) -> list[str]:
    """Return a list of detected object labels in ``image_path``."""
    name = os.path.basename(image_path).lower()
    for key, labels in _KEYWORDS.items():
        if key in name:
            return labels
    # fall back to simple check on image size
    if Image:
        try:
            with Image.open(image_path) as img:  # pragma: no cover - file access
                w, h = img.size
            if w > 100 and h > 100:
                return ["large-object"]
        except Exception:
            pass
    return []


def caption_image(image_path: str) -> str:
    """Generate a very naive caption for ``image_path``."""
    labels = detect_objects(image_path)
    if labels:
        return f"Image contains a {labels[0]}"
    return "No objects detected"
