from collections import defaultdict, namedtuple
from functools import lru_cache


class Hdefaultdict(defaultdict):
    def __hash__(self):
        return hash(frozenset(self.items()))


def day7_split():
    with open('day7.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day7_common():
    node = namedtuple('node', ('left_parent', 'right_parent', 'operator'))
    input_lines = day7_split()
    lines = [x.split(' ') for x in input_lines]
    result = Hdefaultdict(bool)
    for l in lines:
        end_val = l[-1].rstrip('\n')
        if len(l) == 3:
            data = node(l[0], None, None)
        elif len(l) == 4:
            data = node(l[1], None, 'NOT')
        elif len(l) == 5:
            data = node(l[0], l[2], l[1])
        else:
            print('oh snap')
            return False
        result[end_val] = data
    return result


def day7_pt1(wire):
    circuit = day7_common()
    return find_value(wire, circuit)


def day7_pt2(wire):
    circuit = day7_common()
    pt1 = day7_pt1(wire)
    circuit['b'] = pt1
    return find_value(wire, circuit)


@lru_cache(maxsize=None, typed=True)
def find_value(wire, circuit):
    try:
        circuit[wire] = int(wire)
        return circuit[wire]
    except ValueError:
        pass
    node = circuit[wire]
    if isinstance(node, int):
        return node
    if node.right_parent is None and node.operator is None:
        try:
            return int(node.left_parent)
        except ValueError:
            return find_value(node.left_parent, circuit)
    elif node.operator == 'NOT':
        return 65535 - find_value(node.left_parent, circuit)
    else:
        return run_op(find_value(node.left_parent, circuit), node.operator, find_value(node.right_parent, circuit))


def run_op(a, o, b):
    if o == 'AND':
        return a & b
    if o == 'OR':
        return a | b
    if o == 'RSHIFT':
        return a >> b
    if o == 'LSHIFT':
        return a << b
