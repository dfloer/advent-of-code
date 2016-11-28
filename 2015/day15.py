from functools import reduce
import operator


def day15_split():
    with open('day15.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day15_parse():
    lines = day15_split()
    l = [x.rstrip('\n').split(' ') for x in lines]
    d = {}
    for e in l:
        d[e[0]] = [int(e[2].strip(',')), int(e[4].strip(',')), int(e[6].strip(',')), int(e[8].strip(',')), int(e[10].strip(','))]
    return d


def day15_pt1():
    x = day15_parse()
    d = {k: v[:-1] for k, v in x.items()}
    return knapsack(d, 100, None)


def day15_pt2():
    d = day15_parse()
    return knapsack(d, 100, 500)


def f(n, s):
    if n == 1:
        yield (s,)
    else:
        for i in range(s + 1):
            for j in f(n - 1, s - i):
                yield (i,) + j


def knapsack(d, total=100, calories=None):
    all_orderings = list(f(len(d), total))
    results = []
    properties = list(d.values())
    for order in all_orderings:
        # Generates a list of the total amount of each property for each ingredient.
        total_ingredients = [[count * total_property for total_property in amounts] for count, amounts in zip(order, properties)]
        # Adds the properties together across all of the ingredients
        total_amounts = [max(sum(prop), 0) for prop in zip(*total_ingredients)]
        if calories is not None and total_amounts[-1] != calories:
            results.append(0)
        elif calories is None:
            results.append(reduce(operator.mul, total_amounts, 1))
        else:
            results.append(reduce(operator.mul, total_amounts[:-1], 1))
    m = max(results)
    i = results.index(m)
    return m, all_orderings[i]
