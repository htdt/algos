# 17.1 Add Without Plus: Write a function that adds two numbers. You should not
# use + or any arithmetic operators.

from random import randrange


def add(a, b):
    while b != 0:
        # XOR is a bit sum without carrying to higher bits
        s = a ^ b
        # if both bits are 1, we need to carry 1 to the next bit
        carry = (a & b) << 1
        # iterate until there's nothing to carry
        a, b = s, carry
    return a


if __name__ == "__main__":
    for _ in range(100):
        a, b = randrange(10 ** 9), randrange(10 ** 9)
        assert add(a, b) == a + b
    print("yay")
