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


def solve_pt2(answer, startVal):
    global register_a, register_b, register_c, program, output
    print("Solving for", answer, startVal)
    for test_val in range(64):
        output = []
        register_a = (startVal << 3) + test_val
        ip = 0
        while ip < len(program):
            ip = execute_instruction(ip)
        if output == answer:
            return (startVal << 3) + test_val

    print("!!!! SHOULD NEVER GET HERE!!!!")
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


mnemonics = {
    0: 'adv',
    1: 'bxl',
    2: 'bst',
    3: 'jnz',
    4: 'bxc',
    5: 'out',
    6: 'bdv',
    7: 'cdv'
}


def print_program():
    for instruction, operand in zip(program[::2], program[1::2]):
        print(mnemonics[instruction], operand)


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

#    print("Register A", register_a)
#    print("Register B", register_b)
#    print("Register C", register_c)
    print("Program", program)
    #    print_program()
    ip = 0
    while ip < len(program):
        ip = execute_instruction(ip)


#    print("Register A", register_a)
#    print("Register B", register_b)
#    print("Register C", register_c)

    print("Output:", ",".join([str(x) for x in output]))

    answer = []
    startVal = 0
    for bytecode in program[::-1]:
        answer = [bytecode] + answer
        startVal = solve_pt2(answer, startVal)

    print("Register A", startVal)
    ip = 0
    register_a = startVal
    output = []
    while ip < len(program):
        ip = execute_instruction(ip)
    print("Output:", ",".join([str(x) for x in output]))

if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
