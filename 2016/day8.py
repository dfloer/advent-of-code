def day8_split():
    with open('day8.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day8(screen_width=50, screen_height=6):
    data = day8_split()
    pixels = [[0 for _ in range(screen_width)] for _ in range(screen_height)]
    for line in data:
        split = line.split()
        op = split[0]
        if op == "rect":
            w, h = split[1].split('x')
            for i in range(int(w)):
                for j in range(int(h)):
                    pixels[j][i] = 1
        elif op == "rotate":
            direction = split[1]
            idx = int(split[2].split('=')[1])
            amount = int(split[4])
            if direction == "row":
                row = pixels[idx]
                amount *= -1
                new_row = row[amount:] + row[:amount]
                pixels[idx] = new_row
            elif direction == "column":
                # Aww yiss. Rotate once, treat it like a column and then rotate 3 times. Yeah...
                rotated_pixels = [list(a) for a in zip(*pixels[::-1])]
                col = rotated_pixels[idx]
                new_col = col[amount:] + col[:amount]
                rotated_pixels[idx] = new_col
                pixels_a = [list(a) for a in zip(*rotated_pixels[::-1])]
                pixels_b = [list(a) for a in zip(*pixels_a[::-1])]
                pixels = [list(a) for a in zip(*pixels_b[::-1])]
            else:
                print("unknown direction")
        else:
            print("unknown operations")
            break
    pprint_lists(pixels)
    return sum(flatten(pixels))


def flatten(l):
    return[val for sublist in l for val in sublist]


def pprint_lists(l):
    for x in l:
        for y in x:
            if y == 1:
                c = '#'
            else:
                c = '.'
            print(c, "", end='')
        print()
