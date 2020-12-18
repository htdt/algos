# 17.9 Kth Multiple: Design an algorithm to find the kth number such that the
# only prime factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be
# factors, but it should not have any other prime factors. For example, the first
# several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

from collections import deque


def get_num_357_queues(k):
    # q3 contains only factor 3: 3, 3*3 ...
    # q5 has factors 3 and 5: 5, 5*3, 5*5, 5*3*3 ...
    # q7 has factors 3, 5 and 7: 7, 7*3, 7*5, 7*7, 7*3*3 ...
    q3, q5, q7 = deque([1]), deque(), deque()
    for i in range(k):
        v3 = q3[0] if len(q3) else float("inf")
        v5 = q5[0] if len(q5) else float("inf")
        v7 = q7[0] if len(q7) else float("inf")
        v = min(v3, min(v5, v7))
        if v == v3:
            # if our smallest number has factor 3,
            # we must append multiplications to each queue
            q3.popleft()
            q3.append(3 * v)
            q5.append(5 * v)
        elif v == v5:
            # but if the number has factor 5, we do not append it to q3
            # to avoid duplicates
            q5.popleft()
            q5.append(5 * v)
        else:
            # similar logic here: factor 7 goes only into q7
            q7.popleft()
        q7.append(7 * v)
        print(v)
    return v


if __name__ == "__main__":
    get_num_357_queues(16)
