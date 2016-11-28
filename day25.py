def day25(row, column, initial_value, mult, div):
    total_numbers = int(((row + column - 2) * (row + column - 1)) / 2 + column - 1)
    print(row, column, total_numbers, mult, div)
    value = initial_value
    # I feel like there's a simple mathematical answer to this.
    for x in range(total_numbers):
        value = (value * mult) % div
    print(value)


