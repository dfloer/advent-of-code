def day13(n=1350, goal_x=31, goal_y=39):
    x, y = (1, 1)
    return find_path(n, x, y, goal_x, goal_y)


def find_path(n, x, y, goal_x, goal_y):
    """
    Simplified A* because we don't need to determine a heuristic, every possible choice is assumed to have equal weighting to get us to our goal.
    Search space is quite small (upper bound of ~1200 steps), so no major optimizations needed.
    Originally I had written a version with a heuristic that weighted ones with a lower Manhattan distance to the goal higher and that used a heapq with this priority,
        but it was buggy so I tore out everything I didn't absolutely need to implement A*.
    It's late, this might actually just be Dijkstra's algorithm.
    """
    start = (x, y)
    closed_set = {start}
    open_set = {start}
    steps = 0
    while True:
        check = open_set.copy()
        open_set = set()
        for start_x, start_y in check:
            for neighbour in [a for a in get_neighbours(start_x, start_y)]:
                if is_wall(*neighbour, n) or neighbour in closed_set:
                    continue
                closed_set.add(neighbour)
                open_set.add(neighbour)
        steps += 1
        if (goal_x, goal_y) in open_set:
                return steps


def is_wall(x, y, n):
    """
    Returns True if the space we're looking at is a wall, False if it's an open space.
    """
    e = x * x + 3 * x + 2 * x * y + y + y * y
    return bin(e + n).count("1") % 2 == 1


def get_neighbours(x, y):
    """
    Returns the up, down, left, and right neighbours of the given position, as long as they're +'ve.
    """
    out = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(a, b) for a, b in out if not a < 0 or not b < 0]
