from typing import List
from sort.eval import eval_sort


def merge(arr: List[int], lo: int, mid: int, hi: int) -> int:
    aux = arr[:]
    i, j = lo, mid + 1
    counter = 0
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            counter += 1
            j += 1
        else:
            arr[k] = aux[i]
            counter += 1
            i += 1
    return counter


def sort(arr: List[int], lo: int, hi: int) -> int:
    if hi <= lo:
        return 0
    mid = lo + (hi - lo) // 2
    counter = sort(arr, lo, mid)
    counter += sort(arr, mid + 1, hi)
    counter += merge(arr, lo, mid, hi)
    return counter


if __name__ == "__main__":
    eval_sort(sort)
