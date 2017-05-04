import sequenceAnalysis

class GenomeAnalyzer:

    def __init__(self):
        """
        Instantiates two objects. One of FastAreader class and one of NucParams.
        FastAreader object reads fasta file and NucParams does the counting of the
        sequences inside fasta file.
        """
        self.fastaFile = sequenceAnalysis.FastAreader('testGenome.fa')
        self.sequence = sequenceAnalysis.NucParams()

    def analyze(self):
        """ Analyzes each sequence of fasta file and prints out information about it. """
        megaBP = 0
        for header, sequence in self.fastaFile.readFasta():  # Adds sequences to dictionaries.
            self.sequence.addSequence(sequence)

        gc = self.sequence.nucComposition['G']+self.sequence.nucComposition['C']/self.sequence.nucCount()  # GC content.
        megaBP = self.sequence.nucCount() * 1 / 1000  # Kishwar said to divide by 1,000
        print('Sequence length = {0:.2f} Mb\n'.format(megaBP))
        print('GC Content = {:.1f} %\n'.format(gc*100))

        for codon in sorted(self.sequence.codonComposition):
            print('{:s} : {:s} ({:6d})'.format(codon, self.sequence.rnaCodonTable[codon], self.sequence.codonComposition[codon]))


def main():
    mySequence = GenomeAnalyzer()
    mySequence.analyze()
main()