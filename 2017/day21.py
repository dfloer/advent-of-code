import numpy as np


def day21_split():
    with open('day21.txt', 'r') as f:
        lines = f.read().splitlines()
    res = {}
    for l in lines:
        match, result = l.split(" => ")
        res[convert_string_np(match).tobytes()] = convert_string_np(result)
    return res


def convert_np_bytes(b):
    if len(b) == 4:
        return np.frombuffer(b, dtype=bool).reshape(2, 2)
    else:
        return np.frombuffer(b, dtype=bool).reshape(3, 3)


def convert_string_np(s):
    # Convert # to True, . to False
    return np.array([[c == '#' for c in x] for x in s.split('/')])


def create_new_rules_np(rule):
    res = [rule]
    res += [np.fliplr(rule)]
    res += [np.flipud(rule)]
    for x in range(4):
        res += [np.rot90(rule, x)]
        res += [np.fliplr(np.rot90(rule, x))]
        res += [np.flipud(np.rot90(rule, x))]
    return res


def lights_enhance(lights, rules):
    size = len(lights)
    if size % 2 == 0:
        dim = 2
    else:
        dim = 3
    # calculate the size of our new "enhanced" grid of lights.
    new_size = size * (dim + 1) // dim
    # New, empty grid for the lights.
    new_lights = np.empty((new_size, new_size), dtype=bool)
    for i, new_i in zip(range(0, size, dim), range(0, new_size, dim + 1)):
        for j, new_j in zip(range(0, size, dim), range(0, new_size, dim + 1)):
            square = lights[i : i + dim, j : j + dim]
            new_square = rules[square.tobytes()]
            new_lights[new_i : new_i + 1 + dim, new_j : new_j + 1 + dim] = new_square
    return new_lights


def day21_part1(iterations=5):
    start = convert_string_np(".#./..#/###")
    raw_rules = day21_split()
    enhancement_rules = {}
    for k, v in raw_rules.items():
        new_rules = create_new_rules_np(convert_np_bytes(k))
        for r in new_rules:
            enhancement_rules[r.tobytes()] = v
    lights = start
    for _ in range(iterations):
        lights = lights_enhance(lights, enhancement_rules)
    return lights.sum()


if __name__ == "__main__":
    print(f"Solution to day21 part1: {day21_part1()}")
    print(f"Solution to day21 part1: {day21_part1(18)}")
