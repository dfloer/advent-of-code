def day19(elves):
    # Part1 appears to be the Josephus problem: https://en.wikipedia.org/wiki/Josephus_problem
    # The algorithm is given on that article, in the "Solution" section, translated from Java.
    l = elves - highest_one_bit(elves)
    pt1 = 2 * l + 1

    """
    For part 2 I did the first 10 iterations until I spotted a pattern. The pattern looks like:
    1:1 (1=3^0)
    2:1, 3:3 (3=3^1)
    4:1, 5:2, 6:3, 7:5, 8:7, 9:9 (9=3^2)
    10:1, 11:2. 12:3, 13:4, 14:5, 15:6, 16:7, 17:8 18:9, 19:11, 20:13, ..., 25:23, 26:25, 27:27.
    28:1, 29:2, 30:3, ..., 52:25, 53:27, 54:27, 55:19, 56:31, ..., 79:77, 80:79, 81:81.
    82:1 ..., 3^5:3^5 (3^5=243).
    etc...
    I speculated that this pattern held then worked out a mathematical solution to produce it.
    The algorithm finds the largest power of 3 that is less than the number of elves.
    Then finds the difference between it and the power of 3 closest but lower than it,
        noticing that they increase 1x after then until the next power of 3.
    Note: This doesn't appear to work for all inputs. ):
    """
    i = 1
    x = 0
    while True:
        a = (3 ** i)
        if a > elves:
            break
        x = a
        i += 1
    pt2 = elves - x

    # If the given number of elves is a power of 3, return that power of 3.
    if elves == x:
        pt2_better = elves
    else:
        # Fudge is needed because the previous solution seems to miscount. Determined via trial-and-error.
        # I need the fudge amount only if it's +'ve.
        fudge = max(0, elves - 2 * x)
        pt2_better = elves - x + fudge
    return "Part1: {}, Part2: {}, Broken Part2: {}".format(pt1, pt2_better, pt2)


def highest_one_bit(n):
    # Finds the value of the highest 1 bit in a number by exploiting the behaviour that a bin() call doesn't pad with 0s.
    return 2 ** (len(bin(n)[2:]) - 1)
