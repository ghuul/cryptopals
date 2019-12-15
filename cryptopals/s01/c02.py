"""
c02.py

Cryptopals Set 1, Challenge 2
"""

from cryptopals import xor


def main():
    b1 = bytearray.fromhex('1c0111001f010100061a024b53535009181c')
    b2 = bytearray.fromhex('686974207468652062756c6c277320657965')

    # Run fixed XOR on both byte arrays.
    r = xor.fixed(b1, b2).encode('hex')
    print r
