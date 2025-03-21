#!/usr/bin/env python3
import array
arr = array.array("i",[2, 8, 9, 48, 8, 22, -12, 2])
new_arr = array.array("i", [])
for i in arr:
    if i>5:
        new_arr.append(i+2)
print(new_arr)