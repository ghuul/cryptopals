"""
c09.py

Cryptopals Set 2, Challenge 9
"""

from cryptopals import padding


def main():
    r = padding.pkcs7(b'YELLOW SUBMARINE', 20)
    print bytes(r).encode('hex')
