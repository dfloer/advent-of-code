from collections import defaultdict


def day3_split():
    with open('day3.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):
    res = {}
    for l in lines:
        ll = l.split()
        elf_id = int(ll[0][1:])
        start = tuple(int(x) for x in ll[2][: -1].split(','))
        size = tuple(int(x) for x in ll[3].split('x'))
        res[elf_id] = {"start": start, "size": size}
    return res


def day3_part1():
    data = parse(day3_split())
    fabric = defaultdict(list)
    for elf_id, claim in data.items():
        start = claim["start"]
        size = claim["size"]
        for x in range(start[0], start[0] + size[0]):
            for y in range(start[1], start[1] + size[1]):
                fabric[(x, y)] += [elf_id]
    total = 0
    for f in fabric.values():
        if len(f) >= 2:
            total += 1
    return total


if __name__ == "__main__":
    print(f"Solution to day 1 part 1: {day3_part1()}")
