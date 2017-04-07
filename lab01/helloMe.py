#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group Members: none
 
"""
This is my first program in python, prints out my name.
""" 
 
class Announcer(str):
    def printMe(self):
        print(self)

student = Announcer('Hello Carlos Barillas')
#prints out student name using printMe method from announcer class
student.printMe()
