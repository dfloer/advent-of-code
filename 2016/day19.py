def day19(elves):
    # Part1 appears to be the Josephus problem: https://en.wikipedia.org/wiki/Josephus_problem
    # The algorithm is given on that page.
    l = elves - highest_one_bit(elves)
    return 2 * l + 1


def highest_one_bit(n):
    # Finds the value of the highest 1 bit in a number by exploiting the behaviour that a bin() call doesn't pad with 0s.
    return 2 ** (len(bin(n)[2:]) - 1)
