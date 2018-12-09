from collections import deque


def day9_split():
    with open('day9.txt', 'r') as f:
        data = f.read().split()
    return int(data[0]), int(data[6])


def day9(extra=1):
    total_players, last_points = day9_split()
    players = {x : 0 for x in range(total_players)}
    marbles = deque([0])
    for v in range(1, (last_points + 1) * extra):
        player = v % total_players
        if v % 23 == 0:
            players[player] += v
            marbles.rotate(7)
            players[player] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(v)
    return max(players.values())


if __name__ == "__main__":
    print(f"Solution to day 9 part 1: {day9()}")
    print(f"Solution to day 9 part 2: {day9(100)}")
