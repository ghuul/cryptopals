"""
c09.py

Cryptopals Set 2, Challenge 9
"""

import cryptopals.padding as padding


def main():
    r = padding.pkcs7(b'YELLOW SUBMARINE', 20)
    print(r)
