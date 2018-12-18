from collections import Counter
from operator import mul


def day18_split():
    with open('day18.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day18_split()
    board = {}
    for y in range(50):
        for x in range(50):
            board[(x, y)] = lines[x][y]
    return board


def count_neighbours(x, y, board):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    res = []
    for d in directions:
        try:
            k = (x + d[0], y + d[1])
            e = board[k]
            res += [e]
        except KeyError:
            pass
    return Counter(res)


def day18():
    board = parse()
    totals = {}
    for minute in range(500):
        old_board = {k: v for k, v in board.items()}
        for a in range(50):
            for b in range(50):
                e = old_board[(a, b)]
                neighbours_count = count_neighbours(a, b, old_board)
                if e == '.':
                    if neighbours_count['|'] >= 3:
                        board[(a, b)] = '|'
                elif e == '|':
                    if neighbours_count['#'] >= 3:
                        board[(a, b)] = '#'
                elif e == '#':
                    if neighbours_count['|'] >= 1 and neighbours_count['#'] >= 1:
                        board[(a, b)] = '#'
                    else:
                        board[(a, b)] = '.'
        total_trees = len([x for x in board.values() if x == '|'])
        total_yards = len([x for x in board.values() if x == '#'])
        totals[minute] = [total_trees, total_yards]

    p = {}
    repeat = []
    for i in range(1, len(totals)):
        l = totals[i - 1]
        t = totals[i]
        x = l[0] * t[0] - l[1] * t[1]
        if x in p:
            v = sum([mul(*totals[a]) for a in range(p[x], i)])
            repeat = [i, p[x], v]
            break
        p[x] = i
    period = repeat[0] - repeat[1]
    off = (1000000000 % period) + repeat[0]

    pt1 = mul(*totals[9])
    pt2 = mul(*totals[off - 1])
    return pt1, pt2


if __name__ == "__main__":
    pt1, pt2 = day18()
    print(f"Solution to day 18 part 1: {pt1}")
    print(f"Solution to day 18 part 1: {pt2}")
