import sequenceAnalysis

class GeonomeAnalyzer:

    def __init__(self):
        self.readObject = SA.FastaReader('testGenome.fa')
        self.genome = SA.NucParams()


    def analyze(self):
        for head, seq in self.readObject:
            self.genome.addSequence(seq)
        gc = self.genome.nucDict('G')+self.genome.nucDict('C')



def main():
    fred = GenomeAnalyzer()
    fred.analyze()
main()