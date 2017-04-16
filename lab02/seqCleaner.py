#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class SequenceClean(str):
    """
    Sequence class returns a string object in upper case letters
    Keyword arguments:
    sequence -- DNA sequence user enters
    """
    def __new__(self,sequence):
        """Returns a copy of sequence in upper case letters"""
        return str.__new__(self,sequence.upper())

    def getN(self):
        """Returns the number of N's in the sequence"""
        num_N = self.count("N")
        return num_N
    
    def removeN(self):
        firstN = self.find("N")
        lastN  = self.rfind("N")+1
        print(self[:firstN]+'{'+str(self.getN())+'}'+self[lastN:])
    
"""
Builds a new DNAString object based on what the user inputs
Replaces the string of  
"""
DNA = input("Enter a DNA sequence: ")
seq = DNAString(DNA)
seq.removeN()
