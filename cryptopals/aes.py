"""
aes.py
"""

import itertools
from Crypto.Cipher import AES
from cryptopals import util


def detect_ecb(ctexts):
    """
    Given a list of ciphertexts, determines which one is most likely to be
    AES in ECB mode.
    """
    for i in range(len(ctexts)):
        if is_ecb(ctext):
            return ctexts, i
    return None


def is_ecb(ctext):
    """
    Returns True if ciphertext is likely to be encrypted under ECB mode, False
    if otherwise.
    """
    # Break into blocks of 16.
    blocks = [ctext[i:i+16] for i in range(0, len(ctext), 16)]

    # Find the set of unique blocks.
    unique = set(blocks)

    # If the set of unique blocks is smaller than the number of blocks, then
    # we have repeated blocks - therefore it is encrypted under ECB mode.
    return len(unique) < len(blocks)


def ecb_cbc_oracle(ctext):
    """
    Detects whether a ciphertext is encrypted under ECB or CBC mode.
    """
    if is_ecb(ctext):
        return AES.MODE_ECB
    return AES.MODE_CBC
