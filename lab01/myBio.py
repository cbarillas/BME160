#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none
 
 
"""
Program that prints out information about myself
"""
 
class Person:
    def __init__(self,name,username,status,major,why,interest,experience):
        self.myName = name
        self.myUser = username
        self.myStat = status
        self.myMajor = major
        self.why = why
        self.intrst = interest
        self.exp = experience
        
    def introduce(self):
        print("Hi there, I am {0}\nMy username is {1}".format(self.myName,self.myUser))
        print("I am a {0}\nMy major is {1}".format(self.myStat,self.myMajor))
        print("I'm hoping to {0}\nI'm {1}".format(self.why,self.intrst))
        print("I have prior programming experience using {0}".format(self.exp))
 
# constant names not part of Person class 
name = "Carlos Barillas"
username = "cbarilla"
status = "undergraduate"
major = "Computational Mathematics"
why = "learn Python and how it can be applied to molecular biology"
interest = "interested in gene therapy"
experience = "Assembly, C, Java" 

#create object called newPerson with my const data as paramters and print to stdout
newPerson = Person(name,username,status,major,why,interest,experience)
newPerson.introduce()
