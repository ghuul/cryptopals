"""
aes.py
"""

import itertools
import cryptopals.util as util


def detect_aes_ecb(ctexts):
    """
    Given a list of ciphertexts, determines which one is most likely to be
    AES in ECB mode.
    """
    # Find the average edit distance for blocks of 16, for each ciphertext.
    rets = []
    line = 0
    for ctext in ctexts:
        # Break into blocks of 16 and find all permutations of length 2.
        blcks = [ctext[i:i+16] for i in range(0, len(ctext), 16)]
        perms = itertools.permutations(blcks, 2)

        # Calculate the average edit distance.
        dists = [util.hamming_distance(p[0], p[1]) for p in perms
                if len(p[0]) == len(p[1])]
        rets.append((sum(dists) / len(dists), ctext, line)) 
        line += 1

    # Find the ciphertext with the smallest average edit distance.
    rets.sort(key=lambda x: x[0])
    return rets[0]

