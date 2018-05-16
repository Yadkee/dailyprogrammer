#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
"""It is not a short solution but an optimized one"""
from math import sqrt


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
    yield from range(2, min(m, 4))
    for i in range(6, m - 1, 6):
        yield from (i - 1, i + 1)
    if m > 8 and i + 5 < m:
        yield i + 5


def primes_until(m):
    """(https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)"""
    sieve = [True] * m
    for i in sixn(int(sqrt(m)) + 1):
        if sieve[i]:
            for mult in range(i * i, m, i):
                sieve[mult] = False
    yield from (i for i in sixn(m) if sieve[i])


def solve(inp):
    def weak_goldbach(n):
        for p1 in primes:
            if p1 >= n:
                break
            n1 = n - p1
            for p2 in primes:
                if p2 >= n1:
                    break
                if n1 - p2 in primesSet:
                    return "%d + %d + %d" % (p1, p2, n1 - p2)
    numbers = [int(i) for i in inp.splitlines()]
    primes = list(primes_until(max(numbers)))
    primesSet = set(primes)
    return "\n".join(weak_goldbach(n) for n in numbers)


print(solve("""11
35
111
17
199
287
53"""))
