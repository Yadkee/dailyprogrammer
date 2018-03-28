#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/

pump = (1, 0, 3, 4, 3)
pie = (0, 1, 4, 3, 2)
recipes = {pump: "pumpkin", pie: "apple"}


def can_bake(ing, recipe):
    for i, j in zip(ing, recipe):
        if i < j:
            return False
    return True


def bake(ing, recipe):
    return tuple(i - j for i, j in zip(ing, recipe))


def solve(ing, hist=[]):
    possible = []
    for r in recipes:
        if can_bake(ing, r):
            testIng = bake(ing, r)
            s = solve(testIng, hist + [r])
            if s:
                possible.append(s)
    if possible:
        return max(possible, key=lambda x: (len(x[1]), sum(x[0])))
    return (ing, hist)


def pretty_output(hist):
    for i in set(hist):
        print("%d %s pies" % (hist.count(i), recipes[i]))
    print()

pretty_output(solve((10, 14, 10, 42, 24))[1])
pretty_output(solve((12, 4, 40, 30, 40))[1])
pretty_output(solve((12, 14, 20, 42, 24))[1])
