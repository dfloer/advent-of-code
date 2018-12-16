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
    while offset < 3244:
        before = [int(x) for x in re.findall(r'-?\d+', raw[offset])]
        op = [int(x) for x in re.findall(r'-?\d+', raw[offset + 1])]
        after = [int(x) for x in re.findall(r'-?\d+', raw[offset + 2])]
        instructions[offset] = {"before": before, "op": op, "after": after}
        offset += 4
    return instructions


opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]


def day16_part1():
    instructions = parse()
    matches = defaultdict(list)
    for k, v in instructions.items():
        for opcode in opcodes:
            args = v["op"][1 : ]
            result = run_opcode(opcode, *args, [x for x in v["before"]])
            expected = v["after"]
            if result == expected:
                matches[k] += [opcode]
    total = 0
    for m in matches.values():
        if len(m) >= 3:
            total += 1
    return total


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