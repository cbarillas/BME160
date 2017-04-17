#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

from math import *
class Triad:
    """
    This class calculates angles and distances among a triad of points.
    Points can be supplied in any dimensional space as long as they are
    consistent.
    Points are supplied as tupels in n-dimensions, and there should be
    three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()
    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
    p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods: angleQ() angles measured in degrees
    dPQ(), dQR() distances in the same units of p,q,r
    """
    def __init__(self, p, q, r):
        """ Construct a Triad.
        p1 = Triad(p=(1,0,0), q=(0,0,0), r=(0,0,0)).
        """
        self.p = p
        self.q = q
        self.r = r
    
    # Private helper methods.
    def d2(self, a, b):
        """Calculate squared distance of point a to b"""
        return float(sum((ia-ib)*(ia-ib) for ia,ib in zip (a,b))) 

    def ndot(self, a, b, c):
        """Dot Product of vector a, c standardized to b."""
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))

    # Calculate lengths(distances) of segments PQ and QR.
    def dPQ(self):
        """Provides the distance between point p and point q."""
        return sqrt(self.d2(self.p, self.q))

    def dQR(self):
        """Provides the distance between point q and point r."""
        return sqrt(self.d2(self.q, self.r))

    # Calculates the angles in degrees for angleQ
    def angleQ(self):
        """Provides the angle made at point q by segments qp and qr
        (degrees)."""
        return acos(self.ndot(self.p, self.q, self.r) /
        sqrt(self.d2(self.p, self.q)*self.d2(self.r, self.q))) * 180/pi

coordinates = input("Enter three sets of atomic coordinates: \n")
leftP = coordinates.replace( '(', ',')
rightP = leftP.replace (')', ',')
myList = rightP.split (',')

p = (float(myList[1]),float(myList[2]), float(myList[3]) )
q = (float(myList[5]),float(myList[6]), float(myList[7]) )
r = (float(myList[9]),float(myList[10]), float(myList[11]) )

triad = Triad(p, q, r)

print('N-C bond length = {0:.2f} \nN-Ca bond length = {1:.2f} \nC-N-Ca bond' \
      ' angle = {2:.1f}'.format(triad.dPQ(), triad.dQR(), triad.angleQ()))
 
