#!/usr/bin/env python3

##
#  ex6-quicksand/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

l = lines[0].split(' ')
H, L = int(l[0]), int(l[1])
del lines[0]

M = list()
for _ in range(H):
    M.append([0]*L)

E = list()
for i, line in enumerate(lines):
    for j, case in enumerate(line):
        if case == '.':
            M[i][j] = 0
            E.append([i, j])

def dist(case):
    global i, j
    return abs(i - case[0]) + abs(j - case[1])

for i, line in enumerate(lines):
    for j, case in enumerate(line):
        if case == '#':
            M[i][j] = min(list(map(dist, E)))

deepest = 0
for line in M:
    deepest = max(deepest, max(line))

print(deepest)
