"""
c16.py

Cryptopals Set 2, Challenge 16
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptopals import padding

secret_key  = get_random_bytes(16)
init_vector = get_random_bytes(16)


def main():
    data = encryption_oracle('none~admin~true')
    blocks = [data[i:i+16] for i in range(0, len(data), 16)]

    target = bytearray(blocks[1])

    # 0111 1110 (~) -> 0011 1011 (;) 
    # 0111 1110 ^ 0100 0101 = 0011 1011
    target[4] ^= 69

    # 0111 1110 (~) -> 0011 1101 (=)
    # 0111 1110 ^ 0100 0011 = 0011 1101
    target[10] ^= 67

    blocks[1] = bytes(target)

    data = reduce(lambda ac, x: ac + x, blocks)
    print verify_admin(data)


def encryption_oracle(bs):
    """
    Takes an input and sandwiches it between two known strings before
    encrypting it with an unknown iv and key under CBC mode.
    """
    bs = ('comment1=cooking%20MCs;userdata=' + sanitize(bs) +
            ';comment2=%20like%20a%20pound%20of%20bacon')
    bs = padding.pkcs7(bs, 16)
    return AES.new(secret_key, AES.MODE_CBC, init_vector).encrypt(bs)


def sanitize(inp):
    """
    Sanitizes user input, removes the ';' and '=' characters.
    """
    # Escape the ';' and '=' characters.
    inp = inp.replace(';', '')
    return inp.replace('=', '')


def verify_admin(bs):
    """
    Decripts an encrypted input, and verifies that the user that submitted was
    an admin.
    """
    # Decrypt the data.
    data = AES.new(secret_key, AES.MODE_CBC, init_vector).decrypt(bs)

    # Parse and return whether user is admin.
    try:
        data = padding.pkcs7_unpad(data, 16)
        return parse(data)['admin'] == 'true'
    except:
        return False


def parse(s):
    """
    Parses an encoded string and outputs it as a dictionary object.
    """
    return {k:v for k, v in (kv.split('=') for kv in s.split(';')
        if len(kv.split('=')) == 2)}

