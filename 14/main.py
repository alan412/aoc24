import sys
import re

tiles = [101, 103]
#tiles = [11, 7]


class Robot:

    def __init__(self, x, y, x_amt, y_amt):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.x_amt = x_amt
        self.y_amt = y_amt

    def move(self, num_times):
        self.x = (self.start_x + (self.x_amt * num_times)) % tiles[0]
        self.y = (self.start_y + (self.y_amt * num_times)) % tiles[1]

    def in_area(self, x1, y1, x2, y2):
        return x1 <= self.x <= x2 and y1 <= self.y <= y2

    def __repr__(self):
        return f"Robot({self.x}, {self.y}, {self.x_amt}, {self.y_amt})"


robots = []


def print_robots(sec):
    for robot in robots:
        robot.move(sec)

    screen = [['.' for _ in range(tiles[0])] for _ in range(tiles[1])]
    for robot in robots:
        if (screen[robot.y][robot.x] == '.'):
            screen[robot.y][robot.x] = '1'
        else:
            screen[robot.y][robot.x] = str(1 + int(screen[robot.y][robot.x]))
    for row in screen:
        print(''.join(row))


def calc_safety(sec):
    for robot in robots:
        robot.move(sec)

    mid_x = (tiles[0] // 2) - 1
    mid_y = (tiles[1] // 2) - 1

    quadrants = [[0, 0, mid_x, mid_y], [mid_x + 2, 0, tiles[0] - 1, mid_y],
                 [0, mid_y + 2, mid_x, tiles[1] - 1],
                 [mid_x + 2, mid_y + 2, tiles[0] - 1, tiles[1] - 1]]
    print(quadrants)
    quadrant_score = [0, 0, 0, 0]
    for robot in robots:
        if robot.in_area(quadrants[0][0], quadrants[0][1], quadrants[0][2],
                         quadrants[0][3]):
            quadrant_score[0] += 1
        elif robot.in_area(quadrants[1][0], quadrants[1][1], quadrants[1][2],
                           quadrants[1][3]):
            quadrant_score[1] += 1
        elif robot.in_area(quadrants[2][0], quadrants[2][1], quadrants[2][2],
                           quadrants[2][3]):
            quadrant_score[2] += 1
        elif robot.in_area(quadrants[3][0], quadrants[3][1], quadrants[3][2],
                           quadrants[3][3]):
            quadrant_score[3] += 1

    return quadrant_score[0] * quadrant_score[1] * quadrant_score[
        2] * quadrant_score[3]


def puzzle(filename):
    global robots
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')

    for line in lines:
        result = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)

        robots.append(
            Robot(int(result.group(1)), int(result.group(2)),
                  int(result.group(3)), int(result.group(4))))

    print("Part 1", calc_safety(100))

    for sec in range(101 * 103):
        print(sec)
        print_robots(sec)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
