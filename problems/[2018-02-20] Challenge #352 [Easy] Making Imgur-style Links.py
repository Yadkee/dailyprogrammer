#! python3
# -*- coding: utf-8 -*-
# https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/
abc = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base(n, b):
    out = []
    while n:
        n, d = divmod(n, b)
        out.append(abc[d])
    return "".join(reversed(out))

print(base(187621, 62))
print(base(237860461, 62))
print(base(2187521, 62))
print(base(18752, 62))
