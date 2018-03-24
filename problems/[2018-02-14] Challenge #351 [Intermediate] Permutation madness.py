#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/7xkhar/20180214_challenge_351_intermediate_permutation/
from os.path import join


def permute(s, i):
    """Permute string s according to instructions i"""
    p = tuple(range(len(s)))
    for j in i.split(","):
        if j.startswith("s"):
            n = int(j[1:])
            s = s[-n:] + s[:-n]
            p = p[-n:] + p[:-n]
        else:
            a, b = tuple(int(i) for i in j[1:].split("/"))
            if j.startswith("p"):
                a, b = p.index(a), p.index(b)
            if a < b:
                s = s[:a] + s[b:b + 1] + s[a + 1:b] + s[a:a + 1] + s[b + 1:]
                p = p[:a] + p[b:b + 1] + p[a + 1:b] + p[a:a + 1] + p[b + 1:]
            else:
                s = s[:b] + s[a:a + 1] + s[b + 1:a] + s[b:b + 1] + s[a + 1:]
                p = p[:b] + p[a:a + 1] + p[b + 1:a] + p[b:b + 1] + p[a + 1:]
        # print(s, j)
    return s



print(permute("abcde", "s1,x3/4,p4/1"))
print(permute("dbagcfe", "s4,s5,x5/3,x5/6,s5,s3,x0/3,x3/6,x6/0,x2/3,x3/5,s5,"
                         "s5,s5,s1,s5,s3,s3,x2/3,x1/0,s1,s1,s1,s4,x1/3,x4/2,"
                         "x5/1,x6/0,s2,x2/1"))
i1 = "[2018-02-14] Challenge #351 [Intermediate] Permutation madness Input #1"
i2 = "[2018-02-14] Challenge #351 [Intermediate] Permutation madness Input #2"
for i in (i1, i2):
    with open(join("..", "files", i + ".txt")) as f:
        s, i = f.read().split("\n", 1)
        i = "".join(i.split())
        print(permute(s, i))
