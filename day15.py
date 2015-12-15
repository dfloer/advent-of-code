from itertools import permutations
from functools import reduce
import operator


def day15_split():
    with open('day15.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day15_parse():
    lines = day15_split()
    l = [x.rstrip('\n').split(' ') for x in lines]
    d = {}
    for e in l:
        d[e[0]] = [int(e[2].strip(',')), int(e[4].strip(',')), int(e[6].strip(',')), int(e[8].strip(',')), int(e[10].strip(','))]
    return d


def day15_pt1():
    x = day15_parse()
    d = {k: v[:-1] for k, v in x.items()}
    return knapsack(d, 100, None)


def day15_pt2():
    d = day15_parse()
    return knapsack(d, 100, 500)


def f(n, s):
    if n == 1:
        yield (s,)
    else:
        for i in range(s + 1):
            for j in f(n - 1, s - i):
                yield (i,) + j


def knapsack(d, total=100, calories=None):
    # all_orderings = [y for y in permutations([x for x in range(total)], 5) if sum(y) == total]
    all_orderings = list(f(len(d), total))
    res = []
    v = list(d.values())
    for x in all_orderings:
        q = [[z[0] * a for a in z[1]] for z in zip(x, v)]
        r = [max(sum(a), 0) for a in zip(*q)]
        if calories is not None and r[-1] != calories:
            res.append(0)
        elif calories is None:
            res.append(reduce(operator.mul, r, 1))
        else:
            res.append(reduce(operator.mul, r[:-1], 1))
    m = max(res)
    i = res.index(m)
    return m, all_orderings[i]
