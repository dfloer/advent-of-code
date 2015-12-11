from itertools import groupby
from numpy import base_repr

letters = list('abcdefghijklmnopqrstuvwxyz')
base26 = list('0123456789abcdefghijklmnop')

three_letters = [''.join(letters[x: x + 3]) for x in range(len(letters) - 2)]


def day11_split():
    with open('day11.txt', 'r') as f:
        lines = f.readlines()
    return lines

def day11(p):
    valid = False
    while not valid:
        p = inc_string(p)
        valid = check_valid(p)
    return p


def check_valid(p):
    three = [p[x: x+3] for x in range(6)]
    if not any(x in three for x in three_letters):
        return False
    if any(x in 'iol' for x in p):
        return False
    groups = [1 for _, x in groupby(p) if len(list(x)) > 1]
    if len(groups) < 2:
        return False
    return True


def inc_string(s):
    ns = [base26[ord(y) - 97] for y in s]
    sn = ''.join(ns)
    i = int(sn, 26) + 1
    isn = base_repr(i, 26).lower()
    ins = [letters[base26.index(y)] for y in isn]
    pw = ''.join(ins)
    return pw
