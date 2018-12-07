def day7_split():
    with open('day7.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_input():
    res = []
    for x in day7_split():
        e = x.split(' ')
        res += [(e[1], e[7])]
    return res


def day7():
    lines = parse_input()
    all_steps = set([item for sublist in lines for item in sublist])

    step_ordering = ''
    while all_steps:
        candidates = list(set([x[0] for x in lines]) - set([x[1] for x in lines]))
        # Special handling for the end/last item.
        if candidates is []:
            candidates = list(all_steps)
        candidates.sort()
        next_step = candidates[0]
        step_ordering += next_step
        all_steps.remove(next_step)
        lines = [(a, b) for a, b in lines if a != next_step]

    return step_ordering


if __name__ == "__main__":
    print(f"Solution to day 7 part 1: {day7()}")
    # print(f"Solution to day 7 part 2: {pt2}")