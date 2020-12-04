# 17.2 Shuffle: Write a method to shuffle a deck of cards. It must be a perfect
# shuffle - in other words, each of 52! permutations of the deck has to be
# equally likely. Assume that you are givan a random number generator which
# is perfect.

from random import randrange


def shuffle(arr):
    # if len(arr) == 2, we simply swap once with p = 1/2
    # if len(arr) == n, we assume arr[:n-1] is shuffled and we swap
    # n-th element with any with p = 1/n, in this case this element can be
    # equally likely at every position
    for i in range(1, len(arr)):
        k = randrange(i + 1)
        arr[i], arr[k] = arr[k], arr[i]
    return arr


if __name__ == "__main__":
    a = [0] * 5
    for _ in range(10 ** 5):
        s = shuffle(list(range(len(a))))
        for i, v in enumerate(s):
            a[i] += v
    print(a)
