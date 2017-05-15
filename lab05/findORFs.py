#!/usr/bin/env python3


########################################################################
# CommandLine
########################################################################
class CommandLine():
    '''
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

    '''

    def __init__(self, inOpts=None):
        '''
        CommandLine constructor.
        Implements a parser to interpret the command line argv string using argparse.
        '''

        import argparse
        self.parser = argparse.ArgumentParser(
            description='Program prolog - a brief description of what this thing does',
            epilog='Program epilog - some other stuff you feel compelled to say',
            add_help=True,  # default is True
            prefix_chars='-',
            usage='%(prog)s [options] -option1[default] <input >output'
            )
        self.parser.add_argument('inFile', action='store', help='input file name')
        self.parser.add_argument('outFile', action='store', help='output file name')
        self.parser.add_argument('-lG', '--longestGene', action='store', nargs='?', const=True, default=True,
                                 help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices=range(0, 2000), action='store',
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

    def findOrfs(self):
        ''' 
        find Orfs on top strand and return list of Orfs

        remember to handle the dangling start and stop cases
        '''
        start_positions = []
        stop_positions = []
        orfs = []
        start_pos = 0
        stop_pos = 0
        
        for frame in range(0,3):  # We need to check for frames 1, 2, 3
            for i in range(frame, len(self.seq), 3):
                codon = self.seq[i:i+3]  # The codon is 3 nucleotides.
                #print(codon)
                if codon == 'ATG':
                    start_pos = i
                    start_positions.append([codon, i])
                
                if codon in OrfFinder.stop_codons:
                    stop_pos = i
                    stop_positions.append([codon, i])
                    length = stop_pos - start_pos
            
                
        print('start:',start_positions)
        print('stop:', stop_positions)
        print(orfs)

    def reverse_complement(self):
        return ''.join([self.complement[base] for base in self.seq[::-1]])  # Dictionary comprehenesion to find complement of DNA sequence.

    def findRevOrfs(self):
        ''' 
        find Orfs on the bottom strand and return that list of Orfs

        remember to fixup the orfList so that it r	efers to top strand coordinates and the rev frames

        '''
        complement = reverse_complement(self.seq)
        pass

    def saveOrf(self, start, stop, length, frame):

        pass


########################################################################
# Main
# Here is the main program
#
#
########################################################################


def main(myCommandLine=None):
    '''
    Implements the Usage exception handler that can be raised from anywhere in process.  

    '''
    orf = OrfFinder('ACTAAGG')
    orf.findOrfs()
    orfc = orf.reverse_complement()
    print(orfc)






    
    if myCommandLine is None:
        myCommandLine = CommandLine(['tass2.fa',
                                     'tass2ORFdata-ATG-100.txt',
                                     '--longestGene',
                                     '--start=ATG',
                                     '--minGene=100'])
    else:
        myCommandLine = CommandLine(myCommandLine)
        ###### replace the code between comments.
        # myCommandLine.args.inFile has the input file name
        # myCommandLine.args.outFile has the output file name
        # myCommandLine.args.longestGene is True if only the longest Gene is desired
        # myCommandLine.args.start is a list of start codons
        # myCommandLine.args.minGene is the minimum Gene length to include
        #
        import sequenceAnalysis
        myReader = sequenceAnalysis.fastaReader(myCommandLine.args.inFile)


#######

if __name__ == "__main__":
    main()
