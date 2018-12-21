import networkx
from copy import deepcopy


def day20_split():
    with open('day20.txt', 'r') as f:
        line = f.read()
    return line


def parse():
    input_regex = day20_split()
    just_input = input_regex[1 : -1]  # Remove the ^ and $ as we don't need them.
    rooms = networkx.Graph()  # Decided to try this out because my graph thing had a hard-to-find bug. I'm not sure if it ended up being any faster...
    positions = set()
    positions.add(0)
    parens = []
    starts = set()
    starts.add(0)
    ends = set()
    dir_map = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}  # Using the same complex notation for direction as used previously.
    for idx, c in enumerate(just_input):
        if c == "(":
            parens += [(starts, ends)]
            starts = positions
            ends = set()
        elif c == ")":
            positions.update(ends)
            starts, ends = parens.pop()
        elif c == "|":
            ends.update(positions)
            positions = starts
        elif c in ('N', 'E', 'W', 'S'):
            direction = dir_map[c]
            rooms.add_edges_from([(x, x + direction) for x in positions])
            new_positions = [x + direction for x in positions]
            positions = set()
            for x in new_positions:
                positions.add(x)
    return rooms


def day20():
    paths = parse()
    lens = networkx.algorithms.shortest_path_length(paths, 0)
    return max(lens.values())


if __name__ == "__main__":
    print(f"Solution to day 20 part 1: {day20()}")
    # print(f"Solution to day 20 part 2: {day20()}")
