"""Very small XOR-based encryption."""
from __future__ import annotations


def encrypt(text: str, key: int) -> str:
    return ''.join(chr(ord(c) ^ key) for c in text)


def decrypt(cipher: str, key: int) -> str:
    return ''.join(chr(ord(c) ^ key) for c in cipher)
