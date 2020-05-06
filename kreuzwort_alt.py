#!/usr/bin/env python

import os
import sys

def print_expanded(data):
    s1 = "+-"
    bars = '|'
    head_line = s1 * (len(data[0]) + 1) + '+'
    print(head_line)
    for d in data:
        line = bars.join(d)
        print(bars + line + bars)
        print(head_line)

### main
with open("kreuzworträtsel_1.txt", "r") as f:
    data = list(f)

x = data.pop(0).strip()
y = data.pop(0).strip()

size_x = int(x)
size_y = int(y)

while len(data) > size_y:
    data.pop(0)

data = [d.rstrip('\r\n') for d in data]
print_expanded(data)
