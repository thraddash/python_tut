#!/usr/bin/env python

#Optional argument

def get_name(first_name, last_name, middle_name=''):
    complete_name = first_name
    if middle_name:
        complete_name += ' ' + middle_name

    complete_name += ' ' + last_name
    return complete_name

print(get_name('Johnny', 'Good'))
print(get_name('Johnny', 'B', 'Good'))
