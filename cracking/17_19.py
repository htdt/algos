# 17.19 Missing Two: You are given an array with all the numbers from 1 to N
# appearing exactly once, except for one number that is missing. How can you
# find the missing number in O(N) time and O(1) space? What if there were two
# numbers missing?

from random import sample, randint


def find_2(arr):
    # no loops for simplicity, but if mem is important, can be optimized
    arr_sum = sum(arr)
    arr_sum_2 = sum([x ** 2 for x in arr])
    target_len = len(arr) + 2
    target_sum = target_len * (target_len - 1) // 2  # = sum(range(target_len))
    target_sum_2 = sum([x ** 2 for x in range(target_len)])
    s = target_sum - arr_sum
    t = target_sum_2 - arr_sum_2

    # if x and y are our missing numbers,
    # x + y = s, because s is a difference of the full sum and our array sum,
    # x^2 + y^2 = t for the same reason,
    # let's find x and y: y = s - x, x^2 + (s - x)^2 = t,
    # 2x^2 - 2sx + s^2 - t = 0, it's a quadratic equation with coefficients:

    a, b, c = 2, -2 * s, s ** 2 - t
    D = int((b ** 2 - 4 * a * c) ** 0.5)
    return (-b + D) // (2 * a), (-b - D) // (2 * a)


if __name__ == "__main__":
    # one number is obvious: sum(range(len(arr) + 2)) - sum(arr)
    # let's consider two

    for n_iter in range(100):
        size = randint(3, int(1e5))
        arr = sample(range(size), k=size)
        x0, x1 = sample(arr, k=2)
        arr.remove(x0), arr.remove(x1)
        y0, y1 = find_2(arr)
        assert {x0, x1} == {y0, y1}
    print("yay")
