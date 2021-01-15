#!/usr/bin/env python

#-----------
# Exception
#-----------

def div(x, y):
    return x / y

print(div(4, 2))
print()

print("try catch block")
## try catch block
def div2(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Can not divide by zero")
        return None
    return result

print("4/2")
print(div2(4, 2))
print("2/0")
print(div2(2, 0))
