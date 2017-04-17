#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class FastqParse(str):
    """
    FastqParse class takes a string object and returns a sliced string object.
    Keyword arguments:
    sequence -- Single line of a FASTQ file.
    """
    def __new__(self, sequence):
        """Slices sequence & returns a string object w/o '@' symbol."""
        return str.__new__(self, sequence[1:])

    def parseSequence(self):
        """Splits string based on ':' delimiter. Prints out info."""
        parsedSeq = self.split(":")
        instr, rid, fcid, fcl, tnum, x, y = parsedSeq
        print('Instrument = '+instr+'\nRun ID = '+rid+
              '\nFlow Cell ID = '+fcid+'\nFlow Cell Lane = '+fcl+
              '\nTile Number = '+tnum+'\nX-coord ='+x+'\nY-coord = '+y)

"""
Builds a new string object of FastqParse class based on what the user inputs.

Parses out each field of the run information from the string and displays 
each of them on a new line.
"""
seqName = input("Enter a single line of a FASTQ formatted file: ")
seq = FastqParse(seqName)
seq.parseSequence()
