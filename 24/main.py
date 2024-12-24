import sys


class Gate():

    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def andGate(self, other):
        if self.value == None or other.value == None:
            return None
        return self.value & other.value

    def orGate(self, other):
        if self.value == None or other.value == None:
            return None
        return self.value | other.value

    def xorGate(self, other):
        if self.value == None or other.value == None:
            return None
        return self.value ^ other.value

    def __repr__(self):
        return f"{self.name} = {self.value}"


def part1(gates, operations):
    done = False
    while not done:
        for operation in operations:
            (gate1, op, gate2, output_gate) = operation
            if op == "AND":
                gates[output_gate].value = gates[gate1].andGate(gates[gate2])
            elif op == "OR":
                gates[output_gate].value = gates[gate1].orGate(gates[gate2])
            elif op == "XOR":
                gates[output_gate].value = gates[gate1].xorGate(gates[gate2])
            else:
                print("Unknown operation", op)
        bit = 0
        found_none = False
        result = ""
        while f"z{bit:02}" in gates:
            if gates[f"z{bit:02}"].value == None:
                found_none = True
                break
            result = str(gates[f"z{bit:02}"].value) + result
            bit += 1
        if not found_none:
            done = True
    return result


def puzzle(filename):
    total = 0
    total_pt2 = 0
    in_operations = False
    gates = {}
    operations = []

    lines = open(filename, 'r').read().split('\n')

    for line in lines:
        if line == "":
            in_operations = True
            continue
        if not in_operations:
            (name, value) = line.split(':')
            gates[name] = Gate(name, int(value))
        else:
            (gate1, op, gate2, _, output_gate) = line.split(' ')
            operations.append((gate1, op, gate2, output_gate))
            if gate1 not in gates:
                gates[gate1] = Gate(gate1)
            if gate2 not in gates:
                gates[gate2] = Gate(gate2)
            if output_gate not in gates:
                gates[output_gate] = Gate(output_gate)

    result = part1(gates, operations)
    total = int(result, 2)

    print("Part 1", total, result)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
