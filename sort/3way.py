from typing import List
from sort.eval import eval_sort


def sort(arr: List[int], lo: int, hi: int) -> int:
    if hi <= lo:
        return 0
    lt, gt = lo, hi
    v = arr[lo]
    i = lo + 1
    counter = 0
    while i <= gt:
        counter += 1
        if arr[i] < v:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > v:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    counter += sort(arr, lo, lt - 1)
    counter += sort(arr, gt + 1, hi)
    return counter


if __name__ == "__main__":
    eval_sort(sort)
