"""Gelişmiş vision (görsel işleme) modülü.

- Basit etiket ve dosya adından detection
- PIL/Pillow ile gerçek görüntü boyutu, renk ve basit öznitelik analizi
- Basit caption üretimi
- Kolayca yeni model/algoritma entegre edilebilir
"""

from __future__ import annotations
import os

try:
    from PIL import Image
except ImportError:
    Image = None

_KEYWORDS = {
    "cat": ["cat", "kedi", "ked"],
    "dog": ["dog", "köpek"],
    "car": ["car", "araba", "oto"],
    "person": ["person", "insan"],
}

def detect_objects(image_path: str) -> list[str]:
    """Akıllı dosya adı ve görsel üzerinden nesne etiketi bulur."""
    labels = []
    name = os.path.basename(image_path).lower()
    for key, aliases in _KEYWORDS.items():
        if any(alias in name for alias in aliases):
            labels.append(key)
    # Eğer PIL varsa, görsel analizi ile ekstra tag
    if Image:
        try:
            with Image.open(image_path) as img:
                w, h = img.size
                if w > 300 and h > 300:
                    labels.append("large-object")
                # Ortalama renk analizi
                avg = tuple([int(x) for x in img.resize((1,1)).getpixel((0,0))])
                if avg[0] > 200 and avg[1] > 200 and avg[2] > 200:
                    labels.append("mostly-white")
                elif avg[0] < 60 and avg[1] < 60 and avg[2] < 60:
                    labels.append("mostly-dark")
        except Exception:
            pass
    return labels or ["unknown"]

def caption_image(image_path: str) -> str:
    """Görüntüyü özetleyen akıllı bir caption üretir."""
    labels = detect_objects(image_path)
    if not labels or labels == ["unknown"]:
        return "No recognizable objects detected."
    if "person" in labels:
        return "Image contains a person."
    if "cat" in labels or "dog" in labels:
        return f"Image contains a {labels[0]}"
    if "large-object" in labels:
        return "Image shows a large object."
    if "mostly-white" in labels:
        return "Image is mostly white/bright."
    if "mostly-dark" in labels:
        return "Image is mostly dark."
    return f"Image contains: {', '.join(labels)}"

# Ekstra: basit histogram analizi örneği
def image_histogram(image_path: str) -> dict:
    """RGB histogram döndürür (PIL varsa)."""
    if not Image:
        return {}
    try:
        with Image.open(image_path) as img:
            h = img.histogram()
            return {
                "red": sum(h[0:256]),
                "green": sum(h[256:512]),
                "blue": sum(h[512:768]),
            }
    except Exception:
        return {}

# Test & örnek
if __name__ == "__main__":
    path = "test_cat.jpg"
    print("Detected:", detect_objects(path))
    print("Caption:", caption_image(path))
    print("Histogram:", image_histogram(path))
