"""
c10.py

Cryptopals Set 2, Challenge 10
"""

import base64
from Crypto.Cipher import AES
from cryptopals import xor, padding


def main():
    # Read in data.
    data = ''.join(open('assets/challenges/10.txt', 'r').read().splitlines())
    bs = base64.decodestring(bytes(data))
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Decipher AES CBC mode encryption.
    r = aes_cbc_decrypt(bytearray(bs), bytearray(b'YELLOW SUBMARINE'),
            bytearray(iv))
    print r


def aes_cbc_decrypt(bs, key, iv):
    """
    An implementation of AES in CBC mode decryption.
    """
    # Ensure input is a multiple of 16 bytes.
    if len(bs)%16 != 0:
        raise 'Length of input must be a multiple of 16 bytes.'

    # Ensure key is 16 bytes long.
    if len(key) != 16:
        raise 'Key must be 16 bytes long.'

    # Ensure iv is 16 bytes long.
    if len(iv) != 16:
        raise 'Initialization vector must be 16 bytes long.'

    # Initialize cipher and prev_block variable.
    cipher = AES.new(key, AES.MODE_ECB)
    prev = iv

    ret = b''
    for i in range(0, len(bs), 16):
        ret += xor.fixed(bytearray(cipher.decrypt(bs[i:i+16])), prev)
        prev = bs[i:i+16]

    return ret
