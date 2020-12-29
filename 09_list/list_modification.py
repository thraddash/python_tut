#!/usr/bin/env python

# List modification
mix_list = ['honda', 29, 4.4, False]
print(mix_list)
mix_list[0] = 'toyota'
print(mix_list)

# Adding item in list
mix_list.append('audi')
print(mix_list)

mix_list += ['mercedez']  # shortcut version for adding item
print(mix_list)

mix_list.insert(2, 'proton') #inserting proton at index 2
print(mix_list)

# Deleting item in list
del mix_list[1]
print(mix_list)
