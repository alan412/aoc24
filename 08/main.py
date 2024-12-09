import sys

antennas = {}


def get_check_coords(x, y, antenna_x, antenna_y):
    check_y = antenna_y + (antenna_y - y) * 2
    check_x = antenna_x + (antenna_x - x) * 2
    return check_x, check_y


def in_bounds(x, y, max_x, max_y):
    return x >= 0 and x <= max_x and y >= 0 and y <= max_y


def look_for_antenna(antenna_list, antenna_pt, direction, max_x, max_y):
    numSteps = 1
    while True:
        antinode_x = antenna_pt[0] + direction[0] * numSteps
        antinode_y = antenna_pt[1] + direction[1] * numSteps

        if not in_bounds(antinode_x, antinode_y, max_x, max_y):
            break

        antenna_x = antenna_pt[0] - direction[0] * numSteps
        antenna_y = antenna_pt[1] - direction[1] * numSteps

        if not in_bounds(antenna_x, antenna_y, max_x, max_y):
            break

        if (antenna_x, antenna_y) in antenna_list:
            print("Found", antenna_pt, antenna_x, antenna_y, direction,
                  numSteps)
            return (antinode_x, antinode_y)
        else:
            print("Not found", antenna_list, antenna_x, antenna_y)
        numSteps += 1
    return None


def calculate_antinodes(antenna_list, max_x, max_y):
    antinodes = []

    key_list = list(antenna_list.keys())
    for i in range(0, len(antenna_list)):
        for j in range(0, len(antenna_list)):
            if i == j:
                continue
            diff = (key_list[i][0] - key_list[j][0],
                    key_list[i][1] - key_list[j][1])
            print("Diff", diff)
            antinode = (key_list[i][0] + diff[0], key_list[i][1] + diff[1])
            if in_bounds(antinode[0], antinode[1], max_x, max_y):
                antinodes.append(antinode)

    return antinodes


def calculate_antinodes_pt2(antenna_list, max_x, max_y):
    antinodes = []

    key_list = list(antenna_list.keys())
    for i in range(0, len(antenna_list)):
        for j in range(0, len(antenna_list)):
            if i == j:
                continue
            diff = (key_list[i][0] - key_list[j][0],
                    key_list[i][1] - key_list[j][1])
            print("Diff", diff)
            numSteps = 1
            while True:
                antinode = (key_list[i][0] + diff[0] * numSteps,
                            key_list[i][1] + diff[1] * numSteps)
                if not in_bounds(antinode[0], antinode[1], max_x, max_y):
                    break
                antinodes.append(antinode)
                numSteps += 1
            numSteps = -1
            while True:
                antinode = (key_list[i][0] + diff[0] * numSteps,
                            key_list[i][1] + diff[1] * numSteps)
                if not in_bounds(antinode[0], antinode[1], max_x, max_y):
                    break
                antinodes.append(antinode)
                numSteps -= 1
    return antinodes


def puzzle(filename):
    total = 0
    antinodes = set()
    lines = open(filename, 'r').read().split('\n')

    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1

    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            antenna = lines[y][x]
            if antenna != ".":
                if antenna not in antennas:
                    antennas[antenna] = {}
                antennas[antenna][(x, y)] = antenna
    print(antennas)
    for antenna in antennas:
        antinodes.update(calculate_antinodes(antennas[antenna], max_x, max_y))

    print("Part 1", len(antinodes), antinodes)
    antinodes = set()
    for antenna in antennas:
        antinodes.update(
            calculate_antinodes_pt2(antennas[antenna], max_x, max_y))
    print("Part 2", len(antinodes), antinodes)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
