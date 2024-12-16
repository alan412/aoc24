import sys

movements = []
warehouse = {}
robot = (0, 0)


def can_move(pos, direction):
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
    if moveSpot == 'O':
        moving = can_move((newX, newY), direction)
        if moving:
            warehouse[(newX + (direction == '>') - (direction == '<'),
                       newY + (direction == 'v') - (direction == '^'))] = 'O'
            del warehouse[(newX, newY)]
        return moving
    print("Should never get here")
    return False


width = 0
height = 0


def print_warehouse():
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
                if ch == "#" or ch == "O":
                    warehouse[(x, y)] = ch
                elif ch == "@":
                    robot = (x, y)
    width = len(lines[0])
    #    print_warehouse()

    for movement in movements:
        print("Move ", movement)
        if can_move(robot, movement):
            robot = (robot[0] + (movement == '>') - (movement == '<'),
                     robot[1] + (movement == 'v') - (movement == '^'))
        #print_warehouse()

    for location in warehouse:
        if warehouse[location] == 'O':
            score = location[1] * 100 + location[0]
            total += score

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
