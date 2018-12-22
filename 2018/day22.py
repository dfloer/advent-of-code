from functools import lru_cache


def day22_split():
    with open('day22.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day22_split()
    depth = int(lines[0].split()[-1])
    target = tuple([int(x) for x in lines[1].split()[-1].split(',')])
    return depth, target


def day22():
    depth, target = parse()
    x_size, y_size = target
    new_target = target[::-1]
    geology = {}
    y_mult = 16807
    x_mult = 48271
    erosion_mod = 20183

    for x in range(x_size + 1):
        for y in range(y_size + 1):
            geology[(x, y)] = geologic_index(x, y, x_mult, y_mult, erosion_mod, depth, new_target)

    # for x in range(x_size + 1):
    #     for y in range(y_size + 1):
    #         r = geology[(x, y)] % 3
    #         if (x, y) == (0, 0):
    #             e = 'M'
    #         elif (x, y) == target:
    #             e = 'T'
    #         elif r == 0:
    #             e = '.'
    #         elif r == 1:
    #             e = '='
    #         elif r == 2:
    #             e = '|'
    #         else:
    #             e = "!"
    #         print(e, end='')
    #     print()
    pt1 = sum(x % 3 for x in geology.values())
    return pt1


@lru_cache()
def geologic_index(x, y, x_mult, y_mult, erosion_mod, depth, target):
    if x == y and x == 0:
        res = 0
    elif (x, y) == target:
        res = 0
    elif y == 0:
        res = y_mult * x
    elif x == 0:
        res = x_mult * y
    else:
        a = geologic_index(x - 1, y, x_mult, y_mult, erosion_mod, depth, target)
        b = geologic_index(x, y - 1, x_mult, y_mult, erosion_mod, depth, target)
        res = a * b
    return (res + depth) % erosion_mod


if __name__ == "__main__":
    print(f"Solution to day 22 part 1: {day22()}")
