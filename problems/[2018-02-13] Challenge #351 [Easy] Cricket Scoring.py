#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/


def solve(game):
    scores = [0, 0]
    s, r, n = 0, 1, 2  # Striker, replacement, next
    balls = extras = 0
    for e in game:
        # print(scores)
        if e.isdigit():
            ie = int(e)
            scores[s] += ie
            if ie & 1:
                s, r = r, s
            balls += 1
        elif e == ".":
            balls += 1
        elif e == "b":
            s, r = r, s
            balls += 1
            extras += 1
        elif e == "w":
            extras += 1
        elif e == "W":
            balls += 1
            if len(scores) == n:
                scores.append(0)
            s, n = n, n + 1
        if balls == 6:
            balls = 0
            s, r = r, s
    print(scores, extras)


solve("1.2wW6.2b34")
solve("WWWWWWWWWW")
solve("1..24.w6")
