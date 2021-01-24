#!/usr/bin/env python

# Decorator
# tool for wrapping code around functions or classes (defined blocks)
# allow user to add new functionality to an existing functions or classes
# without modifying its structure.

def decor(decoratedFunc):
    def inner():
        print("Inner Function")
    return inner

def testFunc():
    print("Test Func")

#decorated_func = decor(testFunc)
#decorated_func()

## syntatic sugar
# by writing syntatic sugar before testFunc1,
# testFunct1 automatically pass over to decor function
@decor
def testFunc1():
    print("Test Func1")

testFunc1()
