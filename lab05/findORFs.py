#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group: None
# compile: $ python3 findORFs.py -lG -s 'ATG' -mG 300 <tass2.fa >tass2ORFdata-ATG-100.txt


########################################################################
# PseudoCode:
#
# ORFfinder class attributes: start_pos list and stop_pos list.
#
# init:
#     seq = DNA from FASTA
#     ORFs = list of ORFs found
# 
# findOrf:
#     for frame from 1 to 3
#         for i from frame = 1 to len(seq) with a step of 3:
#             codon = slice seq
#             if codon is start:
#                 save start position in ORFs list
#             if foundStart codon and foundStop codon:
#                  start = ORFs[0]
#                  stop = i + 3
#             if haven't foundStart but we foundStop codon:
#                  start = 1
#                  stop = i + 3
#          if foundStart codon but haven't foundStop:
#              start = ORFs[0]
#              stop = length of seq
#
#
# findRevOrfs:
#     take reverse complement of DNA seq and do the same as findOrf on reverseComplement string
#
# saveOrf:
#     append the [frame, start, stop, length] of given ORF to our ORF list.
#     ORFs.append([frame, start, stop, length])
#
# reverseComplement:
#     helper method to take the reverse complement of DNA seq.
#
# main method:   
# create fasta object
#     for header, seq in readFasta():
#          print header
#          create Orf finder object with seq as the parameter.
#          findOrfs of ORF finder obj
#          findRevOrfs of ORF finder obj
#          remove ORFS if length < minGene.args 
#          for frame, start, stop, length in sorted & filteredList: 
#              print(frame, start, stop, length)

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
            description='Finds the largest ORF in a DNA sequence',
            epilog='Program epilog - some other stuff you feel compelled to say',
            add_help=True,  # default is True
            prefix_chars='-',
            usage='%(prog)s [options] -option1[default] <input >output'
            )
        self.parser.add_argument('-lG', '--longestGene', action='store_true', help='longest Gene in an ORF')
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
    """
    Takes in a sequence of a FASTA file and stores ORFs in a lists of lists. 
    Attributes:
        attr1 (list): List of valid stop codons.
        attr2 (list): List of valid start codon.
        attr3 (dict): Dictionary of valid nucleotides.
    """
    stop_codons = ['TGA', 'TAG', 'TAA']
    start_codons = ['ATG']
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    def __init__(self, seq):
        """Takes in sequence from users input file then creates a list of 
        lists. 
        Then creates ORFs list  which holds the frame, start, stop, length of the ORF. 
        Args:
            param1 (str): String of DNA from FASTA file.
        """
        self.seq = seq
        self.orfs = []  # The lists where we save lists of ORFS and their position/length/frame.

    def findOrfs(self):
        """
        Find Orfs on top strand and return list of Orfs.
        Returns:
            (list): list of lists of ORFs found.
        """
        start_positions = []
        foundStart = 0
        foundCodon = 0

        for frame in range(0,3):  # We need to check for frames 1, 2, 3
            foundStart = 0  # Flag name for when finding codons and start codons.
            foundCodon = 0
            start_positions = []  # Clears the start position list for each frame.
            for i in range(frame, len(self.seq), 3):
                codon = self.seq[i:i+3]  # The codon is 3 nucleotides.
                if codon == 'ATG':  # When start codon is found.
                    start_positions.append(i)
                    foundStart = 1
                    foundCodon = 1
                
                if codon in OrfFinder.stop_codons and foundStart:
                    #print('ORF found')
                    start = start_positions[0] + 1 - frame
                    stop = i + 3
                    length = stop - start + 1
                    self.saveOrf((frame%3) + 1, start, stop, length)
                    start_positions = []
                    foundStart = 0
                    foundCodon = 1

                if not foundCodon and codon in OrfFinder.stop_codons:  # If no start codon was found but stop codon found.
                    #print("Dangling stop at 5' end")
                    start = 1
                    stop = i + 3
                    length = stop - start + 1
                    self.saveOrf((frame%3) + 1, start, stop, length)
                    start_positions = []
                    foundCodon = 1

            if foundStart:  # If no stop codon was found but start codon was found.
                #print("Dangling start at 3' end")
                start = start_positions[0] + 1
                stop = len(self.seq)
                length = stop - start + 1
                self.saveOrf((frame%3) + 1, start, stop, length)
                
        return self.orfs

    def findRevOrfs(self):
        """ Find Orfs on the bottom strand and returns that list of Orfs.
        Remember to fixup the orfList so that it refers to top strand coordinates and the rev frames.
        Returns:
            (list): list of lists of ORFs found on the reverse complement.
        """
        reverseComp = self.reverseComplement()
        start_positions = []
        foundStart = 0
        foundCodon = 0

        for frame in range(0, 3):  # We need to check for frames 1, 2, 3
            foundStart = 0  # Flag name for when finding codons and start codons.
            foundCodon = 0
            start_positions = []  # Clears the start position list for each frame.
            for i in range(frame, len(reverseComp), 3):
                codon = reverseComp[i:i + 3]  # The codon is 3 nucleotides.

                if codon == 'ATG':  # When start codon is found.
                    start_positions.append(i)
                    foundStart = 1
                    foundCodon = 1

                if codon in OrfFinder.stop_codons and foundStart:  # We have a start and stop codon.
                    stop = len(reverseComp) - start_positions[0]
                    start = len(reverseComp) - (i+2)
                    if frame == 1: stop += 1  # I'm not sure about this part.
                    elif frame == 2: stop += 2
                    length = stop - start + 1
                    self.saveOrf(-1 * ((frame%3) + 1), start, stop, length)
                    start_positions = []
                    foundStart = 0
                    foundCodon = 1

                if not foundCodon and codon in OrfFinder.stop_codons:  # If no start codon was found but stop codon found.
                    #print("Dangling stop at 5' end")
                    start = len(reverseComp) - i - 2
                    stop = len(reverseComp)
                    length = stop - start + 1
                    self.saveOrf(-1 * ((frame%3) + 1), start, stop, length)
                    start_positions = []
                    foundCodon = 1

            if foundStart:  # If no stop codon was found but start codon was found.
                #print("Dangling start at 3' end")
                start =  start_positions[0] + 1
                stop = 1
                length = stop - start + 1
                self.saveOrf(-1 * ((frame%3) + 1), start, stop, length)
                
        return self.orfs

    def saveOrf(self, frame, start, stop, length):
        """ Saves the information about the ORF that was found.
        This method is used in findOrfs and findRevOrfs.
        Args:
            param1 (int): Start position.
            param2 (int): Stop position.
            param3 (int): Length of my Orf. (Stop - Start)
            param4 (int): Which frame my Orf was found in.
        Returns:
            (list): A list of lists of Orfs with their appropriate information.
        """
        self.orfs.append([frame, start, stop, length])

    def reverseComplement(self):
        """ Helper method to take the reverse complement of a DNA seqeunce.
        Returns:
            (list): Reverse complement of DNA sequence.
        """
        return ''.join([self.complement[base] for base in self.seq[::-1]])  # Dictionary comprehension to find reverse complement of DNA sequence.

########################################################################
# This is my main program.
########################################################################
import sequenceAnalysis

def main(myCommandLine=None):
    """Reads in a fasta file and outputs the ORFs frame, start, stop, and length position on a output file."""
    if myCommandLine is None:
        myCommandLine = CommandLine()
        if myCommandLine.args.longestGene:  # If the terminal sees lG flag variable start this part of code.
            fastaFile = sequenceAnalysis.FastAreader()
            for header, sequence in fastaFile.readFasta():
                print(header)
                orfData = OrfFinder(sequence)
                orfData.findOrfs()
                orfData.findRevOrfs()
                filteredList = filter(lambda orf: orf[3] > myCommandLine.args.minGene, orfData.orfs)  # Filters out the ORFS depending on the minGene arg.
                for frame, start, stop, length in sorted(filteredList, key=lambda orf: orf[3], reverse = True):  # Unzips filteredList and sorts the list by length. 
                    print('{:+d} {:>5d}..{:>5d} {:>5d}'.format(frame, start, stop, length))
    else:
        myCommandLine = CommandLine(myCommandLine)
  

if __name__ == "__main__":
    main()
