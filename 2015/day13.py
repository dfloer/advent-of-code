from itertools import permutations

def day13_split():
    with open('day13.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day13_parse():
    lines = day13_split()
    out = {}
    people = set()
    for l in lines:
        l = l.rstrip('\n').split()
        who = l[0]
        if l[2] == 'gain':
            h = int(l[3])
        else:
            h = - int(l[3])
        next_to = l[10][: -1]
        out[(who, next_to)] = h
        people.add(who)
    return out, people


def day_13_pt1():
    l, people = day13_parse()
    return day13_common(l, people)


def day_13_pt2():
    l, people = day13_parse()
    people.add('42')
    return day13_common(l, people)


def day13_common(l, people):
    permute_people = permutations(people)
    totals = []
    for p in permute_people:
        happiness = []
        for idx in range(len(p)):
            if idx == len(p) - 1:
                pair = [p[-1], p[0]]
            else:
                pair = [p[idx],  p[idx + 1]]
            rpair = (pair[-1], pair[0])
            pair = tuple(pair)
            if '42' in pair:
                h = 0
            else:
                h = l[pair] + l[rpair]
            happiness.append(h)
        totals.append(sum(happiness))
    return max(totals)
