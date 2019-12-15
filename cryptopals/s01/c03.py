"""
c03.py
"""

from cryptopals import xor, scoring


def main():
    bs = bytearray.fromhex('1b37373331363f78151b7f2b783431333d78397828372d36' +
            '3c78373e783a393b3736')

    # Run the break single byte xor function and print the output.
    scorer = scoring.Scorer(2)
    r = xor.break_single_byte(bs, scorer)
    print r
