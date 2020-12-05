# 17.3 Random Set: Write a method to randomly generate a set of m integers from
# an array of size n. Each element must have equal probability of being chosen.

from random import randrange


def sample(arr, m):
    # if len(arr) == m, the task is trivial:
    subset = arr[:m]
    # now we assume that we have the correct subset for length n-1
    # the next n-th element must be added with p = m / n
    for i in range(m, len(arr)):
        k = randrange(i + 1)
        if k < m:
            subset[k] = arr[i]
    return subset


if __name__ == "__main__":
    # let's sample 5 numbers out of 0..15 many times and validate
    # that each number is chosen roughly the same number of times
    a = [0] * 16
    for _ in range(10 ** 5):
        s = sample(list(range(len(a))), 5)
        for v in s:
            a[v] += 1
    print(a)
