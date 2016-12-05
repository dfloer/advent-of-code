from hashlib import md5


def day5(input):
    password = []
    idx = 0
    while True:
        hash = md5()
        to_hash = input + str(idx)
        hash.update(to_hash.encode('utf-8'))
        candidate = hash.hexdigest()
        if candidate[:5] == '00000':
            password += [candidate[5]]
        idx += 1
        if len(password) == 8:
            break

    return''.join(password)
