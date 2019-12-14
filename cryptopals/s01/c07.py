"""
c07.py

Cryptopals Set 1, Challenge 7
"""

import base64
from Crypto.Cipher import AES


def main():
    # Read in data.
    data = ''.join(open('assets/challenges/7.txt', 'r').read().splitlines())
    bs = base64.decodestring(bytes(data, 'utf-8'))

    # Decrypt the data with key 'YELLOW SUBMARINE'.
    cipher = AES.new(b'YELLOW SUBMARINE', AES.MODE_ECB)
    r = cipher.decrypt(bs)
    print(r)
