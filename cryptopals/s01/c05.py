"""
c05.py

Cryptopals Set 1, Challenge 5
"""

import cryptopals.xor as xor


def main():
    bs = bytes('Burning \'em, if you ain\'t quick and nimble\n' +
            'I go crazy when I hear a cymbal', 'utf-8')
    key = b'ICE'
    
    # Repeating key XOR with key 'ICE'.
    r = xor.repeating_key_xor(bs, key)
    print(r.hex())
