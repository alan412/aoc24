import sys
import re
import numpy as np


class Machine:

    def __init__(self, btnA_X, btnA_Y, btnB_X, btnB_Y, prize_X, prize_Y):
        self.btnA_X = int(btnA_X)
        self.btnA_Y = int(btnA_Y)
        self.btnB_X = int(btnB_X)
        self.btnB_Y = int(btnB_Y)
        self.prize_X = int(prize_X)
        self.prize_Y = int(prize_Y)

    def __repr__(self):
        return f"Machine: {self.btnA_X} {self.btnA_Y} {self.btnB_X} {self.btnB_Y} {self.prize_X} {self.prize_Y}"

    def solve(self):
        A = np.array([[self.btnA_X, self.btnB_X], [self.btnA_Y, self.btnB_Y]])
        B = np.array([self.prize_X, self.prize_Y])
        s = np.linalg.solve(A, B)

        if np.all(np.abs(s - np.round(s)) < 1e-3):
            return s[0] * 3 + s[1] * 1
        return 0


def puzzle(filename):
    machines = []
    machines_pt2 = []
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    a_re = re.compile(r"\D+(\d+)\D+(\d+)")
    for i in range(0, 1 + len(lines) // 4):
        btnA_X, btnA_Y = a_re.match(lines[i * 4]).groups()
        btnB_X, btnB_Y = a_re.match(lines[i * 4 + 1]).groups()
        prize_X, prize_Y = a_re.match(lines[i * 4 + 2]).groups()
        machines.append(
            Machine(btnA_X, btnA_Y, btnB_X, btnB_Y, prize_X, prize_Y))
        machines_pt2.append(
            Machine(btnA_X, btnA_Y, btnB_X, btnB_Y,
                    int(prize_X) + 10000000000000,
                    int(prize_Y) + 10000000000000))

    for machine in machines:
        machine_tokens = machine.solve()
        total += machine_tokens
        print(machine_tokens, total)

    print("Part 1", total)
    for machine in machines_pt2:
        machine_tokens = machine.solve()
        total_pt2 += machine_tokens
        print(machine_tokens, total_pt2)

    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
