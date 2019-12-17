"""
c15.py

Cryptopals Set 2, Challenge 15
"""

from cryptopals import padding


def main():
    s = 'ICE ICE BABY\x04\x04\x04\x04'
    print len(s), s
    
    s = padding.pkcs7_unpad(s, 16)
    print len(s), s
