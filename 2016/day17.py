from hashlib import md5
from itertools import compress


def day17(inp):
    s = inp
    start = (0, 0)
    goal = (3, 3)
    door_poss = "UDLR"
    bounds = (0, 1, 2, 3)
    q = [(start, [start], [])]
    while q:
        posn, path, dirs = q.pop(0)
        open_doors = [is_open(x) for x in get_hash4(s + ''.join(dirs))]
        for d in compress(door_poss, open_doors):
            nxt = get_move(d, posn)
            nx, ny = nxt
            if nx not in bounds and ny not in bounds:
                continue
            elif nxt == goal:
                return ''.join(dirs + [d])
            else:
                q += [(nxt, path + [nxt], dirs + [d])]


def is_open(x):
    if x in 'bcdef':
        return True
    return False


def get_hash4(a):
    h = md5()
    h.update(a.encode('utf-8'))
    x = h.hexdigest()[:4]
    return x


def get_move(m, p):
    x, y = p
    moves = {'U': (x, y - 1), 'D': (x, y + 1), 'R': (x + 1, y), 'L': (x - 1, y)}
    return moves[m]
