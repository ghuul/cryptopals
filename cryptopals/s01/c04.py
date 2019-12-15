"""
c04.py

Cryptopals Set 1, Challenge 4
"""

from cryptopals import xor, scoring


def main():
    ctexts = open('assets/challenges/4.txt', 'r').read().splitlines()
    ctexts = [bytearray.fromhex(c) for c in ctexts]

    scorer = scoring.Scorer(2)
    r = xor.detect_single_byte(ctexts, scorer)
    print r 
