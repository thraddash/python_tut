#!/usr/bin/env python

# Lifecycle2

class X:
    def __init__(self,name):
        self.name = name
        print(self.name + " created")
    def __del__(self):
        print(self.name + " is destroyed")

# new function hello
# with 2 objects X, Y 
# call function hello
# once function is completed, object are destroyed

def hello():
    x = X('hello_X') 
    y = X('hello_Y') 
hello()
print("blah blah")

# output
# hello_X created
# hello_Y created
# hello_X is destroyed
# hello_Y is destroyed
# blah blah

# X, Y ref =1, after function is done ref 0
# any instance or variable ref 0, garbage collection will remove from memory

