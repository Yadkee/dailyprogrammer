#! python3
# https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/


def solve(males, females, needed):
    male, female = [0, 0, males], [0, 0, females]
    while sum(male[:96]) + sum(female[:96]) < needed:
        fertile = sum(female[4:96])
        male.insert(0, fertile * 5)
        female.insert(0, fertile * 9)
    return len(male) - 3, sum(male[96:]) + sum(female[96:])

print(solve(2, 4, 1000000000))
print(solve(2, 4, 15000000000))
