#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none
 
 
"""
Program that prints out information about myself
"""
 
class Person:
    """Iniatializes new human object of Person class with information about themselves"""
    def __init__(self,name,username,status,major,why,interest,experience):
        self.name = name
        self.username = username
        self.status = status
        self.major = major
        self.why = why
        self.interest = interest
        self.experience = experience
        
    def introduce(self):
        """Print an introduction message based on info provided"""
        print("Hi there, I am {0}\nMy username is {1}".format(self.name,self.username))
        print("I am a {0}\nMy major is {1}".format(self.status,self.major))
        print("I'm hoping to {0}\nI'm {1}".format(self.why,self.interest))
        print("I have prior programming experience using {0}".format(self.experience))
 
"""Constant names not part of Person class""" 
name = "Carlos Barillas"
username = "cbarilla"
status = "undergraduate"
major = "Computational Mathematics"
why = "learn Python and how it can be applied to molecular biology"
interest = "interested in gene therapy"
experience = "Assembly, C, Java" 

"""Create object called newPerson with my constant data as paramters and print to stdout"""
newPerson = Person(name,username,status,major,why,interest,experience)
newPerson.introduce()
