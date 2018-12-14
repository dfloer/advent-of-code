def day13_split():
    with open('day13.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day13_split()
    tracks = {}
    mine_carts = []
    directions = {"<": -1, "v": +1j, ">": +1, "^": -1j}
    all_parts = {"<": "-", "v": "|", ">": "-", "^": "|"}
    # After getting stuck for several hours trying to solve this the old way, I did some research on maze algorithms.
    # And found that you can represent mazes using complex numbers, so I'm trying that out now.
    for y, line in enumerate(lines):
        for x, e in enumerate(line):
            if e in ('<', '>', 'v', '^'):
                direction = directions[e]
                new_cart = {"current_location": x + y * 1j, "current_direction": direction, "current_cross_direction": 0, "crashed": False}
                mine_carts += [new_cart]
                track_part = all_parts[e]
            else:
                track_part = e
            # Only care about when a cart changes direction.
            if track_part in ('\\', '/', '+'):
                tracks[(x + y * 1j)] = track_part
    return tracks, mine_carts


def corner_turn(next_part, mine_cart):
    if next_part == "+":
        # cart can either turn forward, right or left. I missed this part of the problem completely for several hours...
        mine_cart["current_direction"] *= -1j * 1j ** mine_cart["current_cross_direction"]
        mine_cart["current_cross_direction"] = (mine_cart["current_cross_direction"] + 1) % 3
    # Note that all of these are with a +'ve y-axis downwards instead of the normal up. Yep, that got me too...
    elif next_part == "/":
        if mine_cart["current_direction"].real == 0:
            mine_cart["current_direction"] *= 1j  # up to right, down to left.
        else:
            mine_cart["current_direction"] *= -1j  # right to up, left to down
    elif next_part == "\\":
        if mine_cart["current_direction"].real == 0:
            mine_cart["current_direction"] *= -1j  # down to right, up to left
        else:
            mine_cart["current_direction"] *= 1j  # right to down, left to up
    return mine_cart


def day13_part1():
    tracks, mine_carts = parse()
    while True:
        # Important!
        mine_carts.sort(key=lambda k: (k["current_location"].imag, k["current_location"].real))
        for idx, mine_cart in enumerate(mine_carts):
            # update the cart's position
            mine_cart["current_location"] += mine_cart["current_direction"]
            # Check and see if we just ran into a cart.
            for other_cart in mine_carts:
                if other_cart != mine_cart:
                    a = other_cart["current_location"]
                    b = mine_cart["current_location"]
                    if a == b:
                        x_coord = int(a.real)
                        y_coord = int(a.imag)
                        return f"{x_coord},{y_coord}"
            try:
                track_part = tracks[mine_cart["current_location"]]
            except KeyError:
                track_part = ' '
                tracks[mine_cart["current_location"]] = track_part
            mine_carts[idx] = corner_turn(track_part, mine_cart)


def day13_part2():
    tracks, mine_carts = parse()
    while len(mine_carts) > 1:
        # Important!
        mine_carts.sort(key=lambda k: (k["current_location"].imag, k["current_location"].real))
        for idx, mine_cart in enumerate(mine_carts):
            if mine_cart["crashed"]:
                continue
            # update the cart's position
            mine_cart["current_location"] += mine_cart["current_direction"]
            # Check and see if we just ran into a cart.
            for other_cart in mine_carts:
                if other_cart != mine_cart:
                    a = other_cart["current_location"]
                    b = mine_cart["current_location"]
                    if a == b:
                        mine_cart["crashed"] = True
                        other_cart["crashed"] = True
                        break
            try:
                track_part = tracks[mine_cart["current_location"]]
            except KeyError:
                track_part = ' '
                tracks[mine_cart["current_location"]] = track_part
            mine_carts[idx] = corner_turn(track_part, mine_cart)
        # Remove crashed carts.
        mine_carts = [x for x in mine_carts if not x["crashed"]]
    x_coord = int(mine_carts[0]["current_location"].real)
    y_coord = int(mine_carts[0]["current_location"].imag)
    return f"{x_coord},{y_coord}"


if __name__ == "__main__":
    print(f"Solution to day 13 part 1: {day13_part1()}")
    print(f"Solution to day 13 part 1: {day13_part2()}")
