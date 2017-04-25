#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group: none


class ProteinParam(str):
    # These tables are for calculating:
    #     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
    #     absorbance at 280 nm (aa2abs280)
    #     pKa of positively charged Amino Acids (aa2chargePos)
    #     pKa of negatively charged Amino acids (aa2chargeNeg)
    #     and the constants aaNterm and aaCterm for pKa of the respective termini
    #  Feel free to move these to appropriate methods as you like

    # As written, these are accessed as class attributes, for example:
    # ProteinParam.aa2mw['A'] or ProteinParam.mwH2O

    aa2mw = {
        'A': 89.093, 'G': 75.067, 'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225, 'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
    }

    mwH2O = 18.015
    aa2abs280 = {'Y': 1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R': 12.4, 'H': 6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34
    aaDictionary = {}


    # the __init__ method requires a protein string to be provided, either as a
    # string or list of strings that will be concatenated
    def __init__(self, protein):
        myList = ''.join(protein).split()
        self.proteinString = ''.join(myList).upper()
        
        for aa in self.aa2mw.keys():  # Iterates through the aa2mw's keys (valid aa's)
            self.aaDictionary[aa] = self.protString.count(aa)  # Each key has a count as value

    def aaCount(self):
        """ Iterates through every character in string and returns a count of valid 
        amino acids. Ignores invalid characters.
        Returns:
             aaTotal (int): Total number of valid amino acids.  
        """
        aaTotal = 0
        for aa in self.protString:                          # Iterates through each character in string object.
            if aa.upper() in self.aa2mw.keys():  # Checks if character is valid by checking if it's in dictionary aa2mw.
                aaTotal += 1
        return aaTotal


    def pI(self):
        maxCharge = 10000
        bestPH = 0
        PH = 0
        while PH < 14.01:
            charge = self.charge(PH)
            if charge < maxCharge:
                maxCharge = charge
                bestPH = PH
            PH += 0.01
        return bestPH


    def aaComposition(self):
        """ Constructs dictionary consisting of amino acids as keys and the count of each one as values.
        Returns: A dictionary keyed by single letter amino acid code, having 
        associated values that are the counts of those amino acids in the sequence.
        """
        return self.aaDictionary


    def charge(self, pH):

        posCharge = 0
        for aa in self.aa2chargePos:
            nAA = self.aaDictionary[aa]
            posCharge += nAA *((10**self.aa2chargePos[aa])/(10**self.aa2chargePos[aa]+10**pH))
        posCharge += (10**self.aaNterm)/(10**self.aaNterm + 10**pH)

        negCharge = 0
        for aa in self.aa2chargeNeg:
            nAA = self.aaDictionary[aa]
            negCharge += nAA * ((10**pH)/(10**self.aa2chargeNeg[aa]+10**pH))
        negCharge += (10**pH)/(10**self.aaCterm + 10**pH)

        netCharge = abs(posCharge - negCharge)

        return netCharge

    def molarExtinction(self):
        tyrosine = self.aaDictionary['Y'] * self.aa2abs280['Y']
        tryptophans = self.aaDictionary['W'] * self.aa2abs280['W']
        cysteines = self.aaDictionary['C'] * self.aa2abs280['C']
        molarEx = tyrosine + tryptophans + cysteines
        return molarEx


    def massExtinction(self):
        myMW = self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0


    def molecularWeight(self):
        """
        Calculates the MW of the protein sequence. 
        """
        aaWeight = 0
        waterMW = self.mwH2O * (self.aaCount()-1)
        for aa, count in self.aaDictionary.items():
            aaWeight += (count * self.aa2mw[aa])
        return aaWeight - waterMW

# Please do not modify any of the following.  This will produce a standard output that can be parsed
import sys

for inString in sys.stdin:
    myParamMaker = ProteinParam(inString)
    myAAnumber = myParamMaker.aaCount()
    print("Number of Amino Acids: {aaNum}".format(aaNum=myAAnumber))
    print("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
    print("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
    print("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
    print("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
    print("Amino acid composition:")
    myAAcomposition = myParamMaker.aaComposition()
    keys = list(myAAcomposition.keys())
    keys.sort()
    if myAAnumber == 0: myAAnumber = 1  # handles the case where no AA are present
    for key in keys:
        print("\t{} = {:.2%}".format(key,float(myAAcomposition[key])/myAAnumber))
