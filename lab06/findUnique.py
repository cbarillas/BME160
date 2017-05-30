#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group: none
# compile: $ python3 findUnique.py <tass2.fa 

import sequenceAnalysis as SA
from itertools import chain, combinations

class findUnique:
    def __init__(self, tRNA):
        """
        """
        self.tRNA = tRNA
        #self.trnaList = []  do i need this?
        
    def substring(self, sequence):
        """
        Generator that yields the substrings for each tRNA sequence,
        without duplicates.
        Ex: 'ABABC' = ['A', 'B', 'C',
                      'AB', 'BC'
                      'ABA', 'BAB', 'ABC',
                      'ABAB', 'BABC',
                      'ABABC']
        """
        seen = set()
        for size in range(1, len(sequence)+1):
            for index in range(len(sequence)+1-size):
                substring = sequence[index:index+size]
                if substring not in seen:
                    seen.add(substring)
                    yield substring
    




def main():
    # Initalize names
    fastaFile = SA.FastAreader('bos-tRNA-7.fa')
    powersetList = []  # List to store the powerSet of each tRNA sequence
    powersetDictionary = {} # Dictionary to store the powerSet of each tRNA sequence


    
    for header, sequence in fastaFile.readFasta():  # Reads fasta file and yields header/sequence.
        obj = findUnique(sequence)  # Instantiates a new object of findUnique class.
        powerSet = set()
        print(header)
        for substring in obj.substring(obj.tRNA):  # Gets substring of each tRNA sequence.
            powerSet.add(substring)  # Adds substring to powerSet set.
            powersetDictionary[sequence] = powerSet # key = tRNA sequence, value = their powerset.
        powersetList.append(powerSet)  # Adds each powerSet of each tRNA sequence to a list.
        
    uniques = []
    for i in range(len(powersetList)):
        compList =  powersetList[0:i]+powersetList[i+1:-1]
        comp = set.union(*compList)
        tRNAps = powersetList[i]
        uniques.append(set.difference(tRNAps, comp))
    for i in uniques:
         print(i)
    
        
        
if __name__ == "__main__":
    main()
