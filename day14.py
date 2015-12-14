import operator

def day14_split():
    with open('day14.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day14_parse():
    lines = day14_split()
    l = [x.rstrip('\n').split(' ') for x in lines]
    d = {}
    for e in l:
        d[e[0]] = [int(e[3]), int(e[6]), int(e[13])]
    return d


def day14(t):
    d = day14_parse()
    # d = {'Comet': [14, 10, 127], 'Dancer': [16, 11, 162]}
    dist = {k: v + v for k, v in d.items()}
    res = {k: 0 for k in d.keys()}
    for x in range(t):
        for k, v in dist.items():
            if v[4] == 0 and v[5] == 0:  # Reindeer is done going and resting, go back to both.
                v[4] = v[1]
                v[5] = v[2]
            if v[4] == 0:  # Reindeer is resting, countdown their resting clock
                v[5] -= 1
            else:  # Reindeer is moving and not resting.
                v[4] -= 1
                res[k] += v[0]
    print(sorted(res.items(), key=operator.itemgetter(1)))



