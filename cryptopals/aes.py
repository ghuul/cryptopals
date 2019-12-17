"""
aes.py
"""

import itertools
from Crypto.Cipher import AES
from cryptopals import util


def detect_ecb_multi(ctexts):
    """
    Given a list of ciphertexts, determines which one is most likely to be
    AES in ECB mode.
    """
    return [c for c in ctexts if detect_ecb(c)]


def detect_ecb(ctext):
    """
    Returns True if ciphertext is likely to be encrypted under ECB mode, False
    if otherwise.
    """
    # Break into blocks of 16.
    blocks = [bytes(ctext[i:i+16]) for i in range(0, len(ctext), 16)]

    # Find the set of unique blocks.
    unique = set(blocks)

    # If the set of unique blocks is smaller than the number of blocks, then
    # we have repeated blocks - therefore it is encrypted under ECB mode.
    return len(unique) < len(blocks)
