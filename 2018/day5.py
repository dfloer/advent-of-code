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
    reacted = raw
    while True:
        hits = 0
        for pair in all_pairs:
            if pair in reacted:
                reacted = ''.join(reacted.split(pair))
                hits += 1
        if hits == 0:
            break
    return len(reacted)


if __name__ == "__main__":
    print(f"Solution to day 3 part 1: {day5()}")
    # print(f"Solution to day 3 part 1: {day5()[1]}")
