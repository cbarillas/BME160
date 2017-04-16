#!/usr/bin/env python3
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

    def parseString(self):
        """
        First removes '@' symbol 
        Then splits string based on ':' delimiter
        """
        newString = list()
        newString = self[1:]
        parsed = newString.split(":")
        instr,rid,fid,fcl,tnum,x,y = parsed
        print('Instrument = '+instr+'\nRun ID = '+rid+'\nFlow Cell ID = '+fid)
        print('Flow Cell Lane = '+fcl+'\nTile Number = '+tnum+'\nX-coord = '+x)
        print('Y-coord = '+y)
"""
Builds a new string object of SequenceCleaner class based on what the user 
inputs.
Removes the ambiguous parts of the sequence, outputs the “cleaned” 
sequence, replacing the ambiguous parts with a count in {}’s  
"""
DNA = input("Enter a DNA sequence: ")
seq = SequenceCleaner(DNA)
seq.parseString()
