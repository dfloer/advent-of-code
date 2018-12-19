from functools import reduce


def day19_split():
    with open('day19.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    lines = day19_split()
    res = []
    ip = -1
    for line in lines:
        line = line.split(' ')
        if "#ip" in line:
            ip = int(line[-1])
        else:
            inst = (line[0], int(line[1]), int(line[2]), int(line[3]))
            res += [inst]
    return ip, res


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


def day19(r0=0):
    """
    What is the algorithm doing? Basically, it's calculating a number (stored in R4).
    With that number, it very slowly find all of the factors of it.
    And then sums all those factors together.
    I noticed this by dropping R4's value into WolframAlpha, and noting that the factors added up to my answer for part 1.
    So did this for part 2, with much faster code to short circuit the execution.
    """
    ip, instructions = parse()
    registers = [r0, 0, 0, 0, 0, 0]
    ip_value = 0
    clock = 0
    while True:
        registers[ip] = ip_value
        try:
            op, a, b, c = instructions[ip_value]
        except Exception:
            print(f"{ip_value} ip outside of program, halting.")
            break
        registers = run_opcode(op, a, b, c, registers)
        ip_value = registers[ip]
        ip_value += 1
        clock += 1
        if clock > 30:
            break
    result = sum(find_divisors(registers[4]))
    return result


def find_divisors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


if __name__ == "__main__":
    print(f"Solution to day 19 part 1: {day19()}")
    print(f"Solution to day 19 part 2: {day19(1)}")
