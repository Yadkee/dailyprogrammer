#! python3
# -*- coding: utf-8 -*-
# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/
from functools import reduce
from operator import mul
from itertools import count


def prod(it):
    return reduce(mul, it, 1)


def sixn():
    yield 2
    yield 3
    for n in count(1):
        yield 6 * n - 1
        yield 6 * n + 1


def factors(n):
    f = []
    if n < 4:
        return f
    for i in sixn():
        while n % i == 0:
            f.append(i)
            n //= i
        if n == 1:
            break
    return f


# f = factors(1234567891011)
f = [int(i) for i in "3*3*3*53*79*1667*20441*19646663*89705489".split("*")]
# Extended way:
possibilities = [prod(f)]
for i in range(len(f)):
    for j in range(i + 1, len(f) + 1):
        possibilities.append(prod(f[:i] + f[j:]) + prod(f[i:j]))
print(min(possibilities))
# Another (compressed) way to code it:
print(min([prod(f[:i] + f[j:]) + prod(f[i:j]) for i in range(len(f)) for j in range(i + 1, len(f) + 1)]))
