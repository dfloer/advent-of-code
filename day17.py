from itertools import combinations


def day17_split():
    with open('day17.txt', 'r') as f:
        lines = f.readlines()
    return [int(x) for x in lines]


def day17(target=150):
    volumes = day17_split()
    combos = []
    for x in range(1, len(volumes) + 1):
        combos += combinations(volumes, x)
    valid_combos = [len(x) for x in combos if sum(x) == target]
    minimum = min(valid_combos)
    return len(valid_combos), valid_combos.count(minimum)
