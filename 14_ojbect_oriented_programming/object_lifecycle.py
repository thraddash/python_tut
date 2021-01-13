#!/usr/bin/env python

# Lifecycle

class X:
    def __init__(self, name):
        self.name = name
        print(self.name + " created")
    def __del__(self):
        print(self.name + " is destroyed")

#  lifecycle
x = X('X')
y = X('Y')
print("HELLO WORLD")
# program exited after HELLO WORLD, X and Y is remove from memory with __del__
