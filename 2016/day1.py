def day1_split():
    with open('day1.txt', 'r') as f:
        lines = f.read().split(', ')
    return lines


def day1():
    lines = day1_split()
    loc = [0, 0]
    direction = 0
    for i in lines:
        turn = i[0 : 1]
        amount = int(i[1 :])

        if turn == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4


        if direction == 0:
            loc[0] += amount
        elif direction == 2:
            loc[0] -= amount
        elif direction == 1:
            loc[1] += amount
        else:
            loc[1] -= amount

    print(abs(loc[0]) + abs(loc[1]))

