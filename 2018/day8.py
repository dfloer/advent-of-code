def day8_split():
    with open('day8.txt', 'r') as f:
        data = [int(x) for x in f.read().split()]
    return data


def parse_node(node_data):
    metadata = []
    metadata_values = []
    child_count, metadata_count = node_data[ : 2]
    node_data = node_data[2 : ]
    for _ in range(child_count):
        x, node_data, values = parse_node(node_data)
        metadata += x
        metadata_values += [values]
    new_metadata = node_data[ : metadata_count]
    metadata += new_metadata

    # Find the value of the node.
    if child_count == 0:
        node_value = new_metadata
    else:
        n = []
        for x in new_metadata:
            # Check and see if the node references makes sense, otherwise don't bother.
            if 0 < x <= len(metadata_values):
                n += metadata_values[x - 1]
        node_value = n
    return metadata, node_data[metadata_count : ], node_value


def day8_parse():
    raw = day8_split()
    res = parse_node(raw)
    return res


def day8():
    part1, _, part2 = day8_parse()
    return sum(part1), sum(part2)


if __name__ == "__main__":
    pt1, pt2 = day8()
    print(f"Solution to day 8 part 1: {pt1}")
    print(f"Solution to day 8 part 2: {pt2}")
