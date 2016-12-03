def day3_split():
    with open('day3.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day3():
    triangles = [x.split() for x in day3_split()]
    count = 0
    total = len(triangles)
    for x in triangles:
        sides = sorted([int(y) for y in x])
        if sides[0] + sides[1] <= sides[2]:
            count += 1
    return total - count
