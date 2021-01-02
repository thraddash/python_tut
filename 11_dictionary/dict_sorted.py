#!/usr/bin/env python
print("#Sorted keys while iterate")
shop_items = {'rice':44, 'flour':22, 'oil':33}
print(shop_items)

for key in sorted(shop_items):
    print(key, shop_items[key])

print("#Sorted values while iterate")
for key in sorted(shop_items, key=shop_items.get):
    print(key, shop_items[key]);

for values in sorted(shop_items.values()):
    print(values)
