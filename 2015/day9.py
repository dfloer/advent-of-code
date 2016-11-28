from collections import defaultdict
from itertools import permutations


def day9_split():
    with open('day9.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day9_common():
    input_lines = day9_split()
    cities = set()
    for l in input_lines:
        l = l.split(' ')
        source = l[0]
        dest = l[2]
        cities.add(source)
        cities.add(dest)
    all_cities = permutations(cities)
    all_distances = []
    for path in all_cities:
        path_dist = []
        for idx in range(len(path) - 1):
            city_pair = (path[idx], path[idx + 1])
            dist = find_distance(city_pair, input_lines)
            path_dist.extend([dist])
        all_distances.append(sum(path_dist))
    return all_distances


def day9_pt1():
    all_distances = day9_common()
    return min(all_distances)


def day9_pt2():
    all_distances = day9_common()
    return max(all_distances)


def find_distance(pair, lines):
    for line in lines:
        if all(x in line for x in pair):
            return int(line.split(' ')[-1])
