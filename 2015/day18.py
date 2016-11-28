from copy import deepcopy


def day18_split():
    with open('day18.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day18_parse():
    lines = day18_split()
    output = []
    for line in lines:
        l = [True if x == '#' else False for x in line.rstrip('\n') ]
        output.append(l)
    return output


def day18(steps=100, stuck_corners=False):
    lights = day18_parse()
    if stuck_corners:
        for x, y in ((0, 0), (99, 99), (0, 99), (99, 0)):
            lights[x][y] = True
    for _ in range(steps):
        next_lights = deepcopy(lights)
        for x in range(100):
            for y in range(100):
                num_on = num_adjacent(lights, x, y)
                this_light = lights[x][y]
                if (x, y) in ((0, 0), (99, 99), (0, 99), (99, 0)) and stuck_corners:
                    next_lights[x][y] = True
                elif this_light:
                    if num_on in (2, 3):
                        next_lights[x][y] = True
                    else:
                        next_lights[x][y] = False
                else:
                    if num_on == 3:
                        next_lights[x][y] = True
                    else:
                        next_lights[x][y] = False
        lights = next_lights
    return day18_count(lights)


def day18_count(lights):
    flatten = [x for sublist in lights for x in sublist]
    return flatten.count(True)


def num_adjacent(lights, x, y):
    adjacent = [row[max(0, y - 1) : y + 2] for row in lights[max(0, x - 1): x + 2]]
    this_light = lights[x][y]
    flatten = [x for sublist in adjacent for x in sublist]
    num_on = flatten.count(True)
    if this_light:
        num_on -= 1
    return num_on
