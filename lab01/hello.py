#!/usr/bin/env python3
# Carlos Barillas(cbarilla)
# Group Members: none
 
"""
This is a demonstration program that prints out the most common statement in computer programming, Hello World!
""" 
 
class announcer (str):
    def printMe (self):
        print (self)
 
student = announcer ('Hello World')
student.printMe()
