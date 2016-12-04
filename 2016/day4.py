from collections import Counter

def day4_split():
    with open('day4.txt', 'r') as f:
        lines = f.read().splitlines()

    return lines

def day4_part1():
    stuff = day4_split()
    ids = []
    for x in stuff:
        line = x.split('[')
        checksum = line[1][:-1]
        room = ''.join(line[0][:-4].split('-'))
        room_id = int(line[0][-3:])
        counts = Counter(room)
        # Sort the dictionary according to the key and then value. Puts the largest counts first, sorted alphabetically.
        sorted_counts = [v[0] for v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))][:5]
        calc_sum = ''.join(sorted_counts)
        if calc_sum == checksum:
            ids += [room_id]
    return sum(ids)


def day4_part2():
    stuff = day4_split()
    for x in stuff:
        line = x.split('[')
        room = ''.join(line[0][:-4].split('-'))
        room_id = int(line[0][-3:])
        room_text = caesar_cipher(room, room_id % 26)
        if room_text.startswith("northpole"):
            return room, room_text, room_id


def caesar_cipher(cipher_text, shift):
    # 97 is the index in ASCII for 'a'.
    decrypted = [chr(((ord(c) - 97 + shift) % 26) + 97) for c in cipher_text]
    return ''.join(decrypted)
