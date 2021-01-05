#!/usr/bin/env python

#Return value

def square(num):
    return num * num

print(square(2), square(2.2), sep='|')

def get_name(first_name, last_name):
    return first_name + " " + last_name

print(get_name('Bill', 'Gates'))
print(get_name('Steve', 'Jobs'))
