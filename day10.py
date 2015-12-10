import itertools


def day10(number, i):
    for idx in range(i):
        number = string_group(number)
    return len(number)


def string_group(s):
    return ''.join(str(len(list(y))) + x for x, y in itertools.groupby(s))
