#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
"""It is not a short solution but an optimized one"""
from itertools import count


def sixn(m):
    """All primes are of the form 6n + 1 or 6n - 1"""
    yield 2
    yield 3
    for i in count(1):
        x = 6 * i + 1
        if x - 2 >= m:
            break
        yield x - 2
        if x >= m:
            break
        yield x


def primes_until(m):
    """(https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)"""
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False


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
