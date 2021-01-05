#!/usr/bin/env python

# Function are first-class object
def str_upper(str):
    return str.upper()

# Function passed as argument
# higher order function

def greetings(func):
    greet = func("Welcome, Nice to meet you")
    print(greet)

greetings(str_upper)
