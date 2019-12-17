"""
c11.py

Cryptopals Set 2, Challenge 11
"""

import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptopals import aes, padding


def main():
    correct = 0
    for _ in range(1000):
        ct, mode = encryption_oracle(bytearray(b'a') * 5 * 16)
        is_ecb = aes.detect_ecb(ct)

        # Check if answer is correct.
        correct += ((is_ecb and mode == AES.MODE_ECB) or
                (not is_ecb and mode == AES.MODE_CBC))

    print correct == 1000


def encryption_oracle(bs):
    """
    A black box that encrypts data under an unknown key using ECB mode half the
    time, and CBC mode the other half.

    It appends a random suffix and a random prefix in the following format:
    random prefix | input | random suffix
    """
    # Prepend 5 - 10 bytes randomly.
    prepend = random.randint(5, 10)
    bs = bytearray(get_random_bytes(prepend)) + bs

    # Append 5 - 10 bytes randomly.
    append = random.randint(5, 10)
    bs += bytearray(get_random_bytes(append))

    # Pad input to a multiple of 16 bytes.
    bs = padding.pkcs7(bs, 16)

    # Generate a random key.
    key = get_random_bytes(16)

    # Choose whether to encrypt under ECB or CBC. 
    r = random.uniform(0, 1)

    if r > 0.5:
        # Encrypt under ECB mode.
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(bytes(bs)), AES.MODE_ECB

    # Encrypt under CBC mode.
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    return cipher.encrypt(bytes(bs)), AES.MODE_CBC
