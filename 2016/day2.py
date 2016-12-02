def day2_split():
    with open('day2.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day2_part1():
    lines = day2_split()
    instructions = [list(x) for x in lines]
    start = 5
    previous_button = start

    code = []
    for digit in instructions:
        for move in digit:
            if move == "D":
                amount = 3
            elif move == "U":
                amount = -3
            elif move == "R":
                amount = 1
            else:
                amount = -1

            if previous_button in (1, 2, 3) and move == "U":
                amount = 0
            elif previous_button in (7, 8, 9) and move == "D":
                amount = 0
            elif previous_button in (1, 4, 7) and move == "L":
                amount = 0
            elif previous_button in (3, 6, 9) and move == "R":
                amount = 0
            else:
                pass
            previous_button += amount
        code += [previous_button]
    return ''.join([str(x) for x in code])


def day2_part2():
    lines = day2_split()
    instructions = [list(x) for x in lines]
    start = [3, 1]
    previous_button = start
    code = []
    for digit in instructions:
        for move in digit:
            x = 0
            y = 0
            if move == "D":
                x = 1
            elif move == "U":
                x = -1
            elif move == "R":
                y = 1
            else:
                y = -1
            x_inc = previous_button[0] + x
            y_inc = previous_button[1] + y
            next_button = get_keypad_value(x_inc, y_inc)
            if next_button != '0':
                previous_button = [x_inc, y_inc]
        code += [get_keypad_value(previous_button[0], previous_button[1])]
    return ''.join([str(x) for x in code])


def get_keypad_value(x, y):
    keypad2 = [
              "0000000",
              "0001000",
              "0023400",
              "0567890",
              "00ABC00",
              "000D000",
              "0000000"]
    return keypad2[x][y]
