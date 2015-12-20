from collections import defaultdict
from functools import reduce


def day19_split():
    with open('day19.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day19_parse():
    lines = day19_split()
    mapping = defaultdict(list)
    s_map = {}
    s_idx = 0
    d_map = {}
    d_idx = 0

    for l in lines:
        s = l.split()
        if len(s) == 3:
            k = s[0]
            v = s[2]
            if k not in s_map:
                s_map[k] = s_idx
                s_idx += 1
            if v not in d_map:
                d_map[v] = d_idx
                d_idx += 1
            mapping[k] += [v]
    to_replace = lines[-1]
    out_counts = {}
    for k, v in s_map.items():
        out_counts[v] = to_replace.count(k)

    out_positions = defaultdict(list)
    for k, v in s_map.items():
        out_positions[k] = [i for i in range(len(to_replace)) if to_replace.startswith(k, i)]

    return s_map, d_map, out_counts, out_positions, to_replace, mapping

def day19():
    s_map, d_map, out_counts, out_positions, start_molecule, mapping = day19_parse()
    replacements = set()

    # print(start_molecule)
    for k, v in out_positions.items():
        for spot in v:
            for x in mapping[k]:
                start = start_molecule[0 : spot]
                end = start_molecule[spot + len(k) :]
                s = start + x + end
                replacements.add(s)
                # print("k:", k, "spot:", spot, "start:", start, "end:", end, "replacement:", x, "out:", s)
    # print(replacements)
    print(len(replacements))