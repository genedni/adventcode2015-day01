#! /usr/bin/python3

import sys

parse = {}
parse['('] = lambda: 1
parse[')'] = lambda: -1

floor = 0

f = open("input.txt", "r")
if f.mode == "r":
    contents = f.read()
for c in contents:
    if c in parse:
        floor += parse[c]()
    else:
        print("Unrecognized character")

print("floor: %d" % floor)
