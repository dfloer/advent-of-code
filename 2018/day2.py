from collections import Counter


def day2_split():
    with open('day2.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines
    # return ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]


def day2_part1():
    lines = day2_split()
    return checksum(lines)


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


if __name__ == "__main__":
    print(f"Solution to day 2 part 1: {day2_part1()}")
