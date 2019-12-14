"""
util.py
"""

import cryptopals.xor as xor


def hamming_distance(b1, b2):
    """
    Calculates the hamming distance in bits, between two byte arrays.
    """
    # Ensure that both byte arrays are the same length.
    if len(b1) != len(b2):
        raise 'Byte arrays are not of equal length.'

    # Calculate the hamming distance.
    x = xor.fixed_xor(b1, b2)
    dist = 0
    for b in x:
        dist += sum([1 for bit in bin(b) if bit == '1'])
    return dist
