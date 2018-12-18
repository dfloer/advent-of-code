from collections import Counter


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
    for minute in range(10):
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
    return total_trees * total_yards





if __name__ == "__main__":
    print(f"Solution to day 18 part 1: {day18()}")
