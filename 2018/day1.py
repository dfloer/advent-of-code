def day1_split():
    with open('day1.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day1(start=0):
    freq = start
    for l in day1_split():
        x = int(l)
        freq +=x
    return freq


if __name__ == "__main__":
    print(f"Solution to day 1 part 1: {day1()}")
