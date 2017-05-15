#!/usr/bin/env python3
########################################################################
# CommandLine
########################################################################
class CommandLine():
    """
    Handle the command line, usage and help requests.

    CommandLine uses argparse, now standard in 2.7 and beyond. 
    it implements a standard command line argument parser with various argument options,
    a standard usage and help, and an error termination mechanism do-usage_and_die.

    attributes:
    all arguments received from the commandline using .add_argument will be
    avalable within the .args attribute of object instantiated from CommandLine.
    For example, if myCommandLine is an object of the class, and requiredbool was
    set as an option using add_argument, then myCommandLine.args.requiredbool will
    name that option.
    """
    def __init__(self, inOpts=None):
        """
         CommandLine constructor.
        Implements a parser to interpret the command line argv string using argparse.
        :param inOpts: 
        """
        import argparse
        self.parser = argparse.ArgumentParser(
            description='Program prolog - a brief description of what this thing does',
            epilog='Program epilog - some other stuff you feel compelled to say',
            add_help=True,  # default is True
            prefix_chars='-',
            usage='%(prog)s [options] -option1[default] <input >output'
            )
        self.parser.add_argument('-lG', '--longestGene', action='store', nargs='?', const=True, default=False,
                                 help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices=(100, 200, 300, 500, 1000), action='store',
                                 help='minimum Gene length')
        self.parser.add_argument('-s', '--start', action='append', nargs='?',
                                 help='start Codon')  # allows multiple list options
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
        if inOpts is None:
            self.args = self.parser.parse_args()
        else:
            self.args = self.parser.parse_args(inOpts)

class OrfFinder():
    stop_codons = ['TGA', 'TAG', 'TAA']
    start_codons = ['ATG']
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    def __init__(self, seq):
        self.seq = seq
        self.orfs = []

    def findOrfs(self):
        """
        find Orfs on top strand and return list of Orfs
        remember to handle the dangling start and stop cases
        """
        start_positions = []
        foundStart = 0
        foundCodon = 0

        for frame in range(0,3):  # We need to check for frames 1, 2, 3
            foundStart = 0        # Flag name for when finding codons and start codons.
            foundCodon = 0
            start_positions = []  # Clears the start position list for each frame.
            for i in range(frame, len(self.seq), 3):
                codon = self.seq[i:i+3]  # The codon is 3 nucleotides.
                if codon == 'ATG':  # When start codon is found.
                    start_positions.append(i)
                    foundStart = 1
                    foundCodon = 1
                
                if codon in OrfFinder.stop_codons and foundStart:
                    start = start_positions[0]
                    stop = i
                    length = stop - start
                    self.saveOrf(start,stop,length,frame)
                    start_positions = []
                    foundStart = 0
                    foundCodon = 1

                if foundCodon == 0 and codon in OrfFinder.stop_codons:  # If no start codon was found but stop codon found.
                    #print("dangling stop at 5' end")
                    start = 0
                    stop = i
                    length = stop - start
                    self.saveOrf(start, stop, length, frame)
                    start_positions = []
                    foundCodon = 1

            if foundStart:  # If no stop codon was found but start codon was found.
                start = start_positions[0]
                stop = len(self.seq)
                length = stop - start
                self.saveOrf(start, stop, length, frame)
                #print("dangling start at 3' end")
        return self.orfs

    def reverseComp(self):
        """ Helper method to take the complement of a DNA seqeunce.
        :return: Complement of DNA.
        """
        return ''.join([self.complement[base] for base in self.seq[::-1]])  # Dictionary comprehenesion to find complement of DNA sequence.

    def findRevOrfs(self):
        """ Find Orfs on the bottom strand and return that list of Orfs
        remember to fixup the orfList so that it refers to top strand coordinates and the rev frames
        :return: 
        """
        comp = self.reverseComp()
        start_positions = []
        foundStart = 0
        foundCodon = 0

        for frame in range(0, 3):  # We need to check for frames 1, 2, 3
            foundStart = 0  # Flag name for when finding codons and start codons.
            foundCodon = 0
            start_positions = []  # Clears the start position list for each frame.
            for i in range(frame, len(comp), 3):
                codon = comp[i:i + 3]  # The codon is 3 nucleotides.
                if codon == 'ATG':  # When start codon is found.
                    start_positions.append(i)
                    foundStart = 1
                    foundCodon = 1

                if codon in OrfFinder.stop_codons and foundStart:
                    start = start_positions[0]
                    stop = i
                    length = stop - start
                    self.saveOrf(start, stop, length, frame)
                    start_positions = []
                    foundStart = 0
                    foundCodon = 1

                if foundCodon == 0 and codon in OrfFinder.stop_codons:  # If no start codon was found but stop codon found.
                    #print("Dangling stop at 5' end.")
                    start = 0
                    stop = i
                    length = stop - start
                    self.saveOrf(start, stop, length, frame)
                    start_positions = []
                    foundCodon = 1

            if foundStart:  # If no stop codon was found but start codon was found.
                start = start_positions[0]
                stop = len(comp)
                length = stop - start
                self.saveOrf(start, stop, length, frame)
                #print("Dangling start at 3' end.")
        return self.orfs

    def saveOrf(self, start, stop, length, frame):
        """ Saves the information about the ORF that was found.
        This method is used in findOrfs and findRevOrfs.
        :param start: Start position.
        :param stop: Stop position.
        :param length: Length of my Orf. (Stop - Start)
        :param frame: Which frame my Orf was found in.
        :return: A list of lists of Orfs with their appropriate information.
        """
        self.orfs.append([start, stop, length, frame])

    def print(self):
        """ Helper Method to print out my list of Orfs.
        :return:
        """
        print(self.orfs)


########################################################################
# Main
# Here is the main program
########################################################################
def main(myCommandLine=None):
    """
    Implements the Usage exception handler that can be raised from anywhere in process. 
    """
    seq = OrfFinder('AAAATGAAAAAATCAAAATGAAAAAAATACAAAAAA')
    print(seq.seq)
    seq.findOrfs()
    seq.findRevOrfs()
    print(seq.orfs)

    if myCommandLine is None:
        myCommandLine = CommandLine()
    else:
        myCommandLine = CommandLine(myCommandLine)
        ###### replace the code between comments.
        # myCommandLine.args.inFile = 'tass2.fa'
        # myCommandLine.args.outFile has the output file name
        # myCommandLine.args.longestGene is True if only the longest Gene is desired
        # myCommandLine.args.start is a list of start codons
        # myCommandLine.args.minGene is the minimum Gene length to include
        #


#######

if __name__ == "__main__":
    main()
