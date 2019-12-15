"""
padding.py
"""


def pkcs7(bs, block_size):
    """
    An implementation of pkcs#7 padding.
    """
    # Find the amount needed to pad to correct length.
    pad = block_size - len(bs)%block_size

    # Pad with padding length and return.
    bs = bytearray(bs)
    for _ in range(pad):
        bs.append(pad)
    return bs
