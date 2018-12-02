from collections import Counter
from difflib import ndiff


def day2_split():
    with open('day2.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines
    # return ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]


def day2_part1():
    lines = day2_split()
    return checksum(lines)


def day2_part2():
    lines = day2_split()
    return str_cmp(lines)


def checksum(lines):
    twos = 0
    threes = 0
    for l in lines:
        c = Counter(l).values()
        if 3 in c:
            threes += 1
        if 2 in c:
            twos += 1
    return twos * threes


def str_cmp(lines):
    length = len(lines[0])
    for x in range(len(lines)):
        for y in range(len(lines) - 1):
            diff = list(ndiff(lines[x], lines[y]))
            if len(diff) == length + 1:
                res = ''
                for x in diff:
                    if x[0] in ('-', '+'):
                        continue
                    else:
                        res += x[2]
                return res


if __name__ == "__main__":
    print(f"Solution to day 2 part 1: {day2_part1()}")
    print(f"Solution to day 2 part 1: '{day2_part2()}'")
