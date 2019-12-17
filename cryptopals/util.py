"""
util.py
"""


def hamming_distance(b1, b2):
    """
    Calculates the hamming distance in bits, between two byte arrays.
    """
    # Ensure that both byte arrays are the same length.
    if len(b1) != len(b2):
        raise Exception('Byte arrays are not of equal length.')

    # Calculate the hamming distance.
    x = bytearray([a ^ b for a, b in zip(b1, b2)])
    return sum(sum([1 for bit in bin(b) if bit == '1']) for b in x)

