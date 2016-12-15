from collections import OrderedDict


def day15_split():
    with open('day15.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day15():
    discs = OrderedDict()
    data = day15_split()
    for disc in data:
        d = disc.split()
        i = int(d[1][-1])
        posns = int(d[3])
        curr = int(d[-1][:-1])
        discs[i] = {'p': posns, 'c': curr}
    t = 0
    while True:
        ps = []
        for i, v in discs.items():
            c = v['c']
            p = v['p']
            ps += [(c + i + t) % p]
        if sum(ps) == 0:
            return t
        t += 1
