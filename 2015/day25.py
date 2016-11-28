def day25(row, column, initial_value, mult, div):
    total_numbers = int(((row + column - 2) * (row + column - 1)) / 2 + column - 1)
    # We need to use modular exponentiation for this: https://en.wikipedia.org/wiki/Modular_exponentiation
    value = initial_value * pow(mult, total_numbers, div) % div
    return value
