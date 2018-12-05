import re

def day5_split():
    with open('day5.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines[0]


def day5():
    raw = day5_split()
    uppers = [chr(i) for i in range(65, 65 + 26)]
    lowers = [chr(i) for i in range(97, 97 + 26)]
    all_pairs = [x + y for x, y in zip(uppers, lowers)] + [y + x for x, y in zip(uppers, lowers)]
    reacted = react(raw, all_pairs)
    part1 = len(reacted)

    best = len(raw)
    for x in uppers:
        reacted = raw
        stripped = ''.join(reacted.split(x))
        stripped = ''.join(stripped.split(x.lower()))
        new_poly = react(stripped, all_pairs)
        if len(new_poly) < best:
            best = len(new_poly)
    part2 = best
    return part1, part2


def react(polymer, all_pairs):
    while True:
        hits = 0
        for pair in all_pairs:
            if pair in polymer:
                polymer = ''.join(polymer.split(pair))
                hits += 1
        if hits == 0:
            return polymer


if __name__ == "__main__":
    pt1, pt2 = day5()
    print(f"Solution to day 3 part 1: {pt1}")
    print(f"Solution to day 3 part 1: {pt2}")
