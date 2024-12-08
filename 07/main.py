import sys


def could_be_true(result, operands):
    if len(operands) == 1:
        return result == operands[0]
    if could_be_true(result, [operands[0] + operands[1]] + operands[2:]):
        return True
    if could_be_true(result, [operands[0] * operands[1]] + operands[2:]):
        return True
    if could_be_true(result, [int(str(operands[0]) + str(operands[1]))] +
                     operands[2:]):
        return True
    return False


class Equation:

    def __init__(self, string):
        parts = string.split(":")
        self.result = int(parts[0])
        self.operands = [int(x) for x in parts[1][1:].split(" ")]

    def value_if_true(self):
        if could_be_true(self.result, self.operands):
            print("True:", self)
            return self.result
        else:
            return 0

    def __str__(self) -> str:
        return f"{self.operands} = {self.result}"


def puzzle(filename):
    total = 0
    equations = []
    lines = open(filename, 'r').read().split('\n')
    for line in lines:
        equations.append(Equation(line))
    for eq in equations:
        total += eq.value_if_true()

    print("Part 1", total)


#    print("Part 2", total_pt2)

if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
