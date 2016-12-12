def day12_split():
    with open('day12.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day12(c_value=0):
    data = [x.split() for x in day12_split()]
    pc = 0
    regs = {'a': 0, 'b': 0, 'c': c_value, 'd': 0}
    while True:
        try:
            inst = data[pc]
        except IndexError:
            return regs
        op = inst[0]
        if op == "cpy":
            x = inst[1]
            y = inst[2]
            if x in regs.keys():
                regs[y] = regs[x]
            else:
                regs[y] = int(x)
            pc += 1
        elif op == "inc":
            r = inst[1]
            regs[r] += 1
            pc += 1
        elif op == "dec":
            r = inst[1]
            regs[r] -= 1
            pc += 1
        elif op == "jnz":
            x = inst[1]
            if x in regs.keys():
                vx = int(regs[x])
            else:
                vx = int(x)

            y = inst[2]
            if y in regs.keys():
                vy = int(regs[y])
            else:
                vy = int(y)
            if vx != 0:
                pc += vy
            else:
                pc += 1
        else:
            return regs
