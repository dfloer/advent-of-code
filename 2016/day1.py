from collections import OrderedDict

def day1_split():
    with open('day1.txt', 'r') as f:
        lines = f.read().split(', ')
    return lines


def day1(part1=True):
    lines = day1_split()
    loc = [0, 0]
    direction = 0
    visited = OrderedDict()
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

            if not part1:
                key = tuple(loc)
                if key in visited.keys():
                    return abs(loc[0]) + abs(loc[1])
                else:
                    visited[key] = 1

    return abs(loc[0]) + abs(loc[1])
