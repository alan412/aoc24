import sys

program = []
register_a = 0
register_b = 0
register_c = 0
output = []


def get_combo_operand(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c
    else:
        print("Unknown operand", operand)
        return 0


def execute_instruction(ip):
    global register_a, register_b, register_c, program, output

    instruction = program[ip]
    operand = program[ip + 1]

    if instruction == 0:  # adv
        register_a = int(register_a / 2**get_combo_operand(operand))
    elif instruction == 1:  # bxl
        register_b = register_b ^ operand
    elif instruction == 2:  # bst
        register_b = get_combo_operand(operand) & 0x7
    elif instruction == 3:  # jnz
        if (register_a != 0):
            return operand
    elif instruction == 4:  # bxc
        register_b = register_b ^ register_c
    elif instruction == 5:  # out
        output.append(get_combo_operand(operand) % 8)
    elif instruction == 6:  # bdv
        register_b = int(register_a / 2**get_combo_operand(operand))
    elif instruction == 7:  # cdv
        register_c = int(register_a / 2**get_combo_operand(operand))
    else:
        print("Unknown instruction", instruction, "at", ip)
    return ip + 2


def puzzle(filename):
    total = 0
    total_pt2 = 0
    ip = 0
    global register_a, register_b, register_c, program, output

    lines = open(filename, 'r').read().split('\n')
    for line in lines:
        groups = line.split(':')
        if groups[0] == "Register A":
            register_a = int(groups[1])
        elif groups[0] == "Register B":
            register_b = int(groups[1])
        elif groups[0] == "Register C":
            register_c = int(groups[1])
        elif groups[0] == "Program":
            program = [int(x) for x in groups[1].split(',')]

    print("Register A", register_a)
    print("Register B", register_b)
    print("Register C", register_c)
    print("Program", program)
    ip = 0
    while ip < len(program):
        ip = execute_instruction(ip)

    print("Register A", register_a)
    print("Register B", register_b)
    print("Register C", register_c)

    print("Output:", ",".join([str(x) for x in output]))

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
