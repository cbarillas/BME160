#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class DNAString(str):
    """
    DNAString class returns a string object in upper case letters
    Keyword arguments:
    sequence -- DNA sequence user enters
    """
    def __new__(self,sequence):
        """Returns a copy of sequence in upper case letters"""
        return str.__new__(self,sequence.upper())

    def removeN(self):
        """Returns length of sequence"""
        return len(self)

    def getN(self):
        """Returns the number of N's in the sequence"""
        num_N = self.count("N")
        return num_N
        


"""
Builds a new DNAString object based on what the user inputs
Prints the total 
"""
DNA = input("Enter a DNA sequence: ")
seq = DNAString(DNA)
print("Your sequence contains {0} ambiguous bases".format(seq.getN()))

