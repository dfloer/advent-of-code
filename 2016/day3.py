def day3_split():
    with open('day3.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day3_part1():
    triangles = [x.split() for x in day3_split()]
    count = 0
    total = len(triangles)
    for x in triangles:
        sides = sorted([int(y) for y in x])
        if sides[0] + sides[1] <= sides[2]:
            count += 1
    return total - count


def day3_part2():
    triangles = [x.split() for x in day3_split()]
    count = 0
    # Basically creates rows from the columns, though they turn out backwards.
    rotated = list(zip(*triangles[::-1]))
    big_list = []
    # Sticks the three different rows into one big row, because they're all the same size.
    for x in rotated:
        big_list += x
    total = len(big_list) // 3
    # Iterate over the list 3 values at a time and check the inequality as above.
    for idx in range(0, len(big_list), 3):
        triangle = big_list[idx : idx + 3]
        sides = sorted([int(y) for y in triangle])
        if sides[0] + sides[1] <= sides[2]:
            count += 1
    return total - count
