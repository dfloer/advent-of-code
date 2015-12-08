import hashlib

def day_4(seed, num_zeroes):
    idx = 0
    while(True):
        text = bytes(seed + str(idx), 'ascii')
        hash = hashlib.md5(text).hexdigest()
        if hash[0 : num_zeroes] == '0' * num_zeroes:
            break
        idx += 1
    return (idx, hash)