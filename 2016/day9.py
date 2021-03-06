def day9_split():
    with open('day9.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day9_part1():
    data = day9_split()[0]
    offset = 0
    output = ''
    while True:
        try:
            c = data[offset]
        except IndexError:
            break
        if c == '(':  # We're looking at a block to offset.
            end = offset + 1
            while data[end] != ')':
                end += 1
            end += 1
            marker = data[offset + 1 : end - 1]
            length, reps = marker.split('x')
            block = data[end : end + int(length)]
            additional = block * int(reps)
            output += additional
            offset += len(block) + len(marker) + 2
        else:  # normal characters that aren't compressed, add as normal.
            output += c
            offset += 1
    return len(output)


def day9_part2():
    data = day9_split()[0]
    return day9_part2_inner(data)


def day9_part2_inner(data):
    offset = 0
    output = 0
    while True:
        try:
            c = data[offset]
        except IndexError:
            break
        if c == '(':  # We're looking at a block to offset.
            end = offset + 1
            while data[end] != ')':
                end += 1
            end += 1
            marker = data[offset + 1 : end - 1]
            length, reps = marker.split('x')
            block = data[end : end + int(length)]
            additional = day9_part2_inner(block) * int(reps)
            output += additional
            offset += len(block) + len(marker) + 2
        else:  # normal characters that aren't compressed, add as normal.
            output += 1
            offset += 1
    return output
