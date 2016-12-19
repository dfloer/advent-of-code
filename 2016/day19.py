def day19(elves):
    # Part1 appears to be the Josephus problem: https://en.wikipedia.org/wiki/Josephus_problem
    # The algorithm is given on that article, in the "Solution" section, translated from Java.
    l = elves - highest_one_bit(elves)
    pt1 = 2 * l + 1

    """
    For part 2 I did the first 10 iterations until I spotted a pattern. The pattern looks like:
    1 (1=3^0)
    1,2,3 (3=3^1)
    1,2,3,5,7,9 (9=3^2)
    1
    I speculated that this pattern held then worked out a mathematical solution to produce it.
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
    # 1410968 high, 1594323 high
    return pt1, pt2


def highest_one_bit(n):
    # Finds the value of the highest 1 bit in a number by exploiting the behaviour that a bin() call doesn't pad with 0s.
    return 2 ** (len(bin(n)[2:]) - 1)
