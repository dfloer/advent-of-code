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


def day21(part_2=False):
    """
    After the previous version didn't work, I spent some time reverse engineering the code.
    Hopefully the code is descriptive enough as to what the algorithm is actually doing.
    I was helped along by the only instruction accessing r0 being the eqrr instruction.

    The first segment is my attempt to make this a general problem, but other people's input may differ in terms of which line the constants are all on.
    """
    max_runs = 50000
    _, instructions = parse()
    seti_input = instructions[7][1]
    bani_1 = instructions[10][2]
    bani_2 = instructions[12][2]
    or_test = instructions[6][2]
    muli_test = instructions[11][2]
    d = 0
    pt2_candidates = set()
    others = []
    i = 0
    while True:
        e = d | or_test
        d = seti_input
        while True:
            i += 1
            c = e & 255
            d += c
            d &= bani_1
            d *= muli_test
            d &= bani_2
            if 256 > e and not part_2:
                return d
            elif 256 > e:
                if d not in pt2_candidates:
                    others += [d]
                pt2_candidates.add(d)
                break
            c = 0
            e = e // 256  # Needed for performance.
            # This is a hack to make the program end, no idea if it works for anything other than my input.
            if i >= max_runs:
                return list(others)[-1]


if __name__ == "__main__":
    print(f"Solution to day 21 part 1: {day21()}")
    print(f"Solution to day 21 part 2: {day21(True)}")
