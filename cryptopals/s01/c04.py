"""
c04.py

Cryptopals Set 1, Challenge 4
"""

import cryptopals.xor as xor
import cryptopals.scoring as scoring


def main():
    ctexts = open('assets/challenges/4.txt', 'r').read().splitlines()

    scorer = scoring.Scorer(2)
    r = xor.detect_single_byte_xor(ctexts, scorer)
    print(r)


if __name__ == '__main__':
    main()
