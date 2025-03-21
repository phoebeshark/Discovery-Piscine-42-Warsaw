#!/usr/bin/env python3
arr = {2, 8, 9, 48, 8, 22, -12, 2}
new_arr = set ()
for i in arr:
    if i>5 and (i+2) not in new_arr:
        new_arr.add(i+2)
print(new_arr)