#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class SequenceCleaner(str):
    """
    SequenceCleaner class returns a string object in upper case letters.
    Keyword arguments:
    sequence -- DNA sequence user enters
    """
    def __new__(self, sequence):
        """Returns a copy of sequence in upper case letters."""
        return str.__new__(self, sequence.upper())

    def parseSequence(self):
        """
        First removes '@' symbol 
        Then splits sequence based on ':' delimiter
        """
        newSeq = list()
        newSeq = self[1:]
        parsedSeq = newSeq.split(":")
        instr,rid,fid,fcl,tnum,x,y = parsedSeq
        print('Instrument = '+instr+'\nRun ID = '+rid+'\nFlow Cell ID = '+fid)
        print('Flow Cell Lane = '+fcl+'\nTile Number = '+tnum)
        print('X-coord = '+x+'\nY-coord = '+y)
"""
Builds a new string object of SequenceCleaner class based on what the user 
inputs.
Removes the ambiguous parts of the sequence, outputs the “cleaned” 
sequence, replacing the ambiguous parts with a count in {}’s  
"""
seqname = input("Enter a single line of a FASTQ formatted file: ")
seq = SequenceCleaner(seqname)
seq.parseSequence()
