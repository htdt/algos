from typing import List, Tuple
from sort.eval import eval_sort


def partition(arr: List[int], lo: int, hi: int) -> Tuple[int]:
    counter = 0
    i, j = lo + 1, hi
    while True:
        while arr[i] < arr[lo] and i < hi:
            i += 1
            counter += 1

        while arr[j] >= arr[lo] and j > lo:
            j -= 1
            counter += 1

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j, counter


def sort(arr: List[int], lo: int, hi: int) -> int:
    if hi <= lo:
        return 0
    j, counter = partition(arr, lo, hi)
    counter += sort(arr, lo, j - 1)
    counter += sort(arr, j + 1, hi)
    return counter


if __name__ == "__main__":
    eval_sort(sort)
