import sys
from heapq import heappop, heappush

width = 0
height = 0


def solve(start, end, maze):
    visited = {}
    q = []
    heappush(q, (0, start, [start]))
    while q:
        score, pos, path = heappop(q)
        if pos == end:
            return path
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):  # Adjacent squares
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if (new_x, new_y) not in maze:
                if (new_x, new_y) not in visited:
                    visited[(new_x, new_y)] = score + 1
                    heappush(q, (score + 1,
                                 (new_x, new_y), path + [(new_x, new_y)]))
    return []  # No path found]


def print_maze(maze):
    for y in range(height):
        row = ""
        for x in range(width):
            row += maze.get((x, y), '.')
        print(row)


def find_cheats2(path, maze):
    cheats = [(abs(x1 - x) + abs(y1 - y), m) for n, (x, y) in enumerate(path)
              for m, (x1, y1) in enumerate(path[n + 102:])]
    return cheats


def find_cheats(path, maze):
    cheats = {}
    # Look for positions that could be 2 apart but have a wall in the middle
    for index, pos in enumerate(path):
        x, y = pos
        for dx1, dy1 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (x + dx1, y + dy1) not in maze:
                continue
            for dx2, dy2 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (dx2, dy2) == (0, 0):
                    continue
                new_x, new_y = x + dx1 + dx2, y + dy1 + dy2
                for index2, pos2 in enumerate(path[index + 1:]):
                    if (new_x, new_y) == pos2:
                        saves = index2 - 1
                        if saves <= 0:
                            continue
                        print("Found a cheat from ", x, y, " to ", new_x,
                              new_y, "saves", saves)
                        if saves not in cheats:
                            cheats[saves] = []
                        cheats[saves].append((x, y, new_x, new_y))
                        break
    return cheats


def puzzle(filename):
    global height, width
    start = (0, 0)
    end = (0, 0)
    total = 0
    total_pt2 = 0
    maze = {}

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
    print_maze(maze)
    path = solve(start, end, maze)
    #cheats = find_cheats(path, maze)
    #for cheat in dict(sorted(cheats.items())):
    #    print("Cheat", cheat, len(cheats[cheat]))
    #    if cheat >= 100:
    #        total += len(cheats[cheat])
    cheats = find_cheats2(path, maze)
    total = sum(d == 2 for d, _ in cheats)
    total_pt2 = sum(d <= min(20, m + 2) for d, m in cheats)

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
