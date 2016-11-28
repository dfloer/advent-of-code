import ast
import json

def day8_split():
    with open('day8.txt', 'r') as f:
        lines = f.readlines()
    return lines


def day8_pt1():
    lines = day8_split()
    lines = [x.replace('\n', '') for x in lines]
    total_chars = sum(len(x) for x in lines)
    strings = [ast.literal_eval(x) for x in lines]
    string_chars = sum([len(x) for x in strings])
    return total_chars - string_chars


def day8_pt2():
    lines = day8_split()
    lines = [x.replace('\n', '') for x in lines]
    total_chars = sum(len(x) for x in lines)
    strings = [json.dumps(x) for x in lines]
    string_chars = sum([len(x) for x in strings])
    return string_chars - total_chars
