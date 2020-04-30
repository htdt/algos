from typing import List
from sort.eval import eval_sort


def sort(arr: List[int], lo: int, hi: int) -> int:
    def swim(k: int):
        """
        finds right position for element in heap
        to append to heap, add to the end and swim it
        """
        while k > 0 and arr[k // 2] < arr[k]:
            arr[k // 2], arr[k] = arr[k], arr[k // 2]
            k //= 2

    def sink(k: int, N: int):
        """
        fixes the case when parent smaller than child
        to remove max element, exchange arr[1] and arr[N],
        remove arr[1], sink arr[N]
        """
        counter = 0
        while 2 * k <= N:
            counter += 2
            j = 2 * k  # get child
            if j < N and arr[j] < arr[j+1]:
                j += 1  # choose bigger from pair
            if arr[k] >= arr[j]:
                break  # parent bigger - done
            arr[k], arr[j] = arr[j], arr[k]
            k = j
        return counter

    arr.insert(0, None)  # index starts from 1
    # binary tree
    # root -> arr[1]
    # children of arr[x] -> arr[2 * x] and arr[2 * x + 1]
    counter = 0
    N = hi + 1  # num elements starting from 1
    for k in reversed(range(1, N // 2 + 1)):  # build heap bottom-up
        # start from N // 2, last - 1 layer
        # sink this element = compare with two children
        # for upper layers more compares
        counter += sink(k, N)
    while N > 1:
        arr[1], arr[N] = arr[N], arr[1]  # swap largest with end
        N -= 1  # don't touch largest
        counter += sink(1, N)  # sink element from end
    del arr[0]
    return counter


if __name__ == "__main__":
    eval_sort(sort)
