#!/usr/bin/env python3
# Carlos Barillas (cbarilla)
# Group Members: none
 
"""
This is my first program in python, prints out my name.
""" 
 
class Announcer(str):
    """
    Announcer class inherits from str class
    """
    def printMe(self):
        """Print method belonging to Announcer class, prints string"""
        print(self)

student = Announcer('Hello Carlos Barillas')
"""Prints out student name using printMe method from announcer class"""
student.printMe()
