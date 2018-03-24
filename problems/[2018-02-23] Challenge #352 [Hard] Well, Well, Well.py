#! python3
# -*- coding: utf-8 -*-
# https://www.reddit.com/r/dailyprogrammer/comments/7zriir/20180223_challenge_352_hard_well_well_well/
r"""Ugly bruteforce but works ¯\_(ツ)_/¯"""
from itertools import count
from fractions import Fraction


def neighbours(cell, w, h):
    if cell % w != 0:
        yield cell - 1
    if cell % w + 1 < w:
        yield cell + 1
    if cell - w > 0:
        yield cell - w
    if cell + w < h * w:
        yield cell + w


def animate(grid, w):
    for a, i in enumerate(grid):
        if a % w == 0 and a != 0:
            print()
        print("%.2f" % i, end=" ")
    print()


def solve(well, target):
    grid = list()
    for y, i in enumerate(well[1:].splitlines()):
        for x, j in enumerate(i.split(" ")):
            ij = int(j)
            grid.append(ij)
            if ij == 1:
                start = y * len(i.split(" ")) + x
            if ij == target:
                end = y * len(i.split(" ")) + x
    w = h = y + 1
    connected = set([start])
    for t in count(1):
        # print("------%d------" % t)
        # animate(grid, w)
        ln = len(connected)
        unit = Fraction(1)
        while unit > 0:
            mn = min(connected, key=lambda x: grid[x])
            q = Fraction(1, ln)
            grid[mn] += q
            unit -= q
            while True:
                for i in connected:
                    for j in neighbours(i, w, h):
                        if j in connected:
                            continue
                        elif grid[i] >= grid[j]:
                            connected.add(j)
                            break
                    else:
                        continue
                    break
                else:
                    break
                continue
        if grid[end] >= target + 1:
            break
    # print("------%d------" % t)
    # animate(grid, w)
    print("Took %d time units." % t)

solve("""
1 9 6
2 8 5
3 7 4""", 4)
solve("""
38 33 11 48 19 45 22
47 30 24 15 46 28 3
14 13 2 34 8 21 17
10 9 5 16 27 36 39
18 32 20 1 35 49 12
43 29 4 41 26 31 37
25 6 23 44 7 42 40""", 35)
solve("""
15 16 46 1 38 43 44
25 10 7 6 34 42 14
8 19 9 21 13 23 22
32 11 29 36 3 5 47
31 33 45 24 12 18 28
40 41 20 26 39 48 2
49 35 27 4 37 30 17""", 26)
