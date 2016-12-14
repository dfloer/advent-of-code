from hashlib import md5
from collections import OrderedDict


def day14(inp="ahsbgdzn", stretch=1):
    idx = 0
    good_candidates = OrderedDict()
    keys = OrderedDict()

    while True:
        h = md5()
        to_hash = inp + str(idx)
        h.update(to_hash.encode('utf-8'))
        to_hash = h.hexdigest()
        candidate = repeat_hash(to_hash, stretch)
        if find_rep(candidate, 3):
            good_candidates[idx] = find_rep(candidate, 3)
        if find_rep(candidate, 5):
            a = find_rep(candidate, 5)
            for x in range(idx - 999, idx):
                try:
                    c = good_candidates[x]
                except KeyError:
                    c = False
                if c == a:
                    keys[x] = a
        if len(keys) > 64:
            test = []
            for idx, d in enumerate(keys):
                test += [d]
            for x, i in enumerate(sorted(test)):
                if x == 63:
                    return i
        idx += 1


def repeat_hash(to_hash, repeat=1):
    # We need to repeat is once more for the last iteration.
    for idx in range(repeat):
        h = md5()
        h.update(to_hash.encode('utf-8'))
        to_hash = h.hexdigest()
    return to_hash


def find_rep(s, n=3):
    # Find if we have n repeated characters.
    for x in range(0, len(s)):
        y = s[x : x + n]
        if len(set(y)) == 1 and len(y) == n:
            return str(y[0])
    return None
