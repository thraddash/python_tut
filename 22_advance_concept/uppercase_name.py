#!/usr/bin/env python
a="""
def person_name(name):
    return name

upper_name = person_name("John Wick")
print(upper_name)
"""
def person_name(name):
    return name

upper_name = person_name("John Wick")
print(a)
print(upper_name)
b="""
##################################################
covert output to uppercase
change person_name during runtime using decorator

def uppercase(function):
    def decorated(*args):
        result = function(*args)
        result_upper = result.upper()
        return result_upper
    return decorated

@uppercase
def person_name(name):
    return name

upper_name = person_name("John Wick")
print(upper_name)
"""

def uppercase(function):
    def decorated(*args):
        result = function(*args)
        result_upper = result.upper()
        return result_upper
    return decorated

@uppercase
def person_name(name):
    return name

upper_name = person_name("John Wick")
print(b)
print(upper_name)

