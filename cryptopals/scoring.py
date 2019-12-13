"""
scoring.py
"""

import csv


class Scorer:
    """ An n-gram based scorer. """

    def __init__(self, n): 
        """
        Instantiates the self.freqs and self.probs dictionaries used for
        scoring given plaintexts.
        """
        self.n = n

        # Read the file's lines into memory.
        fp = open('assets/ngrams/%dgram.csv' % n, 'r')
        rdr = csv.reader(fp)

        # Generate the frequency dictionary.
        self.freqs = {l[0]:int(l[1]) for l in rdr}
        fp.close()

        # Generate the probability dictionary.
        total = sum(self.freqs.values())
        self.probs = {key:(self.freqs[key]/total) for key in self.freqs}


    def score(self, s):
        """
        Scores a given plaintext. The higher the output value, the more like
        english the plaintext is.
        """
        # Convert the text to upper-case as all keys in the dictionary are
        # upper-case values.
        s = s.upper()

        # Return the sum of the probabilities that the characters exist within
        # the english language.
        return sum([self.probs[s[i:i+self.n]] for i in range(len(s)+1-self.n)
            if s[i:i+self.n] in self.probs])
