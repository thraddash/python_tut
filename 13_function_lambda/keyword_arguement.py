#!/usr/bin/env python
# Keyword arguement

def person_details(name, age, city='San Francisco'):
    print(name, age, city, sep='|')

print("#Can define a default value city = sf")
print("name, age, city='San Francisco'")
print("#Keyword arg name=Bill, age=22, city='Redwood City'")
person_details(name='Bill', age=22, city='Redwood City')
print()
print("#Default value Keyword, age=5, name=Ross")
person_details(age=5, name='Ross')
print()
print("#Default value positional argument name=James, age=30")
person_details('James', 30) 
print()

def key(a,b,c):
    first = f"a is {a}"
    second = f"b is {b}"
    third = f"c is {c}"
    return first, second, third

print("#cannot start off keyword arguement then change to positional arguement")
print("print(key(a=5, b=2, 6))")
print("SyntaxError: positional argument follows keyword argument\n")
print("#duoable start off positional arguement then keyword arguement")
print("print(key(5, b=2, c=6))")
print(key(5, b=2, c=6))

print("#arguement order doesn't matter, when using keyword arguement")
print("print(key(c=6, b=2, a=5))")
print()

print("#non-default arguement follows default argument")
print("name='', age, country='USA' will not work")
print("name='', age=0, country='USA' will not work")
'''
def person(name='', age, country='USA'):
   print(name, age, country, sep='|')
'''
def person(name='', age=0, country='USA'):
   print(name, age, country, sep='|')

