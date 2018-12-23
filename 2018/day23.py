import re
import operator


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
    return len(inside)


def manhattan(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


if __name__ == "__main__":
    print(f"Solution to day 23 part 1: {day23()}")
