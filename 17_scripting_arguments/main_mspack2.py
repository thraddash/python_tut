#!/usr/bin/env python

#------------------
# Script arguments
#------------------

import sys
#print(sys.argv)
from mspack import msmath

def process_command(*args):
    command = args[0] # 1st argument = command
    x = int(args[1]) # convert args into int
    y = int(args[2])

    if command == 'sum':
        print ('Sum is ', msmath.sum(x, y))
    if command == 'sub':
        print('Subraction is: ', msmath.subtract(x, y))
    if command == 'mul':
        print('Multiplication is: ', msmath.multiplication(x, y))
    if command == 'div':
        print('Division is: ', msmath.division(x, y))

if len(sys.argv) >= 4: # 1st arg (name of script), 2nd arg(command), 3rd(int), 4th(int)
    # validate commands: sum, sub, mul, div
    command = sys.argv[1].lower()
    x = sys.argv[2]
    y = sys.argv[3]

    try:
        process_command(command, x, y)
    except Exception as e:
        print("Error in process_command: ", e)
else:
    print("Command and Parameter are not sufficient")


