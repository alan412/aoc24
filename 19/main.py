import sys
import re


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

    reg_ex_expression = "^("
    for towel in towels:
        reg_ex_expression += "(" + towel + ")|"
    reg_ex_expression = reg_ex_expression[:-1]
    reg_ex_expression += ")+$"

    for pattern in desired_patterns:
        match = re.match(reg_ex_expression, pattern)
        print(match, pattern)
        if match != None:
            total += 1

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
