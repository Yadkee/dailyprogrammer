#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/8jvbzg/20180516_challenge_361_intermediate_elsiefour/
from random import choice

ABC = "#_23456789abcdefghijklmnopqrstuvwxyz"
INDEX = dict((i, a) for a, i in enumerate(ABC))
NONCE_SIZE = 6


def cipher(key, text):
    out = []
    i = j = 0
    state = [INDEX[i] for i in key]
    encrypt = False
    for char in text:
        if char == "%":
            encrypt = not encrypt
            continue
        if encrypt:
            P = INDEX[char]
            r, c = divmod(state.index(P), 6)
            x = (r + state[i * 6 + j] // 6) % 6
            y = (c + state[i * 6 + j] % 6) % 6
            C = state[x * 6 + y]
            out.append(ABC[C])
        else:
            C = INDEX[char]
            x, y = divmod(state.index(C), 6)
            r = (x - state[i * 6 + j] // 6) % 6
            c = (y - state[i * 6 + j] % 6) % 6
            P = state[r * 6 + c]
            out.append(ABC[P])
        # Right rotate row r
        state.insert(r * 6, state.pop(r * 6 + 5))
        c = (c + 1) % 6
        if x == r:
            y = (y + 1) % 6
        if i == r:
            j = (j + 1) % 6
        # Down rotate col y
        values = state[y::6]
        state[y] = values.pop()
        state[y + 6::6] = values
        x = (x + 1) % 6
        if c == y:
            r = (r + 1) % 6
        if j == y:
            i = (i + 1) % 6
        # Update vector
        i = (i + C // 6) % 6
        j = (j + C % 6) % 6
    return "".join(out)


def signed(key, text, signature=None, header=""):
    if signature:
        nonce = "".join(choice(ABC) for _ in range(NONCE_SIZE))
        ciphered = cipher(key, "%" + nonce + header + text + signature)
        return nonce + ciphered[len(nonce) + len(header):]
    else:
        message = "%" + text[:NONCE_SIZE] + header + "%" + text[NONCE_SIZE:]
        return cipher(key, message)[NONCE_SIZE + len(header):]


key = "s2ferw_nx346ty5odiupq#lmz8ajhgcvk79b"
print(cipher(key, "tk5j23tq94_gw9c#lhzs"))
key = "#o2zqijbkcw8hudm94g5fnprxla7t6_yse3v"
print(cipher(key, "b66rfjmlpmfh9vtzu53nwf5e7ixjnp"))
key = "9mlpg_to2yxuzh4387dsajknf56bi#ecwrqv"
print(cipher(key, "grrhkajlmd3c6xkw65m3dnwl65n9op6k_o59qeq"))
key = "7dju4s_in6vkecxorlzftgq358mhy29pw#ba"
print(cipher(key, "%the_swallow_flies_at_midnight"))
key = "xv7ydq#opaj_39rzut8b45wcsgehmiknf26l"
c = signed(key, "im_about_to_put_the_hammer_down", "#rubberduck")
print(signed(key, c))
