"""
c10.py

Cryptopals Set 2, Challenge 10
"""

import base64
from Crypto.Cipher import AES
import cryptopals.padding as padding
import cryptopals.xor as xor


def main():
    # Read in data.
    data = ''.join(open('assets/challenges/10.txt', 'r').read().splitlines())
    bs = base64.decodestring(bytes(data, 'utf-8'))
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Decipher AES CBC mode encryption.
    r = aes_cbc_decrypt(bs, b'YELLOW SUBMARINE', iv)
    print(r)


def aes_cbc_encrypt(bs, key, iv):
    """
    An implementation of AES in CBC mode encryption.
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
        ret += cipher.encrypt(xor.fixed_xor(bs[i:i+16], prev))
        prev = ret[i:i+16]

    return ret


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
        ret += xor.fixed_xor(cipher.decrypt(bs[i:i+16]), prev)
        prev = bs[i:i+16]

    return ret
