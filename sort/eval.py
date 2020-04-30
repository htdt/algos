from typing import List
import random
import sys
import math


def is_sorted(arr: List[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def eval_sort(sort_fn):
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    r = int(sys.argv[2]) if len(sys.argv) == 3 else k
    random.seed(1337)
    x = random.choices(range(r), k=k)
    print('sorted', is_sorted(x))
    print('compares', sort_fn(x, 0, k - 1))
    print('NlogN', round(k * math.log(k, 2)))
    print('sorted', is_sorted(x))
