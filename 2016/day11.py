from random import randint
from copy import deepcopy

def day11_split():
    with open('day11.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


prefixes = "SPTRC"
chips = [''.join([x, 'M']) for x in prefixes]
gens = [''.join([x, 'G']) for x in prefixes]


def day11():
    #data = day11_split()
    #print(data)

    floors = [["SG", "SM", "PG", "PM"], ["TG", "RG", "RM", "CG", "CM"], ["TM"], []]
    elev = 0
    elev_cap = 2
    moves = 0
    print(check_valid(floors))
    while True:
        prev_state = deepcopy(floors)
        c = None
        # First try to move two things up one floor.
        for f in floors:
            c = find_safe_candidates(f)
            if c != []:
                pass

        if c == []:
            pass
        # If that doesn't work, try to bring one up.

        # If that doesn't work, bring one down.

        # If that doesn't work, bring two down and cry.

        # Shit? How'd we get here? Abort! (Backtrack)



def find_safe_candidates(floor):
    # Finds all two item pairs that can travel on an elevator together. False if there isn't anything on this floor.
    items = []
    for f in floor:
        if f[-1] == "M" and (f[0] + "G" in f):
            items += [[f.index(f), f.index(f[0] + "G")]]
        elif f[-1] == "G" and (f[0] + "M" in f):
            items += [[f.index(f), f.index(f[0] + "M")]]
        return items




def check_valid(end_state):
    # Check and see if any chips are with other generators but not their own.
    for f in end_state:
        for e in f:
            if e[-1] == "M" and (e[0] + "G" not in f):  # Chip but not its generator.
                if any(x in gens for x in f):  # Check and see if there are any generators on this floor.
                    return False
    return True
