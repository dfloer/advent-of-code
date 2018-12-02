def day25_split():
    with open('day25.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse(lines):
    start_state = lines[0][-2]
    checksum_value = int(lines[1].split(' ')[5])
    instructions = {}
    for x in range(3, len(lines), 10):
        block = lines[x: x + 9]
        block_start_state, block_instructions = parse_inst_block(block)
        instructions[block_start_state] = block_instructions
    return start_state, checksum_value, instructions


def parse_inst_block(block):
    """In state B:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D."""
    res = {}
    start_state = block[0][-2]
    for idx in range(1, 9, 4):
        sub_block = block[idx : idx + 4]
        check = int(sub_block[0][-2])
        write = int(sub_block[1][-2])
        if "right" in sub_block[2]:
            direction = 1
        else:
            direction = -1
        state = sub_block[3][-2]
        n = {'write_value': write, 'direction': direction, 'next_state': state}
        res[check] = n
    return start_state, res


def day25_part1():
    lines = day25_split()
    start_state, checksum_iteration, instructions = parse(lines)
    i = 0
    current_state = start_state
    tape = {}
    cursor = 0
    while i <= checksum_iteration:
        try:
            tape[cursor]
        except KeyError:
            tape[cursor] = 0
        current_value = tape[cursor]
        inst = instructions[current_state][current_value]
        tape[cursor] = inst["write_value"]
        cursor += inst["direction"]
        current_state = inst["next_state"]
        i += 1
    return sum(tape.values())


if __name__ == "__main__":
    print(f"Solution to day 2 part 1: {day25_part1()}")
    # print(f"Solution to day 2 part 1: '{day25_part2()}'")
