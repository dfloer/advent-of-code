from collections import defaultdict


def day10_split():
    with open('day10.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day10(chip_a=61, chip_b=17):
    data = day10_split()
    bots = defaultdict(list)
    output = defaultdict(list)
    res = None
    new_data = []
    for x in data:
        split = x.split()
        if split[0] == "value":
            val = int(split[1])
            dest = int(split[-1])
            bots[dest] += [val]
        else:
            new_data += [x]

    while len(new_data) > 0:
        newer_data = []
        for x in new_data:
            split = x.split()
            source = int(split[1])
            hi_out = False
            lo_out = False
            low_dest = int(split[6])
            high_dest = int(split[-1])
            if split[5] == "output":
                lo_out = True
            if split[-2] == "output":
                hi_out = True
            source_bot = bots[source]
            if len(source_bot) == 2:
                lo, hi = sorted(source_bot)
                if lo == min(chip_a, chip_b) and hi == max(chip_a, chip_b):
                    res = source
                bots[source] = []
                if not lo_out:
                    bots[low_dest] += [lo]
                else:
                    output[low_dest] += [lo]
                if not hi_out:
                    bots[high_dest] += [hi]
                else:
                    output[high_dest] += [hi]
            else:
                newer_data += [x]
        new_data = newer_data
    return res, output[0][0] * output[1][0] * output[2][0]

