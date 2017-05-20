#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group: none

import sequenceAnalysis as SA

class GenomeAnalyzer:

    def __init__(self):
        """
        Instantiates two objects. One of FastAreader class and one of NucParams.
        FastAreader object reads fasta file and NucParams does the counting of the
        sequences inside fasta file.
        """
        self.myReader = SA.FastAreader()
        self.thisAnalyzer = SA.NucParams()

    def analyze(self):
        """ Analyzes each sequence of fasta file and prints out information about it. """
        megaBP = 0
        for header, seq in self.myReader.readFasta():  # Adds sequences from fasta file to dictionaries.
            self.thisAnalyzer.addSequence(seq)
            
        try:  # Finds the GC content.
            gc = self.thisAnalyzer.nucleotideComposition['G']+self.thisAnalyzer.nucleotideComposition['C']/self.thisAnalyzer.nucCount()
        except ZeroDivisionError:
            gc = 0

            
        megaBP = self.thisAnalyzer.nucCount() * (1/1000)  # Kishwar said to divide by 1,000 but I think we should divide by 1,000,000
        print('Sequence length = {0:.2f} Mb\n'.format(megaBP))
        print('GC Content = {:.1f} %\n'.format(gc))

        for codon in sorted(self.thisAnalyzer.codonsComposition):
            try:  # Calculates the relative codon frequency for each codon found.
                relativeCF = 100 * self.thisAnalyzer.codonsComposition[codon] / self.thisAnalyzer.aminoAcidComposition[SA.NucParams.rnaCodonTable[codon]]
            except ZeroDivisionError:
                relativeCF = 0
            except KeyError:
                relativeCF = 0
            print('{:s} : {:s} {:5.1f} ({:6d})'.format(codon, self.thisAnalyzer.rnaCodonTable[codon], relativeCF, self.thisAnalyzer.codonsComposition[codon]))


def main():
    """
    Analyzes each genome from fasta file and outputs the mega base pair, gc content and the relative codon frequency of each codon.
    """
    mySequence = GenomeAnalyzer()
    mySequence.analyze()

if __name__ == "__main__":
    main()
