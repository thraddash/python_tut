#!/usr/bin/env python

#-----------
# Exception
#-----------

print("try catch block")
## try catch block
def div2(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Can not divide by zero")
        return None
    except:
        print("Error occured")
        return None
    return result

print("4/2")
print(div2(4, 2))
print()
print("2/0")
print(div2(2, 0))
print()
print("string 5 / string 4")
print(div2('5','4'))
