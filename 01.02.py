#! /usr/bin/python3

import sys

parse = {}
parse['('] = lambda: 1
parse[')'] = lambda: -1

floor = 0

# Test 1
#contents = ")"
# Test 2
#contents = "()())"

f = open("input.txt", "r")
if f.mode == "r":
    contents = f.read()

count = 0
for c in contents:
    count += 1
    if c in parse:
        floor += parse[c]()
        if (floor < 0):
            print("Entered basement at character position: %d" % count)
            sys.exit()
    else:
        print("Unrecognized character")

