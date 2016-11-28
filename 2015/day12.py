import json


def day12_split():
    with open('day12.txt', 'r') as f:
        lines = f.read()
    return lines


def day12_pt1():
    a = day12_split()
    return day12_count(a)


def day12_count(a):
    l = ''
    for idx in range(len(a)):
        x = a[idx]
        if x.isdigit():
            l += x
        elif x == '-' and a[idx + 1].isdigit():
            l += '-'
        else:
            l += ' '
    ln = l.split()
    return sum([int(x)for x in ln])


def day12_pt2():
    a = day12_split()
    j = json.loads(a)
    x = day12_pt2_parse(j)
    js = json.dumps(x)
    return day12_count(js)


def day12_pt2_parse(obj):
    if isinstance(obj, list):
        return [day12_pt2_parse(x) for x in obj]
    elif isinstance(obj, dict):
        if 'red' in obj.values():
            return dict()
        else:
            return {k: day12_pt2_parse(v) for k, v in obj.items()}
    else:
        return obj
