"""
c03.py
"""

import cryptopals.xor as xor
import cryptopals.scoring as scoring


def main():
    bs = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78' +
            '373e783a393b3736')

    # Run the break single byte xor function and print the output.
    scorer = scoring.Scorer(2)
    r = xor.break_single_byte_xor(bs, scorer)
    print(r)
