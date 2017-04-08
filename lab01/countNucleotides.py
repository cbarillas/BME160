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
        return (len(self))

    def getA(self):
        """Returns the number of A's in the sequence"""
        num_A = self.count("A")
        return (num_A)

    def getC(self):
        """Returns the number of C's in the sequence"""
        num_C = self.count("C")
        return (num_C)

    def getG(self):
        """Returns the number of G's in the sequence"""
        num_G = self.count("G")
        return (num_G)

    def getT(self):
        """Returns the number of T's in the sequence"""
        num_T = self.count("T")
        return (num_T)


"""
Builds a new DNAString object based on what the user inputs
Prints the total length of the sequence and the number of each base {total As, Cs, Gs, Ts} found in the sequence
"""
DNA = input("Enter a DNA sequence: ")
coolString = DNAString(DNA)
print("Your sequence is {0} nucleotides long with the following breakdown of bases:".format(coolString.length()))
print("number of A's = {0}".format(coolString.getA()))
print("number of C's = {0}".format(coolString.getC()))
print("number of G's = {0}".format(coolString.getG()))
print("number of T's = {0}".format(coolString.getT()))

