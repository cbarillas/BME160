#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none
 
 
"""
The program asks the user to enter a name and their favorite pet, builds a Person object
with that name and pet, and then has the new object introduce itself.
 
input: a string of arbitrary length, which is used to name the new Person object
output: greeting printed to screen
"""
 
class Person:
    """
    Model simple humans that have a name and favorite pet

    Keyword arguments:
    name -- the name that the human wants to be known by
    pet -- the humans favorite pet
    """
    def __init__(self,name,pet):
        """Capture the name and pet"""
        self.myName = name
        self.myPet = pet

    def introduce(self):
        """Print an introuction message"""
        print("Hi there, I am {0} and I like {1}".format(self.myName,self.myPet))

"""
Build a new Person object, then tell it to introduce itself and their favorite pet
"""
name = input("What is your name? : ") 
pet = input("What is your favorite pet? : ")
newPerson = Person(name,pet)
newPerson.introduce()
