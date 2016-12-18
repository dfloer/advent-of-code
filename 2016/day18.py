def day18_split():
    with open('day18.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day18(row_num=40):
    data = str(day18_split()[0])
    rows = []
    rows += [data]
    for x in range(row_num - 1):
        nr = generate_row(data)
        rows += [nr]
        data = nr
    big_row = ''.join([y for x in rows for y in x])
    return big_row.count('.')


def generate_row(prev):
    traps = ['^^.', '.^^', '^..', '..^']
    l = len(prev)
    p = '.' + str(prev) + '.'  # the non existent spots are safe
    new_row = ''
    for x in range(0, l):
        tri = p[x : x + 3]
        if tri in traps:
            new_row += '^'
        else:
            new_row += '.'
    return new_row
