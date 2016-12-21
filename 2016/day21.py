from itertools import permutations


def day21_split():
    with open('day21.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


# gcedfahb
def day21(pw='abcdefgh'):
    data = day21_split()
    pw = list(pw)
    for entry in data:
        oper = entry.split()
        op = oper[0]
        if op == "swap":
            if oper[1] == "position":
                x = int(oper[2])
                y = int(oper[-1])
            elif oper[1] == "letter":
                x = pw.index(oper[2])
                y = pw.index(oper[-1])
            pw[x], pw[y] = pw[y], pw[x]  # Swap letter at posn x and y.
        elif op == "rotate":
            if oper[1] == "based":
                x = oper[-1]
                idx = pw.index(x)
                rot = ((idx + 1 + (idx >= 4)) % len(pw)) * -1  # Because True == 1.
            else:
                dr = oper[1]
                amt = int(oper[2])
                rot = amt
                if dr == "right":
                    rot *= -1
            pw = pw[rot:] + pw[:rot]
        elif op == "reverse":
            x = int(oper[2])
            y = int(oper[-1])
            pw[x : y + 1] = pw[x : y + 1][::-1]
        elif op == "move":
            x = int(oper[2])
            y = int(oper[-1])
            pw.insert(y, pw.pop(x))
        else:
            print("WTF?")
    return ''.join(pw)


def day21_part2(pw='fbgdceah'):
    letters = 'abcdefgh'
    possibles = permutations(letters, len(letters))
    for p in possibles:
        c = day21(p)
        if c == pw:
            return ''.join(p)
