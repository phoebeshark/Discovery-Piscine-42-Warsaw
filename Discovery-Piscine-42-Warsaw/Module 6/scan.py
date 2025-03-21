#!/usr/bin/env python3
import sys
import re
arg_1=sys.argv[1]
arg_2=sys.argv[2]
count=len(re.findall(r'(?={})'.format(re.escape(arg_1)),arg_2))
print(count)