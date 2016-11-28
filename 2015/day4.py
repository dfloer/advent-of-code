import hashlib

def day_4(seed, num_zeroes):
    idx = 0
    while(True):
        text = bytes(seed + str(idx), 'ascii')
        to_hash = hashlib.md5(text).hexdigest()
        if to_hash[0 : num_zeroes] == '0' * num_zeroes:
            break
        idx += 1
    return (idx, to_hash)