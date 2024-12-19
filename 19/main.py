import sys
import re
from functools import lru_cache

dict_towels = {}


@lru_cache(maxsize=None)
def get_num_possibilities(pattern):
    global dict_towels
    if pattern == "":
        return 1
    if pattern[0] not in dict_towels:
        return 0
    possible_towels = dict_towels[pattern[0]]
    total = 0
    for towel in possible_towels:
        if pattern[:len(towel)] == towel:
            total += get_num_possibilities(pattern[len(towel):])
    return total


# Store towel in a huge hash map
# list should have letters that can be all or partially consumed
def store_towel(towel):
    global dict_towels

    partial_towel = ""
    for ch in towel:
        partial_towel += ch
        if partial_towel not in dict_towels:
            dict_towels[partial_towel] = []
        dict_towels[partial_towel].append(towel)


def puzzle(filename):
    total = 0
    total_pt2 = 0
    towels = []
    desired_patterns = []
    lines = open(filename, 'r').read().split('\n')
    in_patterns = False
    for line in lines:
        if in_patterns:
            desired_patterns.append(line)
        elif line == "":
            in_patterns = True
        else:
            towels = line.split(", ")
    print(towels)
    print(desired_patterns)

    for towel in towels:
        store_towel(towel)
    print(dict_towels)

    for pattern in desired_patterns:
        num = get_num_possibilities(pattern)
        print(num, pattern)
        if num > 0:
            total += 1
        total_pt2 += num
    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
