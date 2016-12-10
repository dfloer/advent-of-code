from collections import defaultdict


def day10_split():
    with open('day10.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day10(chip_a=61, chip_b=17):
    data = day10_split()
    bots = defaultdict(list)
    output = defaultdict(list)
    res = 0
    for x in data:
        split = x.split()
        print(bots)
        if split[0] == "value":
            print(split)
            val = int(split[1])
            dest = int(split[-1])
            print(val, dest)
            bots[dest] += [val]
        else:
            print(split)
            source = int(split[1])
            hi_out = False
            lo_out = False
            low_dest = int(split[6])
            high_dest = int(split[-1])
            if split[5] == "output":
                lo_out = True
            if split[-2] == "output":
                hi_out = True
            print(source, lo_out, low_dest, hi_out, high_dest)
            source_bot = bots[source]
            print(source_bot)
            if len(source_bot) == 2:
                lo, hi = sorted(source_bot)
                if lo == min(chip_a, chip_b) and hi == max(chip_a, chip_b):
                    res = source_bot
                bots[source] = []
                if not lo_out:
                    bots[low_dest] = lo
                else:
                    output[low_dest] = lo
                if not hi_out:
                    bots[high_dest] = hi
                else:
                    output[high_dest] = hi
            else:
                print("Skipped")
    return res

