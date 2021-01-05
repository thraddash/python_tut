#!/usr/bin/env python

# Positional and Arbitary arguments mixing

def students(captain, *other_students):
    print('Captain ', captain)
    print('Others ', other_students)

students('Rick', 'Kobe', 'Joe', 'Washington', 'Jerry')
