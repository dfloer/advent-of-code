from collections import Counter


def day4_split():
    with open('day4.txt', 'r') as f:
        lines = f.read().splitlines()

    return lines


def day4_part1():
    stuff = day4_split()
    ids = []
    for x in stuff:
        room, room_id, checksum = parse_line(x)
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
        room, room_id, _ = parse_line(x)
        room_text = caesar_cipher(room, room_id % 26)
        if room_text.startswith("northpole"):
            return room, room_text, room_id


def caesar_cipher(cipher_text, shift):
    # 97 is the index in ASCII for 'a'.
    decrypted = [chr(((ord(c) - 97 + shift) % 26) + 97) for c in cipher_text]
    return ''.join(decrypted)


def parse_line(line):
    # Split into the room+id and checksum.
    room_data, checksum = line.split('[')
    # Remove the '-' from the input and stick the rest back together, ignoring the ID at the end.
    room = ''.join(room_data[:-4].split('-'))
    # Get the id.
    room_id = int(room_data[-3:])
    # trim the trailing ']'.
    checksum = checksum[:-1]
    return room, room_id, checksum
