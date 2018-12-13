def day13_split():
    with open('day13.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse():
    lines = day13_split()
    tracks = {}
    for y, line in enumerate(lines):
        for x, e in enumerate(line):
            if e == '^':
                track = find_loop_y((x, y), lines, -1)
                tracks[(x, y)] = track
            # elif e == 'v':
            #     track = find_loop_y((x, y), lines, -1)
            #     tracks[(x, y)] = track
            # elif e == '>':
            #     track = find_loop_x((x, y), lines, 1)
            #     tracks[(x, y)] = track
            # elif e == '<':
            #     track = find_loop_x((x, y), lines, -1)
            #     tracks[(x, y)] = track
    return tracks


def find_loop_y(start, tracks, y_direction):
    start_x, start_y = start
    e = tracks[start_y][start_x]
    y = start_y + y_direction
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
    y = start_y + y_direction
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

    path = set()
    for a in range(corner[0][0], corner[2][0] + 1, x_direction):
        path.add((a, corner[0][1]))
        path.add((a, corner[2][1]))
    for b in range(corner[0][1], corner[2][1] + 1, y_direction):
        path.add((corner[0][0], b))
        path.add((corner[2][0], b))
    return path


def find_loop_x(start, tracks, x_direction):
    start_x, start_y = start
    e = tracks[start_y][start_x]
    y = start_y
    x = start_x + x_direction
    corner = []
    # Go from the start position to the first corner, left or right.
    x += x_direction
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
    x = start_x + x_direction
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
    path = set()
    for a in range(corner[0][0], corner[2][0] + 1, x_direction):
        path.add((a, corner[0][1]))
        path.add((a, corner[2][1]))
    for b in range(corner[0][1], corner[2][1] + 1, y_direction):
        path.add((corner[0][0], b))
        path.add((corner[2][0], b))
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
    print(rows, cols)
    for c in range(rows):
        for r in range(cols):
            try:
                e = raw[r][c]
            except IndexError:
                e = '#'
            if (r, c) in all_tracked:
                print(e, end='')
            else:
                print(' ', end='')
        print('')





if __name__ == "__main__":
    print(f"Solution to day 13 part 1: {day13()}")