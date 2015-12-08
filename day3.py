def day3_split():
    with open('day3.txt', 'r') as f:
        lines = f.read()
    return list(lines)


def day3():
    actions = day3_split()
    start = (0, 0)
    house = set()
    for a in actions:
        end = tuple([sum(x) for x in zip(start, action_to_xy(a))])
        house.add(end)
        start = end
    return len(house)


def action_to_xy(action):
    if action == '<':
        return -1, 0
    if action == '>':
        return 1, 0
    if action == '^':
        return [0, 1]
    if action == 'v':
        return [0, -1]
