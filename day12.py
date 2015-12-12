def day12_split():
    with open('day12.txt', 'r') as f:
        lines = f.read()
    return lines

def day12():
    a = day12_split()

    l = ''
    for idx in range(len(a)):
        x = a[idx]
        if x.isdigit():
            l += x
        elif x == '-' and a[idx + 1].isdigit():
            l += '-'
        else:
            l += ' '
    ln = l.split()
    return sum([int(x)for x in ln])
