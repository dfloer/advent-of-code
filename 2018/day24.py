import re


def day24_split():
    with open('day24.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    immune = True
    lines = day24_split()
    res = {"immune": [], "infection": []}
    for line in lines:
        if "Immune System:" in line:
            immune = True
            continue
        elif "Infection:" in line:
            immune = False
            continue
        elif len(line) <= 1:
            continue
        units, hp, attack, initiative = [int(x) for x in re.findall(r'-?\d+', line)]
        print(units, hp, attack, initiative)
        atk_i = line.split(' ').index(str(attack))
        dmg_type = line.split(' ')[atk_i + 1]
        d = re.findall(r'\((.* ?)\)', line)
        # print(d)
        if d != []:
            a = d[0].split(';')
            p = {"weak": [], "immune": []}
            for x in a:
                if "weak" in x:
                    p["weak"] += x[8:].split(', ')
                    # print("weak", x[8:].split(', '))
                if "immune" in x:
                    # print("immune", x[10:].split(', '))
                    p["immune"] += x[10:].split(', ')
        if immune:
            pass







def day24():
    input = parse()


if __name__ == "__main__":
    print(f"Solution to day 24 part 1: {day24()}")
