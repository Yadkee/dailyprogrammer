#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/8ked11/20180518_challenge_361_hard_sudoku_knights_tour/
from modules.sudoku import fromstring, solve, tostring, islegit

_ = """
000009700090000086000087009009000870000870090080900000070008900008790000900000000
000009700090000086000087009009000860000870090086900007070058900008790050900006000
800069700097000086060087009009000860600870090085900007070058900008790050900006000
"""
BANNED = [fromstring(i) for i in _.split()]
# This boards are all unsolvable and produce so much lag


def knight_moves(pos):
    r, c = divmod(pos, 9)
    zip11 = zip((-18, 18), (r > 1, r < 7))
    zip21 = list(zip((-1, 1), (c, c < 8)))
    zip12 = zip((-9, 9), (r, r < 8))
    zip22 = list(zip((-2, 2), (c > 1, c < 7)))
    zips = ((zip11, zip21), (zip12, zip22))
    return set(pos + v + h for zip1, zip2 in zips
               for v, c1 in zip1 if c1
               for h, c2 in zip2 if c2)
KNIGHT_CACHE = [knight_moves(i) for i in range(81)]


def can_travel(iPos, moves):
    # https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorf's_rule
    moves.append(iPos)
    if len(moves) == 81:
        return True
    ts = set(moves)
    aimSet = KNIGHT_CACHE[iPos] - ts
    if aimSet:
        values = [(len(KNIGHT_CACHE[i] - ts), i) for i in aimSet]
        aim = min(values)[0]
        for v, i in values:
            if v == aim:
                if can_travel(i, moves.copy()):
                    return True
    return False


def recursive(iPos, moves, steps):
    moves.append(iPos)
    if steps == 0:
        yield moves
        return
    for i in KNIGHT_CACHE[iPos] - set(moves):
        yield from recursive(i, moves.copy(), steps - 1)
    return


out = []
score = "9999999"  # We know that this is the minimum possible
moves = [10, 29, 48, 67, 60, 43, 26]  # The shorter the more it takes
# Also if you delete too many values you will end up with a lot of different
#  symmetric solutions. And you do not want that. You can see the 8 symmetries
#  clicking here -> https://pastebin.com/EBgVwhDN
moves = [10, 29]

while len(score) != 81:
    print(score)
    for i in (i for i in "987654321" if score.count(i) != 9):
        print(" +%s" % i)
        score += i
        paths = []
        for path in recursive(moves[-1], moves[:-1], len(score) - len(moves)):
            board = bytearray(81)
            for a, i in enumerate(path):
                board[i] = int(score[a])
            if not islegit(board):
                continue
            if not can_travel(path[-1], path[:-1]):
                continue
            if board in BANNED:
                continue
            try:
                solved = solve(board)
            except KeyboardInterrupt:  # If it takes more than 3 secs press it.
                out.append(tostring(board))
                solved = False
            if not solved:
                continue
            paths.append(path)
        if not paths:
            score = score[:-1]
            continue
        moves = []
        for i in range(len(score)):
            # It breaks when they stop being equal
            if len(set(p[i] for p in paths)) != 1:
                break
            moves.append(paths[0][i])
        break
    else:
        raise Exception("Ehm... This should not have occured")

out.extend(["SCORE:", score, "SUDOKU:", tostring(solved), "PATH:", moves])
with open("result.txt", "w") as f:
    f.write("\n".join(map(str, out)))
