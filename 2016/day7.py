import regex as re
from collections import Counter, defaultdict


def day7_split():
    with open('day7.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day7_part1():
    data = day7_split()
    count = 0
    for x in data:
        split = re.split(r"\[(.*?)\]", x)
        inner_count = 0
        for idx in range(len(split)):
            to_check = split[idx]
            res = re.search(r"(.)(.)\2\1", to_check)
            if res:
                # Input always has the form or alternating non-square and square brackets, with non last.
                if idx % 2 == 0:  # Even numbered one, outside square brackets.
                    repeated = Counter(res.group()).most_common()  # looks for repeats of the form 'aaaa'
                    if len(repeated) == 1:  # If we do find a repeat, this address isn't valid
                        continue
                    inner_count = 1
                if idx % 2 == 1:  # Odd numbered one, inside square brackets.
                    repeated = Counter(res.group()).most_common()  # looks for repeats of the form 'aaaa'
                    if len(repeated) != 1:  # If we have a result and it isn't a repeat, this address isn't valid.
                        inner_count = 0
                        break
        count += inner_count
    return count


def day7_part2():
    data = day7_split()
    count = []
    for x in data:
        split = re.split(r"\[(.*?)\]", x)
        indexes = defaultdict(list)
        for idx in range(len(split)):
            to_check = split[idx]
            res = re.findall(r"(.)(.)\1", to_check, overlapped=True)  # (.)(.)(\1) returns 2 items
            if res:
                # Builds up a dictionary if {('a', 'b'): [1]} pairs. The value is the chunk index(es) where the words are.
                for candidate in res:
                    indexes[candidate] += [idx]
        count += [check_valid(indexes)]
    return sum(count)


def check_valid(indexes):
    """
    Checks to see whether or not the string s is valid in the given indexes.
    """
    # Check if any substrings has any versions that are the opposite of it anywhere in that line.
    valid = False
    for k, v in indexes.items():
        swapped = k[::-1]
        other = indexes.get(swapped)
        # Check to see if the swapped version exists in the dictionary.
        if other:
            # 'aaa' case, these are invalid matches, don't bother checking further.
            if k == swapped:
                continue
            # single occurence case
            if len(v) == 1 and len(other) == 1:
                # Case where both occur inside or outsid brackets.
                if (int(v[0]) % 2) == (int(other[0]) % 2):
                    continue
                else:
                    valid = True
            else:
                # Use sets to eliminate duplicates in the same chunk.
                v_s = set(v)
                other_s = set(other)
                # If the two sets are the same, then this is invalid.
                if v_s == other_s:
                    continue
                possible_combinations = [(x % 2, y % 2) for x in v_s for y in other_s]
                # For a pairing to be valid, one part needs to be in an even chunk and the other in an odd ([]) chunk.
                if (1, 0) in possible_combinations or (0, 1) in possible_combinations:
                    valid = True
    return valid
