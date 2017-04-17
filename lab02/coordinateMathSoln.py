#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

import math
class Triad:
    """
    Author: David Bernick
    Date: March 21, 2013
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
    methods: angleP(), angleR(), angleQ() angles measured in radians
    dPQ(), dPR(), dQR() distances in the same units of p,q,r
    """
    def __init__(self,p,q,r) :
        """ Construct a Triad.
        p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,0,0) ).
        """
        
        self.p = p
        self.q = q
        self.r = r
    
    # private helper methods
    def d2(self,a,b) : # calculate squared distance of point a to b
        return float(sum((ia-ib)*(ia-ib) for ia,ib in zip (a,b)))

    def dot(self,a,b) : # dotProd of standard vectors a,b
        return float(sum(ia*ib for ia,ib in zip(a,b)))

    def ndot(self,a,b,c) : # dotProd of vec. a,c standardized to b
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))

    # calculate lengths(distances) of segments PQ, PR and QR
    def dPQ(self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p,self.q))

    def dPR(self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p,self.r))

    def dQR(self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q,self.r))

    def angleP(self) :
        """ Provides the angle made at point p by segments pq and pr
        (radians). """
        return math.acos(self.ndot(self.q,self.p,self.r) /
        math.sqrt(self.d2(self.q,self.p)*self.d2(self.r,self.p)))
 
    def angleQ(self) :
        """ Provides the angle made at point q by segments qp and qr
        (radians). """
        return math.acos(self.ndot(self.p,self.q,self.r) /
        math.sqrt(self.d2(self.p,self.q)*self.d2(self.r,self.q)))
    
    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq
        (radians). """
        return math.acos(self.ndot(self.p,self.r,self.q) /
        math.sqrt(self.d2(self.p,self.r)*self.d2(self.q,self.r)))

coordinates = input("Enter three sets of coordinates: ")
t1 = coordinates.replace( '(', ',')
t2 = t1.replace (')', ',') # change ) to ,
l = t2.split (',')
p = (float(l[1]),float(l[2]), float(l[3]) )
q = (float(l[5]),float(l[6]), float(l[7]) )
r = (float(l[9]),float(l[10]), float(l[11]) )
#print (p,q,r)
triad = Triad(p,q,r)
print('{0:.2f}'.format(triad.dPQ()))
print('{0:.2f}'.format(triad.dQR())) 
