from utils.encryption import encrypt, decrypt
from utils.time_tools import now_ms


def test_encrypt_decrypt():
    cipher = encrypt('x', 1)
    assert decrypt(cipher, 1) == 'x'


def test_now_ms():
    assert isinstance(now_ms(), int)

