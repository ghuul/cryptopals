"""
c01.py

Cryptopals Set 1, Challenge 1
"""

import base64


def main():
    h = ('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69' +
            '736f6e6f7573206d757368726f6f6d')

    # Decode hex to bytes.
    b = bytearray.fromhex(h)
    print b

    # Encode bytes as base64.
    r = base64.encodestring(b).decode('utf-8')[:-1]
    print r

    # Decode base64 to bytes.
    b = base64.decodestring(bytes(r))

    # Encode bytes as hex.
    h = b.encode('hex')
    print h
