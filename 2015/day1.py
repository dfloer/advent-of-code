def day_1_pt1(directions):
    num_up = directions.count('(')
    num_down = directions.count(')')
    return num_up - num_down

def day1_pt2(directions):
    numbers = [1 if x == '(' else -1 for x in directions]
    total = 0
    for idx in range(len(numbers)):
        total += numbers[idx]
        if total == -1:
            return idx + 1  # +1 needed because using 1 based index in problem.