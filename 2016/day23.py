def day23_split():
    with open('day23.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def day23(av=7, bv=0, cv=0, dv=0, part2=False):
    data = [x.split() for x in day23_split()]
    pc = 0
    regs = {'a': av, 'b': bv, 'c': cv, 'd': dv}
    while True:
        #print(regs)
        # This is replacing a very bad multiplication done by repeated additions in the program.
        if pc == 4 and part2:
            print(regs)
            regs['a'] = regs['b'] * regs['d']
            regs['c'] = 0
            regs['d'] = 0
            print(regs)
            pc = 10
            continue
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
        elif op == "tgl":
            x = inst[1]
            if x in regs.keys():
                vx = int(regs[x])
            else:
                vx = int(x)
            new_pc = pc + vx
            new_inst = toggle(data, new_pc)
            if new_inst:
                data[new_pc] = new_inst
            pc += 1
        else:
            return regs


def toggle(data, new_pc):
    try:
        inst = data[new_pc]
    except IndexError:
        return False
    op = inst[0]
    if op == "inc":
        new_op = "dec"
    elif len(inst) == 2:
        new_op = "inc"
    elif op == "jnz":
        new_op = "cpy"
    elif len(inst) == 3:
        new_op = "jnz"
    else:
        print("tgl drop", inst)
        return False
    new_inst = [new_op] + inst[1:]
    return new_inst

