"""
c08.py

Cryptopals Set 1, Challenge 8
"""

import cryptopals.aes as aes


def main():
    # Read in the data.
    lines = open('assets/challenges/8.txt', 'r').read().splitlines()
    lines = [bytearray.fromhex(line) for line in lines]

    # Detect which one is most likely AES in ECB mode.
    out = [bytes(c).encode('hex') for c in aes.detect_ecb_multi(lines)]
    print out

