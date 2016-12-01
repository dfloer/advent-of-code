from collections import OrderedDict


def day1_split():
    with open('day1.txt', 'r') as f:
        lines = f.read().split(', ')
    return lines


def day1():
    lines = day1_split()
    loc = [0, 0]
    direction = 0
    visited = OrderedDict()
    pt2_soln = 0
    for i in lines:
        turn = i[0 : 1]
        amount = int(i[1 :])

        if turn == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        for _ in range(amount):
            if direction == 0:
                loc[0] += 1
            elif direction == 2:
                loc[0] -= 1
            elif direction == 1:
                loc[1] += 1
            else:
                loc[1] -= 1

            key = tuple(loc)
            if key in visited.keys() and not pt2_soln:
                pt2_soln = abs(loc[0]) + abs(loc[1])
            else:
                visited[key] = 1

    pt1_soln = abs(loc[0]) + abs(loc[1])

    return "Part1: {}, part2: {}".format(pt1_soln, pt2_soln)
