#!/usr/bin/env python

## Nested function

def hello_world(str):
    def print_upper(s):
        return s.upper()

    print(print_upper(str))

hello_world("mango")
