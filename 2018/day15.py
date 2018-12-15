from queue import PriorityQueue
import colorama
from collections import deque


colorama.init()

def day15_split():
    with open('day15.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse():
    combatants = {}
    input_lines = day15_split()
    board = {}
    for x, line in enumerate(input_lines):
        for y, e in enumerate(line):
            if e in ('G', 'E'):
                combatants[(x, y)] = e
                e = '.'
            board[(x, y)] = e
    return board, combatants


def day15(atk=3, hp=200):
    board, combatants = parse()
    combatants = {k: {"type": v, "atk": atk, "hp": hp} for k, v in combatants.items()}
    ticks = 1
    print('0')
    print_board(board, combatants)
    print("----\n")
    while True:
        combatants = run_one_round(board, combatants)
        print(ticks)
        print_board(board, combatants)
        print("combatants:")
        for k, v in combatants.items():
            print(k, v)
        print('\n')
        if not combatants:
            break

        elves = sum([v["hp"] for k, v in combatants.items() if v["type"] == 'E'])
        goblins = sum([v["hp"] for k, v in combatants.items() if v["type"] == 'G'])
        if elves == 0 or goblins == 0:
            break
        ticks += 1
        if ticks == 2:
            break
    remaining_hp = sum([v["hp"] for k, v in combatants.items()])

    print(ticks, remaining_hp)
    return ticks * remaining_hp


def run_one_round(board, combatants):
    sorted(combatants, key=lambda k: (k[0], k[1]))
    new_combatants = {k: v for k, v in combatants.items()}
    for k, v in combatants.items():
        if v["type"] == 'G':
            target = 'E'
        else:
            target = 'G'
        # print(k, v, target)

        next_position = find_target(k, target, board, combatants)
        if next_position is None:
            return False
        # print(k, next_position)

        # First try moving everyone. Don't move into a wall (should never happen) or a combatant.
        if board[next_position] == '.' and next_position not in new_combatants.keys():
            new_combatants[next_position] = v
            del new_combatants[k]
        elif board[next_position] == '#':
            print("Tried to move into a stupid wall.")
        # If there's an enemy in the spot we want to go to, don't move and make it murder time.
        elif next_position in new_combatants.keys():
            pass
        else:
            print("what case did I miss?")

        # Now that we've moved, time to get our murder on.
        # First find if we're next to an enemy.
        print("attacker:", k, v, target)
        enemies = [n for n in find_neighbours(next_position) if n in new_combatants.keys()]
        if sorted(enemies, key=lambda a: (a[0], a[1])):
            print("units:", enemies)
        enemies = [e for e in enemies if new_combatants[e]["type"] == target]
        # for x in enemies:
            # print(x, v["type"], new_combatants[x])
        if sorted(enemies, key=lambda a: (a[0], a[1])):
            print("enemies:", enemies)
        # If there are any enemies nearby, we need to kill them first by HP, and then by reading order.
        # find_neighbours() should be reading order.
        enemies_by_health = sorted(enemies, key=lambda a: new_combatants[a]["hp"])
        for enemy in enemies_by_health:
            print("health sort", enemy, new_combatants[enemy]["hp"])
        if enemies != []:
            # Todo: make sure this works!
            to_attack = enemies_by_health[0]
            hp = new_combatants[to_attack]["hp"]
            atk = new_combatants[next_position]["atk"]
            # print(hp, atk)
            hp -= atk
            # Success! Someone has been murdered. Kill them and hide the body. Er, remove them from the datastructure.
            if hp <= 0:
                del new_combatants[to_attack]
            else:
                new_combatants[to_attack]["hp"] = hp
    return new_combatants


def find_target(start_cell, target_type, board, combatants):
    # My first implementation had them following set paths, but I didn't account for everyone moving changing the paths.
    # So what we really want is the next position we should be in.
    target_cell, visited, total_distance = find_paths(start_cell, target_type, board, combatants)
    # distance = total_distance[target_cell]

    if target_cell is None:
        return None

    next_position = target_cell
    next_cell = visited[next_position]
    while next_cell != start_cell:
        next_position = next_cell
        next_cell = visited[next_position]
    return next_position


def find_paths(start_cell, target_type, board, combatants, cost=1):
    visited = {}
    total_distance = {}

    to_visit = deque()
    for neighbour in find_neighbours(start_cell):
        to_visit.append(neighbour)
        visited[neighbour] = start_cell
        total_distance[neighbour] = cost
    target_cell = None
    while len(to_visit) > 0:
        next_cell = to_visit.popleft()
        try:
            combatant_type = combatants[next_cell]["type"]
            if combatant_type == target_type:
                target_cell = next_cell
                break
        except Exception:
            pass
        if board[next_cell] != '.':
            continue
        for neighbour in find_neighbours(next_cell):
            if neighbour not in visited:
                visited[neighbour] = next_cell
                total_distance[neighbour] = total_distance[next_cell] + cost
                to_visit.append(neighbour)
    return target_cell, visited, total_distance


def find_neighbours(xy_coords):
    x_coord, y_coord = xy_coords
    result = []
    # This should be reading order.
    for x, y in [(x_coord - 1, y_coord), (x_coord , y_coord - 1), (x_coord, y_coord + 1), (x_coord + 1, y_coord)]:
        result += [(x, y)]
    return result


def print_board(board, combatants):
    max_x = max(x[0] for x in board.keys())
    max_y = max(x[1] for x in board.keys())
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            e = board[(x, y)]
            if (x, y) in combatants:
                c = colorama.Fore.CYAN
                if combatants[x, y]["type"] == 'E':
                    c = colorama.Fore.GREEN
                e = c + combatants[x, y]["type"] + colorama.Fore.RESET
            else:
                if e == '.':
                    e = colorama.Style.RESET_ALL + colorama.Fore.RED + e + colorama.Fore.RESET
                else:
                    e = colorama.Fore.WHITE + e + colorama.Fore.RESET
            print(colorama.Style.BRIGHT + e + colorama.Style.RESET_ALL, end='')
        print()
    elves = [k for k, v in combatants.items() if v["type"] == 'E']
    goblins = [k for k, v in combatants.items() if v["type"] == 'G']
    print(f"Elves: {len(elves)}")
    print(f"Goblins: {len(goblins)}")


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    print(f"Solution to day 15 part 1: {day15()}")