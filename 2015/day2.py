def day2_split():
    with open('day2.txt', 'r') as f:
        lines = f.readlines()
    return [[int(y) for y in x.split('x')] for x in lines]


def day2():
    boxes = day2_split()
    for x in boxes:
        x.sort()
    total_paper = sum([(x[0] * x[1]) * 3 + (x[1] * x[2]) * 2 + (x[2] * x[0]) * 2 for x in boxes])
    total_ribbon = sum([(x[0] * x[1] * x[2]) + 2 * (x[0] + x[1]) for x in boxes])
    return total_paper, total_ribbon
