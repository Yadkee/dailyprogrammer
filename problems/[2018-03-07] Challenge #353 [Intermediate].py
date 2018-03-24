#! python3
# -*- coding: utf-8 -*-


def solve(pk):
    def flip(l, s, f):
        return l[:s] + list(reversed(l[s:f])) + l[f:]

    def rindex(l, v):
        return len(l) - l[-1::-1].index(v) - 1

    ln = len(pk)
    shift = nFlips = 0
    while True:
        # We can forget about the right-already ordered stack
        until = ln - shift
        if until == 0:
            break
        mx = max(pk[:until])
        imx = rindex(pk[:until], mx)
        # If max value is already at its position:
        if imx == until - 1:
            shift += 1
            continue
        print(pk)
        imx = pk[:until].index(mx)
        pk = flip(pk, imx, until)
        nFlips += 1
    print(pk)
    print("Took %d flips" % nFlips)

solve([3, 1, 2])
solve([7, 6, 4, 2, 6, 7, 8, 7])
solve([11, 5, 12, 3, 10, 3, 2, 5])
solve([3, 12, 8, 12, 4, 7, 10, 3, 8, 10])
