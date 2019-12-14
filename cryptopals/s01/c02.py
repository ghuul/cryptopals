"""
c02.py

Cryptopals Set 1, Challenge 2
"""

import cryptopals.xor as xor


def main():
    b1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    b2 = bytes.fromhex('686974207468652062756c6c277320657965')

    # Run fixed XOR on both byte arrays.
    r = xor.fixed_xor(b1, b2).hex()
    print(r)
