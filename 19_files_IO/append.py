#!/usr/bin/env python

a="""
#########################################
# Append text in an existing file
"""
with open('number.txt', 'a') as fobj:
    fobj.write("adding new number \n")

