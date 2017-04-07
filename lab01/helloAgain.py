#!/usr/bin/env python3
# Name: David Bernick(dbernick)
# Group Members: none
 
 
"""
This is a demonstration program that shows off some basic interactive features
of a python program. The program asks the user to enter a name, builds an object
with that name, and then has the new object introduce itself.
 
input: a string of arbitrary length, which is used to name the new person object
output: greeting printed to screen
"""
 
class person:
    def __init__(self,name):
        self.myName = name
        
    def introduce (self):
        print ("Hi there, I am {0}".format(self.myName))
 
 
name = input( "What is my name? : " )
 
newPerson = person (name)
newPerson.introduce()
