def day_1_pt1(directions):
    num_up = directions.count('(')
    num_down = directions.count(')')
    return num_up - num_down
