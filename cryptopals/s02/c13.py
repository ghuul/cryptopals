"""
c13.py

Cryptopals Set 2, Challenge 13
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptopals import padding

secret_key = get_random_bytes(16)


def main():
    # email=aaaaaaaaaa
    # aaaaaaaaa@gmail.
    # com&uid=10&role=
    # user------------
    email = 'a'*19 + '@gmail.com'

    # This gives us the first part of our privilege escalation.
    p1 = profile_for(email)[:48]

    # email=aaaaaaaaaa
    # admin-----------
    # @gmail.com&uid=1
    # 0&role=user
    email = 'a'*10 + padding.pkcs7('admin', 16) + '@gmail.com'

    # This gives us the second part of our privilege escalation.
    p2 = profile_for(email)[16:32]
    print dec_profile(p1 + p2)


def kv_parser(inp):
    """
    Converts a url-encoded string to a dictionary object.
    """
    return {obj[0]:obj[1]
            for obj in (obj.split('=') for obj in inp.split('&'))
            if len(obj) == 2}


def profile_for(email):
    """
    Generates an encrypted user profile based on an input email, without
    admin privileges.
    """
    # Input sanitization.
    email = email.replace('&', '')
    email = email.replace('=', '')
    return enc_profile('email=%s&uid=10&role=user' % email)


def enc_profile(profile):
    """
    Encrypts a url-encoded user profile.
    """
    profile = padding.pkcs7(profile, 16)
    return AES.new(secret_key, AES.MODE_ECB).encrypt(profile)


def dec_profile(profile): 
    """
    Decrypts and parses an encrypted url-encoded user profile.
    """
    profile = AES.new(secret_key, AES.MODE_ECB).decrypt(profile)

    try:
        return kv_parser(padding.pkcs7_unpad(profile, 16))
    except:
        return kv_parser(profile)
