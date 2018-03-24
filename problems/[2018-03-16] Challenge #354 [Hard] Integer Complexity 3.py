#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/84uk5v/20180316_challenge_354_hard_integer_complexity_3/

"""
(This solution got me a gold medal flair at dailyprogrammer.)
This is an edited version of the code.
With the actual parameters you will get 115, 128, 143, 157, 172, 188,
 207, 218, 234 and 248 which are not the winning solutions.
To get them you will have to play with values
 like the cap parameter or the maximums.
Also note that I used an api to totally factorize numbers
 over 10 ^ 14 and to get complexities below 10 ^ 12 and over 10 ^ 6
 but I did not include the APIs in this code.
"""


from itertools import count
from time import time
import sys
sys.setrecursionlimit(1 << 31 - 1)


def cached(*arg):
    def ww(f):
        def w(*arg, **kw):
            try:
                i = kw["insert"]
            except KeyError:
                k = (arg, tuple(kw.items()))
                try:
                    return cache[k]
                except KeyError:
                    c = f(*arg, **kw)
                    cache[k] = c
                    return c
            else:
                cache[k] = i
        cache = arg[0]
        return w
    return ww


def sixn(m):
    """Yields values in the form of 6n - 1 and 6n + 1 until m"""
    if m <= 2:
        return ()
    if m > 2:
        yield 2
    if m > 3:
        yield 3
    for n in count(1):
        x = 6 * n - 1
        y = x + 2
        if x < m:
            yield x
        else:
            break
        if y < m:
            yield y
        else:
            break


def primes(m):
    """Yields primes until m"""
    if m <= 2:
        return ()
    sieve = [True] * m
    for i in sixn(m):
        if sieve[i]:
            yield i
            for mult in range(i * i, m, i):
                sieve[mult] = False


@cached({})
def factors_s(n, ret=False):
    """Returns all the factors of a number
    (up to the last prime in primeList)"""
    f = set()
    if n < 4:
        return f
    limit = int(n / 2 + 1)
    for i in primeList:
        if i > limit:
            break
        while n != 1:
            if n % i:
                break
            else:
                n //= i
                f.add(i)
        else:
            break
    if ret:
        return (n, f)
    return f


@cached({})
def factors(n):
    n, f = factors_s(n, ret=True)
    if n < maxFacSelfScuared and f:
        f.add(n)
    return f


def complexities(x):
    """Adaptation of zatoichi49s answer to Integer complexity #2"""
    d = {0: 0, 1: 1, 2: 2, 3: 3, 5: 5}
    e = {0: "", 1: "1", 2: "2", 3: "3", 5: "5"}
    for n in range(2, x + 1):
        if n not in d or d[n-1] + 1 < d[n]:
            d[n] = d[n-1] + 1
            e[n] = "(%s+1)" % e[n-1]
        for i in range(2, n + 1):
            if i * n > x:
                break
            else:
                if n * i not in d or d[n] + d[i] < d[n*i]:
                    d[n*i] = d[n] + d[i]
                    e[n*i] = "%s*%s" % (e[n], e[i])
    return tuple((d[i], e[i]) for i in sorted(d))


def doIt(n, cap=1):
    noMore = set()
    isPrime = set()

    @cached({})
    def complexity(n):
        if n < maxCompSelf:
            return complexityList[n]
        elif n in isPrime:
            v, e = complexity(n - 1)
            return (v + 1, "(%s+1)" % e)
        else:
            f = factors(n)
            if f:
                isPrime.update(f)
                if n < cap and n not in noMore:
                    noMore.add(n - 1)
                    v, e = complexity(n - 1)
                    mv, me = (v + 1, "(%s+1)" % e)
                else:
                    mv = n
                for i in f:
                    j = n // i
                    vi, ei = complexity(i)
                    vj, ej = complexity(j)
                    if vi + vj < mv:
                        mv = vi + vj
                        me = "%s*%s" % (ei, ej)
                return mv, me
            else:
                v, e = complexity(n - 1)
                return (v + 1, "(%s+1)" % e)
    return complexity(n)


a1 = 12345678910111213  # 113
a2 = 1234567891011121314  # 127
a3 = 123456789101112131415  # 142
a4 = 12345678910111213141516  # 155
a5 = 1234567891011121314151617  # 170
a6 = 123456789101112131415161718  # 185
a7 = 12345678910111213141516171819  # 205
a8 = 1234567891011121314151617181920  # 211
a9 = 123456789101112131415161718192021  # 230
a10 = 12345678910111213141516171819202122  # 245

pattern = " ->||%d||=%d in %d seconds\n%s\n\n"

maxCompSelf = 10 ** 6
maxFacSelf = 10 ** 7
maxFacSelfScuared = maxFacSelf ** 2
primeList = tuple(primes(maxFacSelf))
print("Got first primes")
complexityList = complexities(maxCompSelf)
print("Precalculated small complexities")

for a in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    t = time()
    v, e = doIt(a, 1)
    msg = pattern % (a, v, int(time() - t), e)
    print(msg, end="")
    with open("result.txt", "a") as f:
        f.write(msg)
