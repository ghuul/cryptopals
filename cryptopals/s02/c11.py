"""
c11.py

Cryptopals Set 2, Challenge 11
"""

import random
from Crypto.Cipher import AES
from cryptopals import aes, padding


def main():
    correct = 0
    for _ in range(1000):
        ct, mode = encryption_oracle(bytearray(b'a') * 5 * 16)
        correct += (mode == aes.ecb_cbc_oracle(ct))

    print correct == 1000


def encryption_oracle(bs):
    # Prepend 5 - 10 bytes randomly.
    prepend = random.randint(5, 10)
    bs = bytearray(random.getrandbits(8) for _ in range(prepend)) + bs

    # Append 5 - 10 bytes randomly.
    append = random.randint(5, 10)
    bs += bytearray(random.getrandbits(8) for _ in range(append))

    # Pad input to a multiple of 16 bytes.
    bs = padding.pkcs7(bs, 16)

    # Generate a random key.
    key = bytearray(random.getrandbits(8) for _ in range(16))

    # Choose whether to encrypt under ECB or CBC. 
    r = random.uniform(0, 1)

    if r > 0.5:
        # Encrypt under ECB mode.
        mode = AES.MODE_ECB
    else:
        # Encrypt under CBC mode.
        mode = AES.MODE_CBC

    cipher = AES.new(bytes(key), mode)
    return cipher.encrypt(bytes(bs)), mode
