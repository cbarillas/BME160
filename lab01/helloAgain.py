#!/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none
 
 
"""
This is a demonstration program that shows off some basic interactive features
of a python program. The program asks the user to enter a name, builds an object
with that name, and then has the new object introduce itself.
 
input: a string of arbitrary length, which is used to name the new person object
output: greeting printed to screen
"""
 
class Person:
    def __init__(self,name,pet):
        self.myName = name
        self.myPet = pet

    def introduce(self):
        print("Hi there, I am {0} and I like {1}".format(self.myName,self.myPet))


name = input( "What is my name? : " ) 
pet = input( "What is my favorite kind of pet? : ")

newPerson = Person(name, pet)
newPerson.introduce()
