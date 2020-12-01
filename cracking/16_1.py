# 16.1 Number Swapper: Write a function to swap a number in place (that is,
# without temporary variables).

from random import randint


def swap(x, y):
    x ^= y
    y ^= x
    x ^= y
    return x, y


if __name__ == "__main__":
    for _ in range(1000):
        x, y = randint(-int(1e9), int(1e9)), randint(-int(1e9), int(1e9))
        xs, ys = swap(x, y)
        assert x == ys and y == xs
    print("yay!")
