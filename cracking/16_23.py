# 16.23 Rand7 from Rand5: Implement a method rand7() given rand5(). That is, given
# a method that generates a random number between 0 and 4 (inclusive), write a
# method that generates a random number between 0 and 6 (inclusive).

from random import randrange
from functools import partial


rand5 = partial(randrange, 5)


def rand2():
    while True:
        x = rand5()
        if x < 4:
            return x % 2


def rand7():
    while True:
        x = 5 * rand5() + rand5()
        if x < 21:
            return x % 7


def rand7_alt():
    while True:
        x = 2 * rand5() + rand2()
        if x < 7:
            return x


if __name__ == "__main__":
    vals = [0] * 7
    for _ in range(10 ** 6):
        vals[rand7()] += 1
    print([x / 1e4 for x in vals])
