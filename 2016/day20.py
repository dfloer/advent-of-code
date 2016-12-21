def day20_split():
    with open('day20.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day20():
    data = [[int(y) for y in x.split('-')] for x in day20_split()]
    total_ips = 2 ** 32
    data.sort()
    idx = 0
    ip = 0
    while ip < total_ips:
        start, end = data[idx]
        if ip >= start:
            if ip <= end:
                ip = end + 1
                continue
            idx += 1
        else:
            return ip
