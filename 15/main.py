import sys
from copy import deepcopy

movements = []
robot = (0, 0)

already_moved = {}
warehouse = {}


def can_move(pos, direction):
    global already_moved, warehouse
    newX = pos[0]
    newY = pos[1]
    if direction == "^":
        newY = pos[1] - 1
    if direction == "v":
        newY = pos[1] + 1
    if direction == "<":
        newX = pos[0] - 1
    if direction == ">":
        newX = pos[0] + 1

    moveSpot = warehouse.get((newX, newY), '.')
    if moveSpot == '.':
        return True
    if moveSpot == '#':
        return False
    if (moveSpot == '[' or moveSpot == ']'):
        if direction == "<" or direction == ">":
            moving = can_move((newX, newY), direction)
            if moving:
                warehouse[(newX + (direction == '>') - (direction == '<'),
                           newY)] = moveSpot
                del warehouse[(newX, newY)]
            return moving
        if direction == "^" or direction == "v":
            side_dir = -1 if moveSpot == ']' else 1

            #            print("Trying to move: ", (newX, newY), (newX + side_dir, newY))
            moving = can_move((newX, newY), direction) and \
                     can_move((newX + side_dir, newY), direction)

            if moving:
                if (newX, newY) not in already_moved:
                    warehouse[(newX, newY + (direction == 'v') -
                               (direction == '^'))] = moveSpot
                    warehouse[(
                        newX + side_dir, newY + (direction == 'v') -
                        (direction == '^'))] = '[' if moveSpot == ']' else ']'
                    del warehouse[(newX, newY)]
                    del warehouse[(newX + side_dir, newY)]

                    already_moved[(newX, newY)] = True
                    already_moved[(newX + side_dir, newY)] = True
            return moving

    print("Should never get here")
    return False


width = 0
height = 0


def print_warehouse(warehouse):
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) == robot:
                line += "@"
            else:
                line += warehouse.get((x, y), '.')
        print(line)


def puzzle(filename):
    global width, height
    global robot
    global already_moved
    global warehouse
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    inMovements = False

    for y, line in enumerate(lines):
        if line == "":
            inMovements = True
            height = y
        if inMovements:
            movements.extend(line)
        else:
            for x, ch in enumerate(line):
                if ch == "#":
                    warehouse[(2 * x, y)] = ch
                    warehouse[(2 * x + 1, y)] = ch
                elif ch == "O":
                    warehouse[(2 * x, y)] = '['
                    warehouse[(2 * x + 1, y)] = ']'
                elif ch == "@":
                    robot = (2 * x, y)
    width = len(lines[0]) * 2
    print_warehouse(warehouse)

    for movement in movements:
        print("Move ", movement)
        already_moved = {}
        if can_move(robot, movement):
            robot = (robot[0] + (movement == '>') - (movement == '<'),
                     robot[1] + (movement == 'v') - (movement == '^'))
        # print_warehouse(warehouse)

    print_warehouse(warehouse)
    for location in warehouse:
        if warehouse[location] == '[':
            score = location[1] * 100 + location[0]
            total_pt2 += score

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
