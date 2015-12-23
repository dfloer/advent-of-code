def day23_split():
    with open('day23.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day23_parse():
    lines = day23_split()
    output = []
    for line in lines:
        output.append(line.split())
    return output


def day23():
    instructions = day23_parse()
    offset = 0
    reg_a = 0
    reg_b = 0
    while True:
        try:
            inst = instructions[offset]
        except IndexError:
            return reg_a, reg_b
        op = inst[0]
        if op == 'jie':
            reg = inst[1].strip(',')
            jump = int(inst[2])
            if reg == 'a' and reg_a % 2 == 0:
                offset += jump
            elif reg == 'b' and reg_b % 2 == 0:
                offset += jump
            else:
                offset += 1
        elif op == 'jio':
            reg = inst[1].strip(',')
            jump = int(inst[2])
            if reg == 'a' and reg_a  == 1:
                offset += jump
            elif reg == 'b' and reg_b == 1:
                offset += jump
            else:
                offset += 1
        elif op == 'hlf':
            reg = inst[1]
            if reg == 'a':
                reg_a //= 2
            else:
                reg_b //= 2
            offset += 1
        elif op == 'tpl':
            reg = inst[1]
            if reg == 'a':
                reg_a *= 3
            else:
                reg_b *= 3
            offset += 1
        elif op == 'inc':
            reg = inst[1]
            if reg == 'a':
                reg_a += 1
            else:
                reg_b += 1
            offset += 1
        elif op == 'jmp':
            jump = int(inst[1])
            offset += jump
        else:
            return reg_a, reg_b
