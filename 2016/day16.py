def day16(inp, disk_len=272):
    a = inp
    while len(a) <= disk_len:
        a = dragon(a)
    data = a[:disk_len]
    xs = data
    while len(xs) % 2 == 0:
        xs = checksum(xs)
    return xs


def dragon(a):
    b = a[:]
    b = b[::-1]
    b = ''.join('1' if x == '0' else '0' for x in b)
    c = a + '0' + b
    return c


def checksum(a):
    s = ''
    for idx in range(0, len(a), 2):
        c = a[idx : idx + 2]
        if len(set(c)) == 1:
            s += '1'
        else:
            s += '0'
    return s
