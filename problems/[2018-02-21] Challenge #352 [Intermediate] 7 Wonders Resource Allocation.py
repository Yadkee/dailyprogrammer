#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/7z8hrm/20180221_challenge_352_intermediate_7_wonders/
"""Inspired by u/Loonter's sorting idea"""
from time import time


def ssolve(scards, starget):
    def yield_tuple_remove(it, o):
        for i in it:
            if i == o:
                break
            yield i
        for i in it:
            yield i

    def tuple_remove(t, o):
        """Like a list.remove() but returns a new instance"""
        return tuple(yield_tuple_remove(iter(t), o))

    def relevant_cards(cards, targetSet):
        """Remove cards that are not in target"""
        targetSet = set(target)
        return tuple(i & targetSet for i in cards)

    def can_win(cards, target):
        """Only can win if there are enough cards for target's needs"""
        for i in set(target):
            tCount = target.count(i)
            cCount = sum(1 for j in cards if i in j)
            if tCount > cCount:
                return False
        return True

    def solve(cards, target):
        if len(target) == 1:  # One card for one target
            return target[0] in cards[0]  # They match
        cards = relevant_cards(cards, target)
        # We first go for cards with only one resource
        for chosen in cards:
            if len(chosen) != 1:
                continue
            cards = tuple_remove(cards, chosen)
            target = tuple_remove(target, chosen.pop())
            return solve(cards, target)
        if not can_win(cards, target):
            return False
        # Remember that target is sorted by resource frequency in cards
        chosen = target[0]
        target = target[1:]
        # We try the cards that contain this resource
        for i in cards:
            if chosen not in i:
                continue
            sCards = tuple_remove(cards, i)
            s = solve(sCards, target)
            if s:
                return True
        # Nothing worked so there is no solution
        return False
    cards = tuple(set(i.split("/")) for i in scards.split(", "))

    def letter_frecuency(l):
        return sum(1 for j in cards if l in j)
    target = tuple(sorted(starget, key=letter_frecuency))
    t0 = time()
    solution = solve(cards, target)
    # Remember that True == 1 and False == 0
    print("It can%sbe solved. Took %.4f seconds" %
          ((" not ", " ")[solution], time() - t0))

ssolve("W/B/S/O, W, S/B, S", "WWSS")
ssolve("W/B/S/O, S/O, W/S, W/B, W/B, W, B", "WWBSSOO")
ssolve("A/B/D/E, A/B/E/F/G, A/D, A/D/E, A/D/E, B/C/D/G, B/C/E, B/C/E/F, "
       "B/C/E/F, B/D/E, B/D/E, B/E/F, C/D/F, C/E, C/E/F/G, C/F, C/F, "
       "D/E/F/G, D/F, E/G", "AABCCCCCCDDDEEEEFFGG")
ssolve("A/C/G/K/L/O/R/S, A/D/H/I/M/Q, A/D/K/W/X, A/D/M/U/Z, A/E/J/M/T, "
       "A/G/H/I/M/R/T/Z, A/G/M/T/U, A/H/I/J/Q, B/C/Q/U/V, B/D/F/K/M/R/W/Y, "
       "B/F/P/T/U/W/Y, B/G/K/M/S/T/X/Y, C/E/F/I/K/N/O, D/E/G/J/M/Q/Z, "
       "D/G/I/R/Z, D/H/I/T/U, E/G/H/J/M/Q, E/G/H/J/Q/R/T/U, E/G/J/M/Z, "
       "E/H/I/Q/T/U/Z, E/J/O/S/V/X, F/G/H/N/P/V, F/G/N/P/R/S/Z, "
       "F/I/M/Q/R/U/Z, F/L/M/P/S/V/W/Y, G/H/J/M/Q",
       "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
