from collections import Counter


def day6_split():
    with open('day6.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day6():
    data = day6_split()
    part1_res = ''
    part2_res = ''
    rotated = list(zip(*data[::-1]))
    for line in rotated:
        counts = Counter(line).most_common()
        part1_res += counts[0][0]
        part2_res += counts[-1][0]
    return part1_res, part2_res
