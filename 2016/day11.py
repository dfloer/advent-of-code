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
    # We want to move everything from floor 1 up to 2, then everything on 2 up to 3 and finally all on 3 to 4.
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


def day11_math():
    """
    I spotted a pattern in the example as I reread it for the nth time after not being able to figure out a good algo.
    The greedy algo I was working on above, going:
        First try to move two things up one floor.
        If that doesn't work, try to bring one up.
        If that doesn't work, bring one down.
        If that doesn't work, bring two down and cry.
        Shit? How'd we get here? Abort! (Backtrack)
    Would move everything up, one floor at a time.
    I could see a pattern for moves, so I worked out how many moves were needed to move 1..10 objects up one floor.
    For one object, I can bring it up in one move. For two objects, also only one move.
    3 objects takes 3 moves, 4 is 4 moves, 5 is 7 moves, 6 is 9, 7 is 11, 8 is 13, 9 is 15, 10 is 17. Definite pattern.
    So I tried to find a sequence that mathed using W|a, didn't quite get one but found one that worked except for n=1 and n=2.
    These were a bit of special cases, so I handled them alone.
    Repeat the the # of objects on each floor until they're at the top.
    formula for n>=3 is 2n-3
    Note: This doesn't work for all cases. The commented out case is broken.
    """
    floors_pt1 = [4, 5, 1, 0]
    # floors_pt1 = [2, 4, 4, 0]
    pt1_ans = 0
    floors_pt2 = [8, 5, 1, 0]
    # floors_pt2 = [6, 4, 4, 0]
    pt2_ans = 0
    idx = 0
    while True:
        if idx == 3:
            break
        n = floors_pt1[idx]
        m = floors_pt2[idx]
        pt1_ans += moves_to_next(n)
        pt2_ans += moves_to_next(m)
        floors_pt1[idx + 1] += n
        floors_pt2[idx + 1] += m
        idx += 1
    return pt1_ans, pt2_ans


def moves_to_next(n):
    # How many moves to take the n items on one floor up one floor?
    if n in (1, 2):
        return 1
    else:
        return 2 * n - 3
