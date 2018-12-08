def day8_split():
    with open('day8.txt', 'r') as f:
        data = [int(x) for x in f.read().split()]
    return data


def parse_node(node_data):
    metadata = []
    child_count, metadata_count = node_data[ : 2]
    node_data = node_data[2 : ]
    for _ in range(child_count):
        x, node_data = parse_node(node_data)
        metadata += x
    metadata += node_data[ : metadata_count]
    return metadata, node_data[metadata_count : ]


def day8_parse():
    raw = day8_split()
    res = parse_node(raw)
    return res


def day8():
    data = day8_parse()
    return sum([item for sublist in data for item in sublist])


if __name__ == "__main__":
    print(f"Solution to day 8 part 1: {day8()}")
    #print(f"Solution to day 8 part 2: {day8_part2()}")