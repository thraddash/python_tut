#!/usr/bin/env python

#---------------
# Exception Msg
#--------------
def div(x, y):
    try:
        result = x / y
    except Exception as e:  #Exception class python Error 
        print("Error happened: ", e)
        return None
    return result

print("string 4 / string 2")
print(div('4', '2'))
print("4/0")
print(div(4, 0))
