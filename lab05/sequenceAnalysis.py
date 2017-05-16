#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group: none

class NucParams:
    """Creates dictionaries to store fasta file information.

        Attributes:
            attr1 (dict): Dictionary of RNA codons.
            attr2 (dict): Dictionary of DNA codons.
            attr3 (dict): Dictionary of valid Nucleotides.
    """

    rnaCodonTable = {
                    # RNA codon table
    # U
        'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
        'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
        'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
        'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
        'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
        'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
        'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
        'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
        'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
        'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
        'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
        'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
        'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
        'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
        'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
        'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'   # GxG
    }

    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}

    validNucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0, 'N': 0}

    def __init__(self):
        """
        Initializes dictionaries with appropriate keys, and values set to zero.
        """
        self.aminoAcidComposition = {}
        self.codonComposition = {}
        self.nucComposition = {}

        for aa in ProteinParam.aa2mw:  # Initializes Amino Acid dictionary.
            self.aminoAcidComposition[aa] = 0

        for codon in self.rnaCodonTable:  # Initializes Codon Composition dictionary.
            self.codonComposition[codon] = 0

        for nuc in self.validNucleotides:  # Initializes Nucleotide Composition dictionary.
            self.nucComposition[nuc] = 0

    def addSequence(self, thisSequence):
        """
        This method accepts additional sequences and adds the data that you were given
        with the __init__ method.
        """
        for nuc in thisSequence:
            if nuc in self.validNucleotides.keys():  # Checks if each nucleotide is valid.
                self.nucComposition[nuc] += thisSequence.count(nuc)  # Counts how many nucleotides there are.

        rnaSequence = thisSequence.replace('T', 'U')  # Converts DNA sequence to RNA

        for start in range(0, len(rnaSequence), 3):
            codon = rnaSequence[start: start + 3]
            if codon in self.rnaCodonTable:
                self.codonComposition[codon] += 1  # Adds RNA sequence to dictionary w/ count.
                aa = self.rnaCodonTable[codon]
                if aa != '-':
                    self.aminoAcidComposition[aa] += 1  # Adds amino acid to dictionary w/ count.


    def aaComposition(self):
        """
        This method will return a dictionary of counts over the 20 amino acids.
        """
        return self.aminoAcidComposition

    def nucComposition(self):
        """
        Returns the updated nucleotide composition dictionary from addSequence.
        """
        return self.nucComposition

    def codonComposition(self):
        """
        This dictionary returns codons in RNA format and counts of codon.
        """
        return self.codonComposition

    def nucCount(self):
        """
        This returns an integer value, summing every valid nucleotide found. This 
        value should exactly equal the sum over the nucleotide composition dictionary. 
        """
        nucTotal = 0
        for count in self.nucComposition.values():
            nucTotal += count
        return nucTotal


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
        self.proteinString = ''.join(myList).upper()

        for aa in self.aa2mw.keys():  # Iterates through aa2mw dictionary, the valid aa's.
            self.aaDictionary[aa] = float(self.proteinString.count(aa))  # Stores values.

    def aaCount(self):
        """ Iterates through every character in string and returns a count of valid 
        amino acids. Ignores invalid characters.

        Returns:
            aaTotal (int): Total number of valid amino acids.  
        """
        aaTotal = 0
        for aa in self.proteinString:
            if aa.upper() in self.aa2mw.keys():  # Checks if character in string is a valid aa.
                aaTotal += 1
        return aaTotal

    def pI(self):
        """Estimates the theoretical isoelectric point by finding the 
        particular pH that yeilds a neutral net charge (as close to 
        zero as possible, accurate to two decimal places).

        Returns:
            (float): Best pH.
        """
        bigCharge = 2 ** 11  # Choose a big number, this is our loop invariant.
        bestPH = 0
        particularPH = 0
        while particularPH < 14.01:
            charge = abs(self.charge(particularPH))  # 0 <= charge <= 14
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
        for aa in self.aa2chargePos:  # Begin summation for posCharges.
            nAA = self.aaDictionary[aa]
            posCharge += nAA * ((10 ** self.aa2chargePos[aa])
                                / (10 ** self.aa2chargePos[aa] + 10 ** pH))
        posCharge += (10 ** self.aaNterm) / (10 ** self.aaNterm + 10 ** pH)  # Include the Nterm to posCharge.

        negCharge = 0
        for aa in self.aa2chargeNeg:
            nAA = self.aaDictionary[aa]
            negCharge += nAA * ((10 ** pH)
                                / (10 ** self.aa2chargeNeg[aa] + 10 ** pH))
        negCharge += (10 ** pH) / (10 ** self.aaCterm + 10 ** pH)

        netCharge = posCharge - negCharge

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
        h2o = self.mwH2O * (self.aaCount() - 1)
        for aa, count in self.aaDictionary.items():
            aaWeight += (count * self.aa2mw[aa])  # Sums the weights of the individual aa's.
        return aaWeight - h2o  # Excludes the h2o's released with peptide bond formation.


import sys

class FastAreader:
    
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
 
    def readFasta (self):
        
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
 
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                line = fileH.readline()
            header = line[1:].rstrip()
 
            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()
 
                 
        yield header,sequence