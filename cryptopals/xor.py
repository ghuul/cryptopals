"""
xor.py
"""

import itertools
from cryptopals import util


def fixed(b1, b2):
    """
    XORs two given sets of bytes, of equal length, together.
    """
    # Ensure that byte arrays are of equal length.
    if len(b1) != len(b2):
        raise Exception('Byte arrays are not of equal length.')

    # XOR byte arrays together and return.
    return bytearray([x ^ y for x, y in zip(b1, b2)])


def single_byte(bs, b):
    """
    Implementation of a single-byte XOR cipher.
    """
    # XOR each byte in the array with the single byte and return.
    return bytearray([bt ^ b for bt in bs])


def break_single_byte(bs, scorer):
    """
    Breaks a single-byte XOR cipher.
    """
    # For each possible byte, decode the single byte XOR and score the
    # plaintext before appending to array of tuples.
    rets = []
    for i in range(256):
        pt = single_byte(bs, i)
        rets.append((scorer.score(pt), i, pt))

    # Return the plaintex with the highest score.
    rets.sort(key=lambda x: x[0], reverse=True)
    return rets[0]


def detect_single_byte(ctexts, scorer):
    """
    Detects single-byte XOR in a list of single-byte XORed ciphertexts.
    """
    # Find the best result for each ciphertext.
    rets = [break_single_byte(c, scorer) for c in ctexts]
    
    # Return the result with the highest score.
    rets.sort(key=lambda x: x[0], reverse=True)
    return rets[0]


def repeating_key(bs, key):
    """
    Implementation of repeating-key XOR.
    """
    # XOR each byte of the byte array with its appropriate key byte.
    return bytearray([bs[i] ^ key[i%len(key)] for i in range(len(bs))])


def break_repeating_key(bs, scorer):
    """
    Breaks a repeating-key XOR cipher.
    """
    # Determine the average edit distance for each keysize.
    kss = []
    for ks in range(2, 40):
        perms = itertools.permutations(
                [bs[i:i+ks] for i in range(0, len(bs), ks)], 2)
        dists = [util.hamming_distance(p[0], p[1])/ks for p in perms
                if len(p[0]) == len(p[1])]
        kss.append((ks, sum(dists) / float(len(dists))))

    # Find the best keysize.
    kss.sort(key=lambda x: x[1])
    ks = kss[0][0]

    # Break ciphertext up into keysize blocks.
    blocks = [bs[i::ks] for i in range(ks)]

    # Solve each block as single-byte XOR.
    key = []
    for block in blocks:
        _, b, _ = break_single_byte(block, scorer)
        key.append(b)

    return (bytearray(key), repeating_key(bs, bytearray(key)))
