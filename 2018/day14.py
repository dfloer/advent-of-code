def day14_split():
    with open('day14.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    n = int(day14_split()[0])
    return n


def day14_part1(start_num):
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


def day14_part2(start_num):
    recipes = [3, 7]
    elf_1 = 0
    elf_2 = 1
    start_num = str(start_num)
    while True:
        s = str(recipes[elf_1] + recipes[elf_2])
        recipes += [int(x) for x in s]
        elf_1 = (elf_1 + recipes[elf_1] + 1) % len(recipes)
        elf_2 = (elf_2 + recipes[elf_2] + 1) % len(recipes)
        # The slightly larger range is needed because a sum can add one or two results to the end of our list.
        # And we don't want to miss the case where our number appears offset from the end rather than at the end.
        s = ''.join(str(x) for x in recipes[-len(start_num) - 1 : ])
        if start_num in s:
            r = ''.join(str(x) for x in recipes)
            return r.index(start_num)


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
    n = parse()
    print(f"Solution to day 14 part 1: {day14_part1(n)}")
    print(f"Solution to day 14 part 2: {day14_part2(n)}")