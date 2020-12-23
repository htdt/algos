# 17.14 Smallest K: Design an algorithm to find the smallest K numbers in an array.

from random import randint, sample


def rank(arr, k, left=0, right=None):
    """
        Selection Rank Algorithm
        returns element of arr with rank k,
        arr is partitioned using this element as a pivot,
        i.e. all elements before the pivot are smaller.
        For simplicity we assume all elements are unique.
        Expected O(len(arr)) time.
    """
    if right is None:
        right = len(arr) - 1
    # pick a random element
    pivot = arr[randint(left, right)]
    # find the position of this element and arange the array
    left_end = partition(arr, left, right, pivot)
    left_size = left_end - left + 1
    if k == left_size - 1:
        # position matches needed rank - we found it
        return pivot
    elif k < left_size:
        # arr = smaller | goal | ... | left_end | larger
        # position of the pivot is larger, our target is in left part
        return rank(arr, k, left, left_end)
    else:
        # arr = smaller | left_end | ... | goal | larger
        # we cut the left part, we must reduce k accordingly
        return rank(arr, k - left_size, left_end + 1, right)


def partition(arr, left, right, pivot):
    """
        aranges arr[left: right + 1] this way:
        elements <= pivot | elements > pivot
        returns position where the pivot would be in a sorted sub-array,
        like sorted(arr[left: right + 1]).index(pivot) + left
    """
    while left <= right:
        if arr[left] > pivot:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        elif arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        else:
            left += 1
            right -= 1
    return left - 1


if __name__ == "__main__":
    for n_iter in range(100):
        size = randint(10, int(1e5))
        arr = sample(range(int(1e7)), k=size)
        arr_sorted = sorted(list(arr))
        k = randint(1, size - 2)
        el = rank(arr, k - 1)
        assert set(arr[:k]) == set(arr_sorted[:k])
        assert el == arr_sorted[k - 1]
        assert el == max(arr[:k])
    print("yay")
