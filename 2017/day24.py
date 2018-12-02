from collections import deque, defaultdict


def day24_split():
    with open('day24.txt', 'r') as f:
        lines = f.read().splitlines()
    return [x.split('/') for x in lines]


def day24_part1():
    input_data = day24_split()
    components = defaultdict(list)
    for a, b in input_data:
        a = int(a)
        b = int(b)
        components[a] += [(a, b)]
        components[b] += [(a, b)]

    max_strength = 0
    start = ([(0, 0)], 0, 0)
    dq = deque([start])

    while dq:
        path, strength, connection = dq.popleft()
        if strength > max_strength:
            max_strength = strength
        for candidate in components[connection]:
            if candidate not in path:
                new_path = path + [candidate]
                new_strength = strength + sum(candidate)
                new_connection = candidate[candidate.index(connection) - 1]
                dq.append((new_path, new_strength, new_connection))
    return max_strength


if __name__ == "__main__":
    print(f"Solution to day21 part1: {day24_part1()}")
    # print(f"Solution to day21 part1: {day24_part1()}")
