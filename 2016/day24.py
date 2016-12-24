from collections import OrderedDict
from itertools import compress, permutations


def day24_split():
    with open('day24.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day24():
    data = day24_split()
    # create a dict with key of (x, y) anv value of the maze location.
    nums = [str(x) for x in range(10)]  # Only single digit numbers.
    nums_shortcut = OrderedDict()
    maze = OrderedDict()
    max_x = len(data)
    max_y = len(data[0])
    for x in range(max_x):
        for y in range(max_y):
            v = data[x][y]
            maze[(x, y)] = v
            if v in nums:
                nums_shortcut[int(v)] = (x, y)
    path_lens = {}
    for start_num, start_pos in nums_shortcut.items():
        for goal_num, goal_pos in nums_shortcut.items():
            if start_num == goal_num:
                continue
            v = bfs(maze, start_pos, goal_pos, max_x, max_y)
            path_lens[(start_num, goal_num)] = v
    res1 = []
    res2 = []
    for a in permutations(range(len(nums_shortcut))):
        if a[0] != 0:
            continue
        d = []
        for b in range(len(a) - 1):
            c = a[b : b + 2]
            d += [path_lens[c]]
        res1 += [sum(d)]
        d = []
        for b in range(len(a)):
            c = a[b : b + 2]
            if len(c) == 1:
                c = (c[0], 0)
            d += [path_lens[c]]
        res2 += [sum(d)]

    return min(res1), min(res2)


def neighbours(x, y):
    n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return n


def bfs(maze, start, goal, max_x, max_y):
    q = []
    q += [(start, [start], [])]
    visited = set()
    visited.add(start)
    while q:
        posn, path, dirs = q.pop(0)
        next_poss = neighbours(*posn)
        open_poss = [True if maze[x] != '#' else False for x in next_poss]
        for d in compress(next_poss, open_poss):
            nxt = d
            nx, ny = nxt
            if nx not in list(range(max_x)) or ny not in list(range(max_y)):
                continue
            elif nxt in visited:
                continue
            elif nxt == goal:
                return len(path)  # off by one?
            else:
                q += [(nxt, path + [nxt], dirs + [d])]
                visited.add(nxt)
    return False
