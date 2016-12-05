from hashlib import md5


def day5_part1(input_text):
    password = []
    idx = 0
    while True:
        h = md5()
        to_hash = input_text + str(idx)
        h.update(to_hash.encode('utf-8'))
        candidate = h.hexdigest()
        if candidate[:5] == '00000':
            password += [candidate[5]]
        idx += 1
        if len(password) == 8:
            break

    return''.join(password)


def day5_part2(input_text):
    password = [''] * 8
    idx = 0
    while True:
        h = md5()
        to_hash = input_text + str(idx)
        h.update(to_hash.encode('utf-8'))
        candidate = h.hexdigest()
        if candidate[:5] == '00000':
            try:
                posn = int(candidate[5])
                if password[posn] == '':
                    password[posn] = candidate[6]
            except IndexError:
                # Handles the case when we already have an index that's too high.
                pass
            except ValueError:
                # Handles indexes that aren't possible.
                pass
        idx += 1
        if password.count('') == 0:
            break

    return ''.join(password)
