import collections
from itertools import groupby


def day5_split():
    with open('day5.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day5():
    words = day5_split()
    nice = [is_nice(x) for x in words]
    return nice.count(True)


def is_nice(word):
    vowel = False
    dupes = False

    bad_strings = any(x in word for x in ['ab', 'cd', 'pq', 'xy'])

    duplicates = collections.defaultdict(int)
    for x in word:
        if x in ['a', 'e', 'i', 'o', 'u']:
            duplicates[x] += 1
    if sum(duplicates.values()) >= 3:
        vowel = True

    for _, x in groupby(word):
        if len(list(x)) > 1:
            dupes = True

    if [bad_strings, vowel, dupes] == [False, True, True]:
        return True
    else:
        return False
