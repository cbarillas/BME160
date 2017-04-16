#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class FastQParse(str):
    """
    SequenceCleaner class returns a string object in upper case letters.
    Keyword arguments:
    sequence -- DNA sequence user enters
    """
    def __new__(self, sequence):
        """Returns a copy of sequence without '@'."""
        return str.__new__(self, sequence[1:])

    def parseSequence(self):
        """Splits string based on ':' delimiter. Prints out info."""
        parsedSeq = self.split(":")
        instr, rid, fcid, fcl, tnum, x, y = parsedSeq
        print('Instrument = '+instr+'\nRun ID = '+rid+
              '\nFlow Cell ID = '+fcid+'\nFlow Cell Lane = '+fcl+
              '\nTile Number = '+tnum+'\nX-coord ='+x+'\nY-coord = '+y)
"""
Builds a new string object of SequenceCleaner class based on what the user 
inputs.
Removes the ambiguous parts of the sequence, outputs the “cleaned” 
sequence, replacing the ambiguous parts with a count in {}’s  
"""
seqName = input("Enter a single line of a FASTQ formatted file: ")
seq = FastQParse(seqName)
seq.parseSequence()
