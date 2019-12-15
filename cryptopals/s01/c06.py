"""
c06.py

Cryptopals Set 1, Challenge 6
"""

import base64
from cryptopals import xor, scoring


def main():
    # Read in data.
    data = ''.join(open('assets/challenges/6.txt', 'r').read().splitlines())
    bs = base64.decodestring(bytes(data))

    # Break repeating key XOR.
    scorer = scoring.Scorer(2)
    r = xor.break_repeating_key(bytearray(bs), scorer)
    print r
