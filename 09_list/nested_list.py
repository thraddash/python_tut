#!/usr/bin/env python
print("# end=' ' , by default python print ends with \\n, you can end a print stmt with any character or string using this parameter.")
matrix = [[1,2,3,4,5], [4,5,6,7,8], [1,1,1,1,1], [0,0,0,0,0]]

for x in matrix:
  for y in x:
    print(y, end=' ')
  print('test')
