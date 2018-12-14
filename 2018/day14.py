def day14_split():
    with open('day14.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    n = int(day14_split()[0])
    return n


def day14():
    start_num = parse()
    print(start_num)
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1
    while True:
        s = str(recipes[elf_1] + recipes[elf_2])
        recipes += [int(x) for x in s]
        elf_1 += recipes[elf_1] + 1
        elf_1 %= len(recipes)
        elf_2 += recipes[elf_2] + 1
        elf_2 %= len(recipes)
        res = recipes[start_num : start_num + 10]
        if len(res) == 10:
            return ''.join([str(x) for x in res])


def print_recipes(recipes, elf_1, elf_2):
    for idx, r in enumerate(recipes):
        if idx == elf_1:
            print(f"({r})", end='')
        elif idx == elf_2:
            print(f"[{r}]", end='')
        else:
            print(f" {r} ", end='')
    print()



if __name__ == "__main__":
    print(f"Solution to day 14 part 1: {day14()}")