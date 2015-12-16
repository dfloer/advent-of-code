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

def day16():
    lines = day16_parse()
    machine_results = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
                       'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    for k, v in lines.items():
        if all(item in machine_results.items() for item in v.items()):
            print(k)


