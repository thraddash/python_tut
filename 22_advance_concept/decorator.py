#!/usr/bin/env python

# Decorator

def decor(decoratedFunc):
    def inner():
        print("Inner Function")
    return inner

def testFunc():
    print("Test Func")

decorated_func = decor(testFunc)
decorated_func()
