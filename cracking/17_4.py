# 17.4 Missing Number: An array A contains all the integers from 0 to n, except
# for one number which is missing. In this problem, we cannot access an entire
# integer in A with a single operation. The elements of A are represented in
# binary, and the only operation we can use to access them is "fetch the jth
# bit of A[i]", which takes constant time. Write code to find the missing
# integer. Can you do it in O(n) time?

from random import randrange


def find_missing(arr, bit_pos=0):
    # we use two bytes for demo
    if bit_pos >= 16:
        return 0
    # mask to retrive only one bit on the specific position
    mask = 1 << bit_pos
    one_bit, zero_bit = [], []
    # group all numbers from the array depending on the bit value
    for x in arr:
        if x & mask == 0:
            zero_bit.append(x)
        else:
            one_bit.append(x)

    # if all numbers would present, then len(0) >= len(1), but one number is missing, so
    # if len(0) == len(1), initially len(0) == len(1) + 1 and the number is in group 0,
    # if len(0) < len(1), initially len(0) == len(1) and number is in 0,
    # if len(0) > len(1), number is in 1
    if len(zero_bit) <= len(one_bit):
        # current bit is 0, get the next bit
        v = find_missing(zero_bit, bit_pos + 1)
        return v << 1
    else:
        v = find_missing(one_bit, bit_pos + 1)
        # current bit is 1, set it
        return (v << 1) | 1


if __name__ == "__main__":
    for _ in range(100):
        arr_len = randrange(2, 1 << 16)
        rm_element = randrange(arr_len)
        arr = list(range(arr_len))
        del arr[rm_element]
        found = find_missing(arr)
        assert found == rm_element
    print("yay")
