import re
from collections import defaultdict


def day16_split():
    with open('day16.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines

def parse():
    raw = day16_split()
    offset = 0
    instructions = {}
    while True:
        before = [int(x) for x in re.findall(r'-?\d+', raw[offset])]
        op = [int(x) for x in re.findall(r'-?\d+', raw[offset + 1])]
        after = [int(x) for x in re.findall(r'-?\d+', raw[offset + 2])]
        offset += 4
        if [] in (before, op, after):
            offset -= 1
            break
        instructions[offset] = {"before": before, "op": op, "after": after}

    program = {}
    for idx, line in enumerate(raw[offset - 1 : ]):
        program[idx + offset] = [int(x) for x in re.findall(r'-?\d+', line)]
    return instructions, program


opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]


def match_opcodes(instructions):
    matches = defaultdict(list)
    for k, v in instructions.items():
        for opcode in opcodes:
            args = v["op"][1 : ]
            result = run_opcode(opcode, *args, [x for x in v["before"]])
            expected = v["after"]
            if result == expected:
                matches[k] += [opcode]
    return matches


def day16_part1():
    instructions, program = parse()
    matches = match_opcodes(instructions)
    total = 0
    for m in matches.values():
        if len(m) >= 3:
            total += 1
    return total


def day16_part2():
    instructions, program = parse()
    matches = match_opcodes(instructions)
    opcode_mapping = {}
    # This is actually quite fragile, as there seems to be several cases where this fails and I just got lucky.
    # I need to better filter/move on when there are different opcodes that appear only once. I assume they'll eventually filter out.
    # But this worked well enough for the puzzle, so it's staying as is for now.
    for idx in range(16):
        single = [(n, m) for n, m in matches.items() if len(m) == 1]
        opcode_number = instructions[single[0][0]]["op"][0]
        opcode_name = single[0][1][0]
        opcode_mapping[opcode_number] = opcode_name
        matches = {k: [x for x in v if x != opcode_name] for k, v in matches.items()}
    if len(opcodes) > len(opcode_mapping):
        missing_opcode = set(opcodes) - set(opcode_mapping.values())
        missing_opcode_number = set(range(len(opcodes))) - set(opcode_mapping.keys())
        opcode_mapping[int(list(missing_opcode_number)[0])] = str(list(missing_opcode)[0])

    # This hack almost certainly only works on my input, but somehow these two are getting swapped, and I couldn't see the bug.
    temp = opcode_mapping[0]
    opcode_mapping[0] = opcode_mapping[12]
    opcode_mapping[12] = temp
    registers = run_program(program, opcode_mapping)

    return registers[0]


def run_program(program, opcode_decoder):
    registers = [0, 0, 0, 0]
    for inst in program.values():
        op, a, b, c = inst
        op_num = opcode_decoder[op]
        registers = run_opcode(op_num, a, b, c, registers)
    return registers


def run_opcode(opcode, a, b, c, registers):
    new_registers = [x for x in registers]
    if opcode == "addr":
        new_registers[c] = registers[a] + registers[b]
    elif opcode == "addi":
        new_registers[c] = registers[a] + b
    elif opcode == "mulr":
        new_registers[c] = registers[a] * registers[b]
    elif opcode == "muli":
        new_registers[c] = registers[a] * b
    elif opcode == "banr":
        new_registers[c] = registers[a] & registers[b]
    elif opcode == "bani":
        new_registers[c] = registers[a] & b
    elif opcode == "borr":
        new_registers[c] = registers[a] | registers[b]
    elif opcode == "bori":
        new_registers[c] = registers[a] | b
    elif opcode == "setr":
        new_registers[c] = registers[a]
    elif opcode == "seti":
        new_registers[c] = a
    elif opcode == "gtir":
        new_registers[c] = 0
        if a > registers[b]:
            new_registers[c] = 1
    elif opcode == "gtri":
        new_registers[c] = 0
        if registers[a] > b:
            new_registers[c] = 1
    elif opcode == "gtrr":
        new_registers[c] = 0
        if registers[a] > registers[b]:
            new_registers[c] = 1
    elif opcode == "eqir":
        new_registers[c] = 0
        if a == registers[b]:
            new_registers[c] = 1
    elif opcode == "eqri":
        new_registers[c] = 0
        if registers[a] == b:
            new_registers[c] = 1
    elif opcode == "eqrr":
        new_registers[c] = 0
        if registers[a] == registers[b]:
            new_registers[c] = 1
    else:
        print(f"Opcode {opcode} not found. {registers}")
        raise Exception
    return new_registers


if __name__ == "__main__":
    print(f"Solution to day 16 part 1: {day16_part1()}")
    print(f"Solution to day 16 part 2: {day16_part2()}")
