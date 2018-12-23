import re
import operator
from collections import defaultdict


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

    bounds = find_bounds(nanobots.keys())
    print(bounds)

    bot_ranges = defaultdict(list)
    # Start by building a list of each bot and which bots are in range of it.
    for bot_key, bot_radius in nanobots.items():
        for bot2_key in nanobots.keys():
            d = manhattan(bot_key, bot2_key)
            if d <= bot_radius:
                bot_ranges[bot_key] += [bot2_key]
    # Find the largest group of bots that all contain each other.
    # bot_groups = {}
    # group_size = {}
    # for k, a in bot_ranges.items():
    #     for ky, b in bot_ranges.items():
    #         group = set(a).intersection(set(b))
    #         key = (k, ky)
    #         bot_groups[key] = group
    #         group_size[key] = len(group)
    #     print(len(bot_groups))
    # vv = sorted(group_size.items(), key=operator.itemgetter(1))
    # print(vv[0], vv[-1])
    t = (50923187, 50166736, 45134786)
    print(manhattan(t, (0, 0, 0)))

    # 146224709 high
    # 98238064 low
    return part1


def find_bounds(points):
    min_x, min_y, min_z = [float("Inf")] * 3
    max_x, max_y, max_z = [-float("Inf")] * 3
    for p in points:
        x, y, z = p
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if z < min_z:
            min_z = z
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
    return (min_x, min_y, min_z), (max_x, max_y, max_z)

def manhattan(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


if __name__ == "__main__":
    print(f"Solution to day 23 part 1: {day23()}")
