#!/usr/bin/env python

#function treated as objects

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
