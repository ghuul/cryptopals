"""
c12.py

Cryptopals Set 2, Challenge 12
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from cryptopals import padding

secret_key    = get_random_bytes(16)
hidden_suffix = base64.decodestring('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWc' +
        'tdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZG' +
        'J5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZ' +
        'HJvdmUgYnkK')


def main():
    # Find the length of the hidden suffix.
    suf_len = suffix_length(encryption_oracle)

    # Find the hidden suffix.
    print decrypt_hidden_suffix(suf_len, encryption_oracle)


def encryption_oracle(bs):
    """
    A black box that encrypts an input with a hidden key under ECB mode.

    It appends a hidden suffix of fixed but unknown length to the data before
    encryption in the following format:
    input | hidden suffix
    """
    bs += hidden_suffix
    bs = padding.pkcs7(bs, 16)
    return AES.new(secret_key, AES.MODE_ECB).encrypt(bs)


def suffix_length(oracle):
    """
    Determines the length of the suffix appended to user input in the oracle.
    """
    start = len(oracle(''))
    for i in range(17):
        if len(oracle('A'*i)) != start:
            break
    return start - i


def decrypt_hidden_suffix(length, oracle):
    """
    Decrypts the hidden suffix appended to the input in the oracle.
    """
    n, suffix = 0, ''
    while len(suffix) < length:
        suffix = decrypt_block(n, suffix, length, oracle)
        n += 1
    return suffix


def decrypt_block(n, suffix, length, oracle):
    """
    Decrypts one block of the hidden suffix appended to the user input in the
    oracle.
    """ 
    for i in range(16):
        # If length of suffix is equal to the length of the suffix, return.
        if len(suffix) == length:
            return suffix

        # Generate input.
        inp = 'A' * (15 - i)

        # Build dictionary and find next byte in the suffix.
        inp_len = len(inp + suffix) + 1
        inputs = {
            oracle(inp + suffix + chr(j))[:inp_len]:(inp + suffix + chr(j))
            for j in range(256)
        }
        suffix += inputs[oracle(inp)[:inp_len]][-1]

    return suffix

