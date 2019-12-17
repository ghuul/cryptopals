"""
padding.py
"""


def pkcs7(bs, block_size):
    """
    An implementation of pkcs#7 padding.
    """
    # Find the amount needed to pad to correct length.
    pad = block_size - len(bs)%block_size
    if pad == 0:
        pad = block_size

    # Pad with padding length and return.
    bs = bytearray(bs)
    for _ in range(pad):
        bs.append(pad)
    return bs


def pkcs7_unpad(bs, block_size):
    """
    An implementation of pkcs#7 unpadding.
    """
    # Check whether valid pkcs#7 padding.
    if not is_pkcs7(bs, block_size):
        raise Exception('Invalid pkcs#7 padding.')

    last = ord(bs[-1])
    return bs[:-last]


def is_pkcs7(bs, block_size):
    """
    Determines if a byte array is pkcs7 padded.
    """
    # Length must be a multiple of the block size.
    if len(bs) % block_size != 0:
        return False

    # Last byte cannot be greater than 15 or less than 1.
    last = ord(bs[-1])
    if last < 1 or last > block_size-1 or last > len(bs):
        return False

    # Check whether all padding is the same byte.
    return len([i for i in bs[-last:] if ord(i) != last]) == 0
