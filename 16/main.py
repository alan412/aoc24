import sys
from heapq import heappop, heappush

maze = {}
width = 0
height = 0

dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

turn_cw = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
turn_ccw = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

LARGEST = 1_000_000_000_000_000_000

visited = {}

paths = []


def solve(start, dir, end):
    q = []
    high_score = LARGEST

    heappush(q, (0, start, dir, ""))
    while q:
        score, pos, dir, path = heappop(q)
        if score > high_score:
            break
        if (pos, dir) in visited and visited[(pos, dir)] < score:
            continue
        visited[(pos, dir)] = score
        if pos == end:
            print("Path found", path, score)
            paths.append(path)
            high_score = score
        (new_x, new_y) = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if (new_x, new_y) not in maze:
            heappush(q, (score + 1, (new_x, new_y), dir, path + "F"))
        heappush(q, (score + 1000, pos, turn_cw[dir], path + "R"))
        heappush(q, (score + 1000, pos, turn_ccw[dir], path + "L"))

    return high_score


def print_maze():
    for y in range(height):
        row = ""
        for x in range(width):
            row += maze.get((x, y), '.')
        print(row)


def num_tiles_on_any_path(start, paths):
    tiles = set()
    tiles.add(start)
    for path in paths:
        pos, dir = (start, 'E')
        for ch in path:
            if ch == 'F':
                pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
                tiles.add(pos)
            elif ch == 'R':
                dir = turn_cw[dir]
            elif ch == 'L':
                dir = turn_ccw[dir]
    return len(tiles)


def puzzle(filename):
    global height, width
    start = (0, 0)
    end = (0, 0)
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                maze[(x, y)] = '#'
            elif ch == 'E':
                end = (x, y)
            elif ch == 'S':
                start = (x, y)
    height = len(lines)
    width = len(line)
    print("Start:", start, " End:", end)
    print_maze()
    total = solve(start, 'E', end)
    total_pt2 = num_tiles_on_any_path(start, paths)
    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
