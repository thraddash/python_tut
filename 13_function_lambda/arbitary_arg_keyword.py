#!/usr/bin/env python

# Arbitary keyword arguments

def students(captain, **other_students):
    print('Captain ', captain)
    print('Others ', other_students)

students(captain='Hook', second_captain='Peter', thrid_captain='Pan')

## Arbitary keywarod arguments are optional
students(captain='Denzel')
