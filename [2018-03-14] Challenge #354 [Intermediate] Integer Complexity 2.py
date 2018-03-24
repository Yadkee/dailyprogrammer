#! python3
# -*- coding: utf-8 -*-
from math import sqrt
pc = {0: 0, 1: 1, 2: 2, 3: 3}  # Precalculated values


def complexity(n):
    try:
        return pc[n]
    except KeyError:
        c = min(p(n), 1 + pc[n - 1])
        pc[n] = c
        return c


def p(n):
    return min([(complexity(i) + complexity(n // i)) for i in range(2, int(sqrt(n)) + 1) if n % i == 0] or [n])

print(sum(complexity(i) for i in range(1, 1001)))
