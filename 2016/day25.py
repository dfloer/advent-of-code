def day25_split():
    with open('day25.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day25_vm(av=0, bv=0, cv=0, dv=0, max_steps=0):
    data = [x.split() for x in day25_split()]
    pc = 0
    regs = {'a': av, 'b': bv, 'c': cv, 'd': dv}
    idx = 0
    out = []
    while idx <= max_steps:
        try:
            inst = data[pc]
        except IndexError:
            return ''.join(out)
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
        elif op == "out":
            x = inst[1]
            if x in regs.keys():
                vx = int(regs[x])
            else:
                vx = int(x)
            out += [vx]
            pc += 1
        else:
            return regs
        if max_steps != 0:
            idx += 1
    return ''.join([str(x) for x in out])


def day25():
    x = 0
    while True:
        out = day25_vm(av=x, bv=0, cv=0, dv=0, max_steps=100000)
        if out.startswith("01" * (len(out) // 2)):
            return x
        x += 1
