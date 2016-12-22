from collections import OrderedDict, namedtuple


def day22_split():
    with open('day22.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day22():
    data = day22_split()
    data = parse(data)
    pairs = day22_part1(data)
    pt1 = len(pairs)
    day22_part2(data)
    return "part 1:" + str(pt1)


def day22_part2(data):
    """
    None of this code actually solves part2, I decided to print the data to visualize it and figure out what was happening.
    I noticed that all of the pairs in part1 shared the same node, one that's empty. I treated this like one of those tile sliding puzzles.
    So in order to figure out how many moves were needed, first I needed to get the empty node to the Starting node. From there, I moved the data to the Goal.
    Moves as follows (for my input, general algorithm works for all, I assume):
        22x moves getting the space to the wall.
        3x moves getting the space to the top of the wall.
        3x moves to get the space to the y=0 column from the top of the wall.
        31x moves to get the space one above the start node.
        1x moves to get the goal into the space
        Next came moving the space up, which takes a total of 5 moves.
            4 moves to move the space from below to above (R, U, U, L)
            1 to move the node into the space.
        32x5 moves to finish.
        =220
    """
    print("0 = hole, X = impassible nodes, G = goal node, S = start node\n")
    max_x = max([x for x, y in data.keys() if y == 0])
    max_y = max([y for x, y in data.keys() if x == 0])
    data_start = (max_x, 0)
    data_end = (0, 0)
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            v = data[(x, y)]
            if v.Used == 0:
                print("0", end='')
            elif v.Used > 100:
                print("X", end='')
            elif (x, y) == data_start:
                print("S", end='')
            elif (x, y) == data_end:
                print("G", end='')
            else:
                print(".", end='')
        print()


def day22_part1(data):
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
    return pair



def parse(data):
    nodes = OrderedDict()
    Node = namedtuple('Node', ("Size",  "Used",  "Avail",  "Use"))

    data = data [2:]  # Remove the first two lines.
    for entry in data:
        e = entry.split()
        c = e[0].split("-")
        coords = (int(c[1][1:]), int(c[2][1:]))
        size = int(e[1][:-1])
        used = int(e[2][:-1])
        avail = int(e[3][:-1])
        use = int(e[4][:-1])
        n = Node(size, used, avail, use)
        nodes[coords] = n
    return nodes