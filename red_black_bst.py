from dataclasses import dataclass
import random
import math


@dataclass
class Node:
    key: int
    left: 'Node' = None
    right: 'Node' = None
    red: bool = True


def find(root: Node, key: int):
    x = root
    count = 0
    while x is not None:
        count += 1
        if key < x.key:
            x = x.left
        elif key > x.key:
            x = x.right
        else:
            return True, count
    return False, count


def rotateLeft(h: Node):
    assert h.right.red
    x = h.right
    h.right = x.left
    x.left = h
    x.red = h.red
    h.red = True
    return x


def rotateRight(h: Node):
    assert h.left.red
    x = h.left
    h.left = x.right
    x.right = h
    x.red = h.red
    h.red = True
    return x


def flipColors(h: Node):
    assert not h.red
    assert h.left.red
    assert h.right.red
    h.red = True
    h.left.red = h.right.red = False


def isRed(h: Node):
    return h is not None and h.red


def append(h: Node, key: int):
    if h is None:
        return Node(key=key)

    if key < h.key:
        h.left = append(h.left, key)
    elif key > h.key:
        h.right = append(h.right, key)
    else:
        pass

    if isRed(h.right) and not isRed(h.left):
        h = rotateLeft(h)
    if isRed(h.left) and isRed(h.left.left):
        h = rotateRight(h)
    if isRed(h.left) and isRed(h.right):
        flipColors(h)

    return h


if __name__ == '__main__':
    k = 1000
    root = Node(key=random.randint(0, k))
    for a in random.choices(range(k), k=k-1):
        append(root, a)
        root.red = False

    x, h = root, 0
    while x is not None:
        h += 1
        x = x.left
    print('height', h)

    outp = [find(root, random.randint(0, k))[1] for _ in range(10000)]
    print('avg', sum(outp) / len(outp))
    print('logN', round(math.log(k, 2)))
