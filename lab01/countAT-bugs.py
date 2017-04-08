#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none
 
class DNAString(str):
    def __new__(self,s):
        return str.__new__(self,s.upper())
      
    def length(self):
        return (len(self))

    def getAT(self):
        num_A = self.count("A")
        num_T = self.count("T")
        return ((num_A + num_T)/ self.length() )

 
DNA = input("Enter a DNA sequence: ")
coolString = DNAString(DNA)
 
print ("AT content = {:0.3f}".format(coolString.getAT()) )
