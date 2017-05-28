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
        self.trnaList = []
        
    def substring(self, iterable):
        s = tuple(iterable)
        seen = set()
        for size in range(1, len(s)+1):
            for index in range(len(s)+1-size):
                slc = iterable[index:index+size]
                if slc not in seen:
                    seen.add(slc)
                    yield slc
    




def main():
    
    fastaFile = SA.FastAreader('bos-tRNA-7.fa')
    for header, sequence in fastaFile.readFasta():
        obj = findUnique(sequence)
        for result in obj.substring(obj.tRNA):
            obj.trnaList.append(set(result))
            print(obj.trnaList)
        
        
if __name__ == "__main__":
    main()
