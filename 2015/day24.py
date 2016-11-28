from itertools import combinations
from functools import reduce
from operator import mul

def day24_split():
    with open('day24.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day24(containers=3):
    package_weights = [int(x) for x in day24_split()]
    total_weight = sum(package_weights) / containers

    # Find the smallest subset that gives the correct total_weight.
    # Note that this assumes that the other two will balance exactly in half, but that isn't necessarily the case.
    for x in range(1, len(package_weights)):
        possible_combos = list(combinations(package_weights, x))
        candidates = [x for x in possible_combos if sum(x) == total_weight]
        if len(candidates) > 0:  # That actually has values in it...
            break
    # Now find the lightest of all of the possible candidates.
    lightest = min(candidates, key=lambda x: sum(x))
    # And finally calculate the quantum entanglement.
    qe = reduce(mul, lightest)
    return qe


