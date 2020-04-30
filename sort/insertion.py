from typing import List
from sort.eval import eval_sort


def sort(arr: List[int], lo: int, hi: int) -> int:
    counter = 0
    for i in range(lo, hi + 1):
        for j in reversed(range(1, i + 1)):
            counter += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return counter


if __name__ == "__main__":
    eval_sort(sort)
