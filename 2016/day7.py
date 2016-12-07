import re
from collections import Counter


def day7_split():
    with open('day7.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day7():
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
                    if len(repeated) != 1:  # If we have a result and it isn't a repeat, this address isn't valie.
                        inner_count = 0
                        break
        count += inner_count
    return count
