def day14_split():
    with open('day14.txt', 'r') as f:
        lines = f.readlines()
    return lines


def parse():
    n = int(day14_split()[0])
    return str(n)


def day14(start_num):
    recipes = "37"
    elf_1 = 0
    elf_2 = 1
    # In general, this may not be safe to so, but as part2 happens long after part 1, we're good here.
    while start_num not in recipes[-len(start_num) - 1 : ]:
        a = int(recipes[elf_1])
        b = int(recipes[elf_2])
        recipes += str(a + b)
        elf_1 = (elf_1 + a + 1) % len(recipes)
        elf_2 = (elf_2 + b + 1) % len(recipes)
    pt1 = recipes[int(start_num) : int(start_num) + 10]
    pt2 = recipes.index(start_num)
    return pt1, pt2


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
    pt1, pt2 = day14(parse())
    print(f"Solution to day 14 part 1: {pt1}")
    print(f"Solution to day 14 part 2: {pt2}")