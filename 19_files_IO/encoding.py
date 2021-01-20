#!/usr/bin/env python
a="""
#############################
# Encoding during file write
# 3rd parameter 'UTF-8'
####### Encoding ####################
with open('spanish.txt', 'w', encoding='UTF-8') as fobj:
with open('spanish.txt', 'w') as fobj:
¿Cuál?
¿Cuándo?
####### Without Encoding ############
# with open('spanish.txt', 'w') as fobj:
□Cu□l?
□Cu□ndo?
"""

with open('spanish.txt', 'w', encoding='UTF-8') as fobj:
    fobj.write('¿Cuál?')
    fobj.write('\n')
    fobj.write('¿Cuándo?')
    fobj.write('\n')
