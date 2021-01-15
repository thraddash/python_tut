#!/usr/bin/env python

# Ignore exception by pass
def div(x, y):
    return x / y

try: 
    div_result = div(2, 1)
    #div_result = div(2, 0)
except:
    pass # do nothing
else: 
    print("Div result is: " + str(div_result))

def div2(x, y):
    try: 
        result = x / y
    except:
        pass # do nothing
    else: 
        return "Div result is: " + str(result)
print()
print("v2 passing arguments")
print(div2(2, 1))
print(div2(2, 0))
