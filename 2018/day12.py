def day12_split():
    with open('day12.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse():
    lines = day12_split()
    initial_state = lines[0][15 : ]
    rules = {}
    for x in range(2, len(lines)):
        l = lines[x]
        b = l[-1]
        a = l[0 : 5]
        rules[a] = b
    return initial_state, rules


def day12(generations=20):
    initial_state, rules = parse()
    middle = 500
    plant_pots = ['.' for _ in range(2 * middle + len(initial_state))]
    for idx, x in enumerate(initial_state):
        plant_pots[middle + idx] = x
    results = {}
    for g in range(generations):
        previous = plant_pots
        for x in range(2, len(plant_pots) - 5):
            c = ''.join(previous[x - 2 : x + 3])
            r = [rules[c]]
            plant_pots = plant_pots[ : x] + r + previous[x + 1:]
        results[g] = [i - middle for i, x in enumerate(plant_pots) if x == "#"]

    return sum(results[19])


if __name__ == "__main__":
    print(f"Solution to day 12 part 1: {day12()}")
    # print(f"Solution to day 12 part 2: {day12()}")
