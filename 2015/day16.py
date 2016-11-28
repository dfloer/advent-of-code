machine_results = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
                       'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def day16_split():
    with open('day16.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day16_parse():
    lines = day16_split()
    l = [x.rstrip('\n').split(' ') for x in lines]
    d = {}
    for e in l:
        e = [x.strip(',').strip(':') for x in e]
        d[int(e[1])] = {e[2]: int(e[3]), e[4]: int(e[5]), e[6]: int(e[7])}
    return d

def day16_pt1():
    lines = day16_parse()
    for k, v in lines.items():
        if all(item in machine_results.items() for item in v.items()):
            return k

def day16_pt2():
    lines = day16_parse()
    for k, v in lines.items():
        a = [x for x in v.items()]
        hit = []
        for x, y in a:
            comp = machine_results[x]
            if x in ('cats', 'trees') and y > comp:
                hit += [True]
                continue
            if x in ('pomeranians', 'goldfish') and y < comp:
                hit += [True]
                continue
            if y == comp and x not in ('cats', 'trees', 'pomeranians', 'goldfish'):
                hit += [True]
                continue
        if len(hit) == 3:
            print(k)


def day16_pt2_a():
    lines = day16_parse()
    res = None
    for x, y in lines.items():
        if len({k: v for k, v in y.items() if check_valid(k, v)}) == 3:
            res = x
    print(res)


def check_valid(x, y):
    comp = machine_results[x]
    if x in ('cats', 'trees') and y > comp:
        return True
    if x in ('pomeranians', 'goldfish') and y < comp:
        return True
    if y == comp and x not in ('cats', 'trees', 'pomeranians', 'goldfish'):
        return True