#!/usr/bin/env python
a="""
#########################################
# CSV file write
list_items = [["name", 'age', 'country'],
              ['Bill Gates', 55, 'US'],
              ['Mark', 34, 'US'],
              ['Taylor', 29, 'Europe']
             ]
import csv

with open('people.csv', 'w') as fobj:
    fcsv = csv.writer(fobj)
    fcsv.writerows(list_items)
"""
print(a)

import csv

list_items = [["name", 'age', 'country'],
              ['Bill Gates', 55, 'US'],
              ['Mark', 34, 'US'],
              ['Taylor', 29, 'Europe']
             ]

with open('people.csv', 'w') as fobj:
    fcsv = csv.writer(fobj)
    fcsv.writerows(list_items)
