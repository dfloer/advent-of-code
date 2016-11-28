def day3_split():
    with open('day3.txt', 'r') as f:
        lines = f.read()
    return list(lines)


def day3_pt1():
    actions = day3_split()
    return len(day3_common(actions))


def day3_common(actions):
    start = (0, 0)
    house = set()
    for a in actions:
        end = tuple([sum(x) for x in zip(start, action_to_xy(a))])
        house.add(end)
        start = end
    return house


def day3_pt2():
    actions = day3_split()
    santa = actions[0:][::2]
    robo_santa = actions[1:][::2]
    santa_count = day3_common(santa)
    robo_santa_count = day3_common(robo_santa)
    return len(santa_count.union(robo_santa_count))


def action_to_xy(action):
    if action == '<':
        return -1, 0
    if action == '>':
        return 1, 0
    if action == '^':
        return [0, 1]
    if action == 'v':
        return [0, -1]
