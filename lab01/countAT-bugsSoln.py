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
        
    def length(self):
        """Returns length of sequence"""
        return len(self)

    def getAT(self):
        """Returns the AT content of the sequence""" 
        num_A = self.count("A")
        num_T = self.count("T")
        return ((num_A + num_T)/self.length())

"""
Builds a new DNAString object based on what the user inputs
Prints the AT content of the sequence
"""
DNA = input("Enter a DNA sequence: ")
coolString = DNAString(DNA)
print ("AT content = {:0.3f}".format(coolString.getAT()))
