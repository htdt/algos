# 8.10 Paint Fill: Implement the "paint fill" function that one might see on many image
# editing programs. That is, given a screen (represented by a 2d array of colors),
# a point, and a new color, fill in the surrounding area until the color changes from
# the original color.

import random


def fill(arr, x, y, cur_color, new_color):
    if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0]):
        return

    if arr[x][y] == cur_color:
        arr[x][y] = new_color
        fill(arr, x - 1, y, cur_color, new_color)
        fill(arr, x + 1, y, cur_color, new_color)
        fill(arr, x, y - 1, cur_color, new_color)
        fill(arr, x, y + 1, cur_color, new_color)


def show(arr):
    chars = {0: " ", 1: "*", 2: "#"}
    for line in arr:
        print("".join(map(lambda x: chars[x], line)))


if __name__ == "__main__":
    arr = [[0] * 16 for _ in range(16)]

    for _ in range(150):
        x, y = random.randint(0, 15), random.randint(0, 15)
        arr[x][y] = 1
    arr[7][7] = 0

    show(arr)
    fill(arr, 7, 7, 0, 2)

    print()
    show(arr)
