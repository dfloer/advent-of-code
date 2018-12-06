from collections import Counter

def day6_split():
    with open('day6.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_input():
    l = day6_split()
    res = {}
    for idx, x in enumerate(l):
        res[idx] = [int(n) for n in x.split(', ')]
    return res


def day6():
    safe_distance = 10000
    data = parse_input()
    # Start by finding a bounding box.
    min_x, max_x, min_y, max_y = find_bbox(data.values())
    res = {}
    region = {}
    # For every point inside our bounding box
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            distances = [find_closest(x, y, *v) for v in data.values()]
            region[(x, y)] = 1 if sum(distances) < safe_distance else 0
            closest = min(distances)
            if distances.count(closest) == 1:
                res[(x, y)] = distances.index(closest)
            else:
                res[(x, y)] = -1
    # This seems fragile, because the largest area could be the finite area inside the box of an infinite area.
    part1 = max(Counter(res.values()).values())
    part2 = sum(region.values())
    return part1, part2


def find_closest(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_bbox(coords):
    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = float("-inf"), float("-inf")
    for x, y in coords:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        elif y > max_y:
            max_y = y
    return min_x, max_x, min_y, max_y


if __name__ == "__main__":
    pt1, pt2 = day6()
    print(f"Solution to day 6 part 1: {pt1}")
    print(f"Solution to day 6 part 2: {pt2}")
