#!/usr/bin/env python

# Arbitary number of arguements
print("*args (non-keyworded arg) and **kwargs (keyword arg)\n")

def students(*students_name):
    print(students_name, type(students_name))
    for student in students_name:
        print(student)

students('Bill', 'Ross', 'Jack', 'Chris', 'Bob')
students()
students('Jack')
