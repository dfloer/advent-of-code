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
    pt1 = sum(results[generations - 1])

    h = [sum(x) for x in results.values()]
    last = 0
    res = 0
    gens = 50000000000
    # I started printing all the values, and noticed a pattern emerging.
    # After a certain point, each row only goes up by the same value.
    # Start by finding this value.
    for i in range(1, len(h)):
        q = h[i - 1] - h[i]
        if q == last:
            res = i
            break
        last = q
    # Now that I've found where the values converge, I can calculate what I'd have after 50G iterations.
    # The first step is to figure out how many generations will be run after the convergence point.
    more_generations = gens - (res + 1)
    # And multiply this by the value each generation goes up by.
    more_gens_total = more_generations * abs(last)
    # And finally, add the value from the start to it.
    pt2 = more_gens_total + h[res]

    return pt1, pt2


if __name__ == "__main__":
    print(f"Solution to day 12 part 1: {day12()[0]}")
    # Note that 101 was chosen after I had found my answer.
    print(f"Solution to day 12 part 2: {day12(101)[1]}")
