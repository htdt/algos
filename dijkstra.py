from random import randrange


def show_grid(arr):
    """
    shows the grid, symbols:
    . cells allowed to visit,
    o cells considered while searching the path,
    # path we found,
    G our goal
    """
    chars = {0: " ", 1: ".", 2: "#", 3: "G", 4: "o"}
    for line in arr:
        print("".join(map(lambda x: chars[x], line)))


def get_neib(arr, x, y, W, H):
    """ helper function, returns valid neighbour cells for (x, y) """
    neib = []
    if x - 1 >= 0 and arr[y][x - 1] > 0:
        neib.append((y, x - 1))
    if x + 1 < W and arr[y][x + 1] > 0:
        neib.append((y, x + 1))
    if y - 1 >= 0 and arr[y - 1][x] > 0:
        neib.append((y - 1, x))
    if y + 1 < H and arr[y + 1][x] > 0:
        neib.append((y + 1, x))
    return neib


def dijkstra(arr, goal_x, goal_y):
    """
    Dijkstra's algorithm for finding shortest path on a grid;
    starting point (0, 0);
    input grid is modified in-place for visualisation
    """
    W, H = len(arr[0]), len(arr)
    # array with shortest distances from (0, 0) for each cell,
    # None indicates that the cell was not checked yet
    dist = [[None] * W for _ in range(H)]
    dist[0][0] = 0

    # set with points we need to check, we start from only (0, 0)
    to_visit = {(0, 0)}

    # set with goal neighbour cells
    goal_neib = set(get_neib(arr, goal_x, goal_y, W, H))

    # main loop
    while len(to_visit) and len(goal_neib):
        # select a cell from to_visit with smallest distance
        cur = min(to_visit, key=lambda v: dist[v[0]][v[1]])
        # we check the cell only once, remove from the set
        to_visit -= {cur}
        # also we track if we checked all goal neighbours for early stopping
        goal_neib -= {cur}
        y, x = cur
        # new possible distance for neighbours = distance of this cell + 1
        dist_new = dist[y][x] + 1

        # check all neighbours
        for ny, nx in get_neib(arr, x, y, W, H):
            # mark them "considered" for visualisation
            arr[ny][nx] = 4
            if dist[ny][nx] is None:
                # we see this cell first time,
                # we should check its neighbours as well
                to_visit.add((ny, nx))
                dist[ny][nx] = dist_new
            elif dist[ny][nx] > dist_new:
                # this cell was already checked, but we found a shorter path to it
                dist[ny][nx] = dist_new

    # loop finishes when we visited all allowed cells (empty to_visit)
    # or when we found the shortest path to the goal (empty goal_neib)

    # visualisation: show the goal and the path we found
    x, y = goal_x, goal_y
    arr[y][x] = 3
    while x != 0 or y != 0:
        n = get_neib(arr, x, y, W, H)
        y, x = min(n, key=lambda v: dist[v[0]][v[1]])
        arr[y][x] = 2

    return dist[goal_y][goal_x]


if __name__ == "__main__":
    W, H = 100, 32
    # our grid, initially all cells are disallowed to visit
    arr = [[0] * W for _ in range(H)]

    # next we add simple random lines to create a maze-like paths on the grid
    # (just to test our implementation)
    x, y = 0, 0
    for _ in range(250):
        axis = randrange(2)
        ds = randrange(2) * 2 - 1
        for step in range(randrange(W)):
            nx = x + ds * axis
            ny = y + ds * (1 - axis)
            if nx < 0 or nx == W or ny < 0 or ny == H:
                break
            x, y = nx, ny
            arr[y][x] = 1
    # in this case, starting cell (0, 0) and the final (x, y) is reachable

    d = dijkstra(arr, x, y)
    print(f"distance: {d}")
    show_grid(arr)
