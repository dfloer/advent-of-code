def day2_split():
    with open('day2.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day2():
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
            previous_button = previous_button + amount

        code += [previous_button]
    return ''.join([str(x) for x in code])
