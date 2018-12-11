from collections import defaultdict


def day11_split():
    with open('day11.txt', 'r') as f:
        data = f.read()
    return int(data)


def day11():
    serial = day11_split()
    fuel_cells = defaultdict(int)
    print(serial)
    for x in range(1, 301):
        for y in range(1, 301):
            fuel_cells[(x, y)] = power_level(x, y, serial)

    max_idx = (0, 0)
    max_val = 0
    for x in range(1, 298):
        for y in range(1, 298):
            t = square_total(x, y, fuel_cells)
            if t > max_val:
                max_val = t
                max_idx = (x, y)
    a, b = max_idx
    return f"{a},{b}"


def square_total(x, y, d):
    n = 0
    for a in range(x, x + 3):
        for b in range(y, y + 3):
            n += d[(a, b)]
    return n


def power_level(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    try:
        power_level = int(str(power_level)[-3])
    except IndexError:
        power_level = 0
    power_level -= 5
    return power_level


if __name__ == "__main__":
    print(f"Solution to day 11 part 1: {day11()}")
    #print(f"Solution to day 11 part 2: {day11()}")