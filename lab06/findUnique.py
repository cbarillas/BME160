#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group: none

import sequenceAnalysis as SA

class findUnique:

    def __init__(self):
        """
        Instantiates two objects. One of FastAreader class and one of NucParams.
        FastAreader object reads fasta file and NucParams does the counting of the
        sequences inside fasta file.
        """
        self.myReader = SA.FastAreader()
        
