from itertools import chain
from math import sqrt

def day20(target):
    idx = 0
    while True:
        factors = find_factors(idx)
        if sum(factors) * 10 >= target:
            return idx
        idx += 1


def find_factors(n):
    """
    Returns the facrtors of n.
    """
    factors = set(chain.from_iterable((i, n // i) for i in range(1, int(sqrt(n)) + 1) if n % i == 0))
    return factors