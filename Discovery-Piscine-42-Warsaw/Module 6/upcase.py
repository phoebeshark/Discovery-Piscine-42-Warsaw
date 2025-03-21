#!/usr/bin/env python3
import sys
count = len(sys.argv) - 1
text = input(" ")      
if count != 1:
    print("none")
else:
     text = sys.argv[1]
     print(text.upper())