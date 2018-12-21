def day21_split():
    with open('day21.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day21_split()
    res = []
    ip = -1
    for line in lines:
        line = line.split(' ')
        if "#ip" in line:
            ip = int(line[-1])
        else:
            inst = (line[0], int(line[1]), int(line[2]), int(line[3]))
            res += [inst]
    return ip, res


def day21():
    """
    After the previous version didn't work, I spent some time reverse engineering the code.
    Hopefully the code is descriptive enough as to what the algorithm is actually doing.
    I was helped along by the only instruction accessing r0 being the eqrr instruction.
    """
    _, instructions = parse()
    seti_input = instructions[7][1]
    bani_1 = instructions[10][2]
    bani_2 = instructions[12][2]
    or_test = instructions[6][2]
    muli_test = instructions[11][2]
    d = 0
    while True:
        e = d | or_test
        d = seti_input
        while True:
            c = e & 255
            d += c
            d &= bani_1
            d *= muli_test
            d &= bani_2
            if 256 > e:
                return d
            c = 0


if __name__ == "__main__":
    print(f"Solution to day 21 part 1: {day21()}")
    # print(f"Solution to day 21 part 2: {}")
