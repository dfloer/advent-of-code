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
    max_idx, _ = find_max(fuel_cells, 3)
    max_max_idx = (0, 0)
    max_size = 0
    max_max_val = 0
    # This solution is very slow, I didn't wait for it to finish but found the first answer that looked right and submitted it. It was correct.
    for square_size in range(1, 301):
        idx, val = find_max(fuel_cells, square_size)
        print(idx, square_size)
        if val > max_max_val:
            max_max_val = val
            max_size = square_size
            max_max_idx = idx
    a, b = max_idx
    c, d = max_max_idx
    e = max_size
    return f"{a},{b}", f"{c},{d},{e}"


def find_max(fuel_cells, square_size):
    max_idx = (0, 0)
    max_val = 0
    for x in range(1, 301 - square_size):
        for y in range(1, 301 - square_size):
            t = square_total(x, y, fuel_cells, square_size)
            if t > max_val:
                max_val = t
                max_idx = (x, y)
    return (max_idx, max_val)


def square_total(x, y, d, s):
    n = 0
    for a in range(x, x + s):
        for b in range(y, y + s):
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
    pt1, pt2 = day11()
    print(f"Solution to day 8 part 1: {pt1}")
    print(f"Solution to day 8 part 2: {pt2}")