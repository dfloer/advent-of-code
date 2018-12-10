import re

def day10_split():
    with open('day10.txt', 'r') as f:
        data = f.readlines()
    return data


def parse():
    lines = day10_split()
    positions = {}
    for idx, line in enumerate(lines):
        e = re.findall(r'-?\d+', line)  # regex to find all numbers in input.
        x = int(e[0])
        y = int(e[1])
        v1 = int(e[2])
        v2 = int(e[3])
        positions[(x, y, idx)] = (v1, v2)
    return positions


def day9():
    start_positions = parse()
    message = ''
    new_positions = start_positions
    count = 0
    bbox_size = float("inf")
    bbox = 0
    while not message:
        count += 1
        next_positions = {(k[0] + v[0], k[1] + v[1], k[2]): v for k, v in new_positions.items()}
        bbox_new = find_bbox([(a, b) for a, b, _ in next_positions.keys()])
        size = abs(bbox_new[1] - bbox_new[0]) * abs(bbox_new[3] - bbox_new[2])
        if size < bbox_size:
            bbox_size = size
        else:
            res = new_positions
            print_values(res, bbox)
            break
        new_positions = next_positions
        bbox = bbox_new
    return count - 1


def print_values(positions, bbox):
    print('')
    x1, x2, y1, y2 = bbox
    for y in range(y1, y2 + 1):
        print('   ', end='')
        for x in range(x1, x2 + 1):
            if (x, y) in [(a, b) for a, b, _ in positions.keys()]:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')


def find_bbox(coords):
    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = float("-inf"), float("-inf")
    for x, y in coords:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        elif y > max_y:
            max_y = y
    return min_x, max_x, min_y, max_y


if __name__ == "__main__":
    print(f"Solution to day 10 part 2: {day9()}")
