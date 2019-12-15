"""
c05.py

Cryptopals Set 1, Challenge 5
"""

from cryptopals import xor


def main():
    bs = bytearray('Burning \'em, if you ain\'t quick and nimble\n' +
            'I go crazy when I hear a cymbal')
    key = bytearray('ICE')
    
    # Repeating key XOR with key 'ICE'.
    r = xor.repeating_key(bs, key)
    print bytes(r).encode('hex')
