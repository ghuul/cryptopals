"""
xor.py
"""


def fixed_xor(b1, b2):
    """
    XORs two given sets of bytes, of equal length, together.
    """
    # Ensure that bytes arrays are of equal length.
    if len(b1) != len(b2):
        raise "Byte arrays are not of equal length."

    # XOR byte arrays together and return.
    return bytes([b1[i] ^ b2[i] for i in range(len(b1))])


def single_byte_xor(bs, b):
    """
    Implementation of a single-byte XOR cipher.
    """
    # XOR each byte in the array with the single byte and return.
    return bytes([bt ^ b for bt in bs])


def break_single_byte_xor(bs, scorer):
    """
    Breaks a single-byte XOR cipher.
    """
    # For each possible byte, decode the single byte XOR and score the
    # plaintext before appending to array of tuples.
    rets = []
    for i in range(256):
        p = ''.join([chr(v) for v in single_byte_xor(bs, i)])
        rets.append((scorer.score(p), p))

    # Return the plaintex with the highest score.
    rets.sort(key=lambda x: x[0], reverse=True)
    return rets[0]


def detect_single_byte_xor(ctexts, scorer):
    """
    Detects single-byte XOR in a list of single-byte XORed ciphertexts.
    """
    # Find the best result for each ciphertext.
    rets = [break_single_byte_xor(bytes.fromhex(c), scorer) for c in ctexts]
    
    # Return the result with the highest score.
    rets.sort(key=lambda x: x[0], reverse=True)
    return rets[0]


def repeating_key_xor(bs, key):
    """
    Implementation of repeating-key XOR.
    """
    # XOR each byte of the byte array with its appropriate key byte.
    return bytes([bs[i] ^ key[i%len(key)] for i in range(len(bs))])


def break_repeating_key_xor(bs):
    """
    Breaks a repeating-key XOR cipher.
    """
    return bs
