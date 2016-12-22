from collections import OrderedDict, namedtuple

def day22_split():
    with open('day22.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day22():
    data = day22_split()
    data = parse(data)
    print(data)
    pair = []
    for ak, av in data.items():
        for bk, bv in data.items():
            if ak == bk:
                continue
            elif av.Used == 0:
                continue
            elif av.Used >= bv.Avail:
                continue
            else:
                pair += [(ak, bk)]
    return len(pair)





def parse(data):
    nodes = OrderedDict()
    Node = namedtuple('Node', ("Size",  "Used",  "Avail",  "Use"))

    data = data [2:]  # Remove the first two lines.
    for entry in data:
        e = entry.split()
        c = e[0].split("-")
        coords = (c[1][1:], c[2][1:])
        size = int(e[1][:-1])
        used = int(e[2][:-1])
        avail = int(e[3][:-1])
        use = int(e[4][:-1])
        n = Node(size, used, avail, use)
        nodes[coords] = n
    return nodes