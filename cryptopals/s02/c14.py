"""
c14.py

Cryptopals Set 2, Challenge 14
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import random
from cryptopals import padding

secret_key    = get_random_bytes(16)
hidden_prefix = get_random_bytes(random.randint(0, 100))
hidden_suffix = base64.decodestring('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWc' +
        'tdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZG' +
        'J5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZ' +
        'HJvdmUgYnkK')


def main():
    # Find the prefix length.
    pre_len = prefix_length(encryption_oracle)

    # Find the suffix length.
    suf_len = suffix_length(pre_len, encryption_oracle)

    # Find the hidden suffix.
    print decrypt_hidden_suffix(pre_len, suf_len, encryption_oracle)


def encryption_oracle(bs):
    """
    A black box that encrypts an input under a hidden key in ECB mode.

    Prior to encryption a random hidden prefix and constant length hidden
    suffix are added to the input in the following format:
    hidden prefix | input | hidden suffix
    """
    bs = hidden_prefix + bs + hidden_suffix
    bs = padding.pkcs7(bs, 16)
    return AES.new(secret_key, AES.MODE_ECB).encrypt(bs)


def prefix_length(oracle):
    """
    Determines the length of the prefix prepended to the user input in the
    encryption oracle.
    """
    # Keep adding until 2 duplicate blocks present.
    for i in range(16):
        dup, idx = duplicate_blocks(oracle('A'*(32 + i)))
        if dup == 2:
            break
    return idx - i


def duplicate_blocks(bs):
    """
    Finds the first instance of duplicate blocks in the encrypted ciphertext.
    """
    blocks = [bs[i:i+16] for i in range(0, len(bs), 16)]

    prev = blocks[0]
    for i in range(1, len(blocks)):
        if blocks[i] == prev:
            break
        prev = blocks[i]

    return (len(blocks) - len(set(blocks)))*2, (i-1)*16


def suffix_length(pre_len, oracle):
    """
    Determines the length of the suffix appended to the input in the oracle.
    """
    # Keep adding until new block is appended.
    start = len(oracle(''))
    for i in range(17):
        if len(oracle('A'*i)) != start:
            break
  
    return start - pre_len - i


def decrypt_hidden_suffix(pre_len, length, oracle):
    """
    Decrypts the content of the hidden suffix appended to the user input in the
    encryption oracle.
    """
    n, suffix = 0, ''
    while len(suffix) < length:
        suffix = decrypt_block(n, suffix, pre_len, length, oracle)
        n += 1
    return suffix


def decrypt_block(n, suffix, pre_len, length, oracle):
    """
    Decrypts a 16-byte block of the hidden suffix appended to the user input
    in the encryption oracle.
    """
    for i in range(16):
        # If length of suffix is equal to the pre-determined suffix length,
        # return the suffix.
        if len(suffix) == length:
            return suffix

        # Generate input.
        inp = 'A' * (16 - pre_len%16) + 'A' * (15 - i)

        # Build dictionary and find next byte in the suffix.
        inp_len = pre_len + len(inp + suffix) + 1
        inputs = {
            oracle(inp + suffix + chr(j))[:inp_len]:(inp + suffix + chr(j))
            for j in range(256)
        }
        suffix += inputs[oracle(inp)[:inp_len]][-1]

    return suffix
