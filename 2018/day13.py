import colorama
from collections import Counter

colorama.init()

def day13_split():
    with open('day13.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day13_split()
    tracks = {}
    # for l in lines:
    #     print(l, end='')
    for y, line in enumerate(lines):
        for x, e in enumerate(line):
            if e == '^':
                track = find_loop_y((x, y), lines, -1)
                tracks[(y, x)] = track
            elif e == 'v':
                track = find_loop_y((x, y), lines, -1)
                tracks[(x, y)] = track
            # if e == '>':
            #     track = find_loop_x((x, y), lines, 1)
            #     tracks[(x, y)] = track
            # elif e == '<':
            #     track = find_loop_x((x, y), lines, -1)
            #     tracks[(x, y)] = track
    return tracks


def find_loop_y(start, tracks, y_direction):
    start_x, start_y = start
    y = start_y
    x = start_x
    corner = []
    # Go from the start position to the first corner, up or down.
    while True:
        e = tracks[y][x]
        if e == '\\':
            corner += [(x, y)]
            break
        elif e == '/':
            corner += [(x, y)]
            break
        else:
            y += y_direction
    # Find the other corner.
    y_direction = -y_direction
    y = start_y
    while True:
        e = tracks[y][x]
        if e == '\\':
            x_direction = -1
            if y_direction == 1:
                x_direction = 1
            corner += [(x, y)]
            break
        elif e == '/':
            x_direction = 1
            if y_direction == 1:
                x_direction = -1
            corner += [(x, y)]
            break
        else:
            y += y_direction
    # Find a third corner. As they are rectangles, we can infer the last corner.
    x += x_direction
    while True:
        e = tracks[y][x]
        if e == '\\':
            corner += [(x, y)]
            break
        elif e == '/':
            corner += [(x, y)]
            break
        else:
            x += x_direction

    corner += [(corner[2][0], corner[0][1])]
    path = set()
    test = []
    ma = max(corner)
    mi = min(corner)
    print(corner)
    for a in range(mi[0], ma[0]):
        path.add((a, mi[1]))
        path.add((a, ma[1]))
        test += [(a, mi[1])]
        test += [(a, ma[1])]
    for b in range(mi[1], ma[1]):
        path.add((mi[0], b))
        path.add((ma[0], b))
        test += [(mi[0], b)]
        test += [(ma[0], b)]
    print(len(test), len(path))
    return path


def find_loop_x(start, tracks, x_direction):
    start_x, start_y = start
    e = tracks[start_y][start_x]
    y = start_y
    x = start_x
    corner = []
    # Go from the start position to the first corner, left or right.
    while True:
        e = tracks[y][x]
        # print(x, y, e)
        if e == '\\':
            corner += [(x, y)]
            break
        elif e == '/':
            corner += [(x, y)]
            break
        else:
            x += x_direction
    # Find the other corner.
    x_direction = -x_direction
    x = start_x
    while True:
        e = tracks[y][x]
        # print(x, y, e)
        if e == '\\':
            y_direction = -1
            if x_direction == 1:
                y_direction = 1
            corner += [(x, y)]
            break
        elif e == '/':
            y_direction = 1
            if x_direction == 1:
                y_direction = -1
            corner += [(x, y)]
            break
        else:
            x += x_direction
    # Find a third corner. As they are rectangles, we can infer the last corner.
    y += y_direction
    while True:
        e = tracks[y][x]
        # print(x, y, e)
        if e == '\\':
            corner += [(x, y)]
            break
        elif e == '/':
            corner += [(x, y)]
            break
        else:
            y += y_direction
    corner += [(corner[0][0], corner[2][1])]
    path = set()
    ma = max(corner)
    mi = min(corner)
    for a in range(mi[0], ma[0]):
        path.add((a, mi[1]))
        path.add((a, ma[1]))
    for b in range(mi[1], ma[1] + 1):
        path.add((mi[0], b))
        path.add((ma[0], b))


    # for c in corner:
    #     path.add(c)
    return path


def day13():
    res = parse()
    # print(res)
    print_debug(res)


def print_debug(tracks):
    all_tracked = []
    for k, v in tracks.items():
        all_tracked += v
    raw = day13_split()
    rows = 150
    cols = 150
    t = ('<', '>', 'v', '^')
    for r in range(rows):
        for c in range(cols):
            try:
                e = raw[r][c]
            except IndexError:
                e = '#'
            if (c, r) in all_tracked and e not in t:
                print(colorama.Style.BRIGHT + colorama.Fore.MAGENTA + e, end='')
            elif e in t:
                print(colorama.Style.BRIGHT + colorama.Fore.CYAN + e, end='')
            else:
                print(colorama.Style.NORMAL + colorama.Fore.GREEN + e, end='')
        print('')





if __name__ == "__main__":
    print(f"\nSolution to day 13 part 1: {day13()}")