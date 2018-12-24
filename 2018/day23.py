import re
import operator
from z3 import Int, If, Optimize

def day23_split():
    with open('day23.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day23_split()
    res = {}
    for line in lines:
        x, y, z, r = [int(x) for x in re.findall(r'-?\d+', line)]
        res[(x, y, z)] = r
    return res


def day23():
    nanobots = parse()
    v = sorted(nanobots.items(), key=operator.itemgetter(1))
    biggest_radius = v[-1][1]
    biggest_key = v[-1][0]
    inside = []
    for bot in nanobots.keys():
        distance = manhattan(bot, biggest_key)
        if distance <= biggest_radius:
            inside += [bot]
    part1 = len(inside)

    res = z3_part2(nanobots)
    part2 = manhattan(res, (0, 0, 0))
    return part1, part2


def z3_part2(nanobots):
    x, y, z = (Int('x'), Int('y'), Int('z'))
    p = (x, y, z)
    start = (0, 0, 0)
    nanobots_z3 = x * 0
    optimizer = Optimize()
    # Transform the input into something z3 understands.
    # This uses the Manhattan distance to set contraints.
    for k, v in nanobots.items():
        nanobots_z3 += If(z3_manhattan(p, k) <= v, 1, 0)
    # This is why I switched to this. I want to maximize the number of nanobots in range.
    optimizer.maximize(nanobots_z3)
    # While also minimizing the distance to (0, 0, 0).
    optimizer.minimize(z3_manhattan(start, (x, y, z)))
    optimizer.check()
    # Actually run things.
    model = optimizer.model()
    return model[x].as_long(), model[y].as_long(), model[z].as_long()


def z3_abs(x):
    return If(x >= 0, x, -x)


def z3_manhattan(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return z3_abs(x1 - x2) + z3_abs(y1 - y2) + z3_abs(z1 - z2)


def manhattan(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


if __name__ == "__main__":
    pt1, pt2 = day23()
    print(f"Solution to day 23 part 1: {pt1}")
    print(f"Solution to day 23 part 2: {pt2}")
