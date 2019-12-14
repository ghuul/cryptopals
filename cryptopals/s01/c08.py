"""
c08.py

Cryptopals Set 1, Challenge 8
"""

import cryptopals.aes as aes


def main():
    # Read in the data.
    lines = open('assets/challenges/8.txt', 'r').read().splitlines()
    lines = [bytes.fromhex(line) for line in lines]

    # Detect which one is most likely AES in ECB mode.
    score, r, line = aes.detect_aes_ecb(lines)
    print((score, r.hex(), line))

