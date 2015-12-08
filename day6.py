import collections


def day6_split():
    with open('day6.txt', 'r') as f:
        lines = f.readlines()
        output = []
        for x in lines:
            x = x.split(' ')
            if x[0] == 'toggle':
                f, s = 1, 3
                action = 'toggle'
            else:
                f, s = 2, 4
                if x[1] == 'on':
                    action = 'on'
                else:
                    action = 'off'
            box = [action, x[f].split(','), x[s].split(',')]
            output.append(box)
    return output


def day6():
    boxes = day6_split()
    lights = collections.defaultdict(bool)
    for box in boxes:
        action = box[0]
        tl = box[1]
        br = box[2]

        x_dim = (int(tl[0]), int(br[0]) + 1)
        y_dim = (int(tl[1]), int(br[1]) + 1)
        for x in range(*x_dim):
            for y in range(*y_dim):
                if action == 'toggle':
                    lights[(x, y)] = not lights[(x, y)]
                elif action == 'on':
                    lights[(x, y)] = True
                else:
                    lights[(x, y)] = False
    return list(lights.values()).count(True)
