#! python3
# -*- coding: utf-8 -*-
# https://www.reddit.com/r/dailyprogrammer/comments/7xyi2w/20180216_challenge_351_hard_star_battle_solver/
from itertools import product
from string import ascii_uppercase as ABC
from time import time


def _insert_newlines(string, every=128):
    return "\n".join(string[i:i + every] for i in range(0, len(string), every))


def main(grid):
    t0 = time()
    S = grid.count("\n")
    LENGHT = S * S
    N = int(grid[0])
    TOTAL = N * S
    grid = "".join(grid[1:].split())
    possibles = tuple(set(i for i in range(LENGHT) if grid[i] is l)
                      for l in ABC[:S])
    regions = sorted(range(S), key=lambda x: grid.count(ABC[:S][x]))
    adjacent = []
    for a in range(LENGHT):
        cols = [0]
        rows = [0]
        if a % S > 0:
            cols.append(-1)
        if a % S < S - 1:
            cols.append(1)
        if a // S > 0:
            rows.append(-S)
        if a // S < S - 1:
            rows.append(S)
        adjacent.append(set(a + sum(i) for i in product(cols, rows)))
    cs = tuple(set(range(i, LENGHT, S)) for i in range(S))
    rs = (0,) * S + tuple(set(range(i * S, i * S + S)) for i in range(S))
    cr = tuple((i % S, i // S + S) for i in range(LENGHT))

    solution = []

    def solve(impossibles, colrows, count=0):
        if count == TOTAL:
            return True
        for a in possibles[regions[count // N]] - impossibles:
            c, r = cr[a]
            tryimpossibles = impossibles | adjacent[a]
            trycolrows = colrows[:]
            trycolrows[c] += 1
            trycolrows[r] += 1
            if trycolrows[c] == N:
                tryimpossibles.update(cs[c])
            if trycolrows[r] == N:
                tryimpossibles.update(rs[r])
            if solve(tryimpossibles, trycolrows, count + 1):
                solution.append(a)
                return True
        return None
    if solve(set(), bytearray(S + S)):
        s = "".join("*" if i in solution else "." for i in range(LENGHT))
        print(_insert_newlines(s, S))
    print("Took", time() - t0, "seconds")

main("""1
AABBCC
AABCCC
AABCCC
DDBBEE
DDBBEF
DDBBFF""")

main("""2
AAAABBCCCC
ADAABBBCBB
ADDBBBBBBB
DDDDBEEEEB
DDBBBBBBEB
FFFFGGHHHH
FIFFGGGHGG
FIIGGGGGGG
IIIIGJJJJG
IIGGGGGGJG""")

main("""3
AAAAABBBBBCCCCC
ADDDDBBBBBEEECC
ADDDDDDBEEEEEEC
ADDDFDDBEEGEEEC
ADDFFFHHHGGGEEC
AAAFFFHHHGGGCCC
AAHHFHHIHHGHCCC
AAAHHHIIIHHHJJJ
AAAKKKIIIKKKKLJ
AAAMKKKIKKKMLLJ
NNNMMKKKKKMMLLJ
NNNOMMMMMMMLLLJ
NOOOOMMMMMOOLLL
NOOOOOMMMOOOLLL
NNOOOOOOOOOOLLL""")
