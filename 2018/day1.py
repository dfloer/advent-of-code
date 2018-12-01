def day1_split():
    with open('day1.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day1_part1(start=0):
    freq = start
    for l in day1_split():
        x = int(l)
        freq += x
    return freq


def day1_part2(start=0):
    freq = start
    freqs = set()
    updates = day1_split()
    idx = 0
    while True:
        x = int(updates[idx % len(updates)])
        freq += x
        if freq in freqs:
            return freq
        else:
            freqs.add(freq)
        idx += 1


if __name__ == "__main__":
    print(f"Solution to day 1 part 1: {day1_part1()}")
    print(f"Solution to day 1 part 1: {day1_part2()}")
