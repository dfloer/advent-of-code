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


def day7_part1():
    lines = parse_input()
    all_steps = set([item for sublist in lines for item in sublist])

    step_ordering = ''
    while all_steps:
        candidates = list(set([x[0] for x in lines]) - set([x[1] for x in lines]))
        # Special handling for the end/last item.
        if candidates == []:
            candidates = list(all_steps)
        candidates.sort()
        next_step = candidates[0]
        step_ordering += next_step
        all_steps.remove(next_step)
        lines = [(a, b) for a, b in lines if a != next_step]

    return step_ordering


def day7_part2(step_duration=60, num_workers=5):
    lines = parse_input()
    all_steps = set([item for sublist in lines for item in sublist])
    elves = [0 for _ in range(num_workers)]
    current_work = [None for _ in elves]

    time_spent = 0
    while all_steps or sum(elves) > 0:
        done = [x[1] for x in lines]
        candidates = [s for s in all_steps if s not in done]
        for x in range(num_workers):
            elves[x] = max(elves[x] - 1, 0)
            if elves[x] == 0:
                e = current_work[x]
                if e is not None:
                    lines = [(a, b) for a, b in lines if a != e]
                if candidates:
                    next_step = candidates.pop(0)
                    elves[x] = step_duration + ord(next_step) - ord('A')
                    current_work[x] = next_step
                    all_steps.remove(next_step)
        time_spent += 1
    return time_spent


if __name__ == "__main__":
    print(f"Solution to day 7 part 1: {day7_part1()}")
    print(f"Solution to day 7 part 2: {day7_part2()}")
