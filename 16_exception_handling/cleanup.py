#!/usr/bin/env python

'''
for line in open("else_block.py"):
    print(line, end="")
'''
with open("else_block.py") as f:
    for line in f:
        print(line, end="")
