# Print all binary numbers of length K without 11 (two consecutive ones) inside
# E.g. K = 3: 000 001 010 100 101


def bruteforce(k):
    total = 2 ** k  # numbers of length k
    for i in range(total):
        i_str = bin(i)[2:]  # to binary as string without "0b"
        # validate - simply check all elements one after another
        valid = True
        for k in range(len(i_str) - 1):
            if i_str[k] == "1" and i_str[k + 1] == "1":
                valid = False
                break
        if valid:
            print(i_str)
    # time complexity O(k * 2 ^ k)


def bruteforce_bin(k):
    total = 2 ** k
    for i in range(total):
        # if we shift the number left or right and apply AND with original,
        # only consecutive ones will produce non-zero result
        if i & (i >> 1) == 0:
            print(bin(i)[2:])
    # time complexity O(2 ^ k)


def recursive(k, prefix=""):
    if len(prefix) >= k:
        print(prefix[:k])
        return
    recursive(k, prefix + "0")
    recursive(k, prefix + "10")
    # time complexity O(2 ^ k)


if __name__ == "__main__":
    bruteforce(4)
    print("----")
    bruteforce_bin(4)
    print("----")
    recursive(4)
