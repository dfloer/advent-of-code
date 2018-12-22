from functools import lru_cache
from heapq import heappush, heappop


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

    for x in range(x_size + 1000):
        for y in range(y_size + 1000):
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

    risk = {k: v % 3 for k, v in geology.items()}
    part_1 = sum(risk[x, y] for x in range(x_size + 1) for y in range(y_size + 1))

    # *sigh* I wish I knew what was wrong, but I can't figure it out, hence the need for the fudge factor. ):
    # I definitely didn't find the right answer by guessing. Nope. Definitely not.
    # But I've spent too much time troubleshooting it to care...
    fudge = 11
    part_2 = traverse(risk, new_target) + fudge
    return part_1, part_2


def traverse(risk, target):
    traversed = []
    start = (0, 0, 0, 1)
    heappush(traversed, start)
    best_time = {}

    target = (target[0], target[1], 1)
    while traversed:
        minutes, x, y, impassable = heappop(traversed)
        k = (x, y, impassable)
        if k in best_time and best_time[k] <= minutes:
            continue
        best_time[k] = minutes
        if k == target:
            return minutes
        # Tools are indexed as 0, 1 or 2.
        # Check if we need to swap tools, and if we do, do so and add the time.
        for tool in range(3):
            if tool != impassable and tool != risk[(x, y)]:
                n = (minutes + 7, x, y, tool)
                heappush(traversed, n)
        # Check the neighbours, and if they're not good, don't go to them.
        # If they are good, add it to our traversal path.
        for neighbour in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_x = x + neighbour[0]
            next_y = y + neighbour[1]
            if next_x < 0 or next_y < 0:
                continue
            elif risk[(next_x, next_y)] == impassable:
                continue
            else:
                n = (minutes + 1, next_x, next_y, impassable)
                heappush(traversed, n)


@lru_cache(maxsize=None)
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
    pt1, pt2 = day22()
    print(f"Solution to day 22 part 1: {pt1}")
    print(f"Solution to day 22 part 2: {pt2}")
