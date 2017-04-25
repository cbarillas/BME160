#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group: none


class ProteinParam(str):
    """Creates a ProteinParam string object in upper case letters. 
    
    Attributes:
        attr1 (dict): Dictionary of molecular weights of amino acids.
        attr2 (float): Molecular weight of H20.
        attr3 (dict): Dictionary of absorbance values at 280nm.
        attr4 (dict): Dictionary of positively charged amino acids.
        attr5 (dict): Dictionary of negatively charged amino acids.
        attr6 (float): Charge of the N terminus.
        attr7 (float): Charge of the C terminus.
        attr8 (dict): Dictionary of valid aa's.
    """

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

    def __init__(self, protein):
        """Takes in sequence from users input then creates a list of 
        strings and concatnates to create a string object. 
        Then creates aaDictionary with the keys being the valid aa's of 
        users input and the value of each one being their corresponding count.

        Args:
            param1 (str): String of amino acids. 
        """
        myList = ''.join(protein).split()
        print(myList)
        self.proteinString = ''.join(myList).upper()
        
        for aa in self.aa2mw.keys(): 
            self.aaDictionary[aa] = float(self.proteinString.count(aa))

    def aaCount(self):
        """ Iterates through every character in string and returns a count of valid 
        amino acids. Ignores invalid characters.
        
        Returns:
            aaTotal (int): Total number of valid amino acids.  
        """
        aaTotal = 0
        for aa in self.proteinString:
            if aa.upper() in self.aa2mw.keys():
                aaTotal += 1
        return aaTotal

    def pI(self):
        """Estimates the theoretical isoelectric point by finding the 
        particular pH that yeilds a neutral net charge (as close to 
        zero as possible, accurate to two decimal places).

        Returns:
            (float): Best pH.
        """
        bigCharge = 2**11
        bestPH = 0
        particularPH = 0
        while particularPH < 14.01:
            charge = self.charge(particularPH)
            if charge < bigCharge:
                bigCharge = charge
                bestPH = particularPH
            particularPH += 0.01  # Needs to iterate through every pH in decimal places.
        return bestPH

    def aaComposition(self):
        """ 
        Returns: 
            aaDictionary created in __init__ method.
        """
        return self.aaDictionary

    def charge(self, pH):
        """Calculates the net charge on the protein at specific pH using pKa of each
        charged amino acid, Nterminus and Cterminus.
        Args:
            param1 (float): pH value from pI method.
        Returns:
            (float): Net charge of the protein.
        """
        posCharge = 0
        for aa in self.aa2chargePos:
            nAA = self.aaDictionary[aa]
            posCharge += nAA * ((10**self.aa2chargePos[aa]) /
            (10**self.aa2chargePos[aa] + 10**pH))
        posCharge += (10**self.aaNterm) / (10**self.aaNterm + 10**pH)

        negCharge = 0
        for aa in self.aa2chargeNeg:
            nAA = self.aaDictionary[aa]
            negCharge += nAA * ((10**pH) /
            (10**self.aa2chargeNeg[aa] + 10**pH))
        negCharge += (10**pH) / (10**self.aaCterm + 10**pH)

        netCharge = abs(posCharge - negCharge)

        return netCharge

    def molarExtinction(self):
        """Estimates the molar extinction coefficient based on the number
        of tyrosines, tryptophans, cysteines and their extinction 
        coefficient at 280nm which can be found in dictionary(aa2abs280).

        Returns:
            (float): Molar extinction coefficient.
        """
        tyrosine = self.aaDictionary['Y'] * self.aa2abs280['Y']
        tryptophans = self.aaDictionary['W'] * self.aa2abs280['W']
        cysteines = self.aaDictionary['C'] * self.aa2abs280['C']
        molarEx = tyrosine + tryptophans + cysteines
        return molarEx

    def massExtinction(self):
        """Computes mass extinction by dividing molar extinction
        by the molecular weight of corresponding protein.

        Returns:
            (float): Mass extinction value.
        """
        myMW = self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight(self):
        """Calculates the molecular weight of the protein sequence by summing
        the weights of the individual Amino acids and excluding the waters 
        that are released with peptide bond formation.

        Returns:
            (float): Molecular weight.
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
        print("\t{} = {:.2%}".format(key, myAAcomposition[key]/myAAnumber))
