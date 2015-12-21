from collections import defaultdict
import re
from itertools import chain


def day19_split():
    with open('day19.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day19_parse():
    lines = day19_split()
    mapping = defaultdict(list)
    s_map = {}
    s_idx = 0

    for l in lines:
        s = l.split()
        if len(s) == 3:
            k = s[0]
            v = s[2]
            if k not in s_map:
                s_map[k] = s_idx
                s_idx += 1
            mapping[k] += [v]
    to_replace = lines[-1]
    out_counts = {}
    for k, v in s_map.items():
        out_counts[v] = to_replace.count(k)

    out_positions = defaultdict(list)
    for k, v in s_map.items():
        out_positions[k] = [i for i in range(len(to_replace)) if to_replace.startswith(k, i)]

    return out_counts, out_positions, to_replace, mapping


def split_elements(s):
    return [x for x in re.split("([A-Z][^A-Z]*)", s) if x]


def day19_pt1():
    out_counts, out_positions, start_molecule, mapping = day19_parse()
    replacements = set()

    for k, v in out_positions.items():
        for spot in v:
            for x in mapping[k]:
                start = start_molecule[0 : spot]
                end = start_molecule[spot + len(k) :]
                s = start + x + end
                replacements.add(s)
    return len(replacements)


def day19_pt2():
    out_counts, out_positions, target_molecule, mapping = day19_parse()

    """
    I tried and tried to come up with a programming solution, and decided to try to math my way out of the problem.
    I noted that Rn and Ar always occurred on the LHS and never on the RHS. As well, Y always appears in between
        Rn and Ar, and it always appears in between another symbol and Rn and Ar.
    Rn and Ar are always paired, so I decided to treat them as ( and ), with Y being +. This means I have s(s) or
        s(s+s) or s(s+s+s) as the possibilities. This means that () will require 0 steps to replace, because they
        never show up on the RHS. So we find the total number of elements (symbols) and subtract the number or Rn and Ar
        from that.
    Next, things with + (Y) in them reduce like s+s to just s, so each + replacement lowers the total by 2x the number of Ys.
    So equation is: # symbols - # Rn's - # of Ar's - 2 * # of Ys = steps.
    I put this in, and it was too high. ): The math seems good, so I subtracted -1 and got the correct answer, because
        experience suggests it was an off-by-one error.
    I wish I knew why I'd made the error, and I'll update this when I figure it out.
    """

    target_molecule = split_elements(target_molecule)
    symbol_count = len(target_molecule)
    count_rn_ar = target_molecule.count('Rn') + target_molecule.count('Ar')
    count_y = target_molecule.count('Y')
    res = symbol_count - count_rn_ar - 2 * count_y - 1
    s = str(symbol_count) + " - " + str(count_rn_ar) + " - " + str(2 * count_y) + " - 1 = "
    print(s)
    print(res)
    return res
