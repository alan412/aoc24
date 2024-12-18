import sys
from heapq import heappop, heappush

max_side = 6
memory_size = 12
max_x = max_side
max_y = max_side


def make_maze(memory, num_steps):
    maze = {}
    for step in range(num_steps):
        maze[memory[step]] = '#'
    return maze


def print_maze(maze):
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            row += maze.get((x, y), '.')
        print(row)


def solve2(start, end, maze):
    end_row, end_col = max_y, max_x
    visited = {}
    q = []
    heappush(q, (0, start))
    while q:
        score, pos = heappop(q)
        if pos == end:
            return score
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):  # Adjacent squares
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and (
                    new_x, new_y) not in maze:
                if (new_x, new_y) not in visited:
                    visited[(new_x, new_y)] = score + 1
                    heappush(q, (score + 1, (new_x, new_y)))
    return -1  # No path found


LARGEST = 1_000_000


def puzzle(filename):
    total = 0
    total_pt2 = 0
    memory = []
    lines = open(filename, 'r').read().split('\n')
    for line in lines:
        (x, y) = line.split(',')
        memory.append((int(x), int(y)))

    maze = make_maze(memory, memory_size)
    print_maze(maze)
    # path = astar((0, 0), (max_x, max_y), maze)
    # total = len(path) - 1
    # print(path, total)
    #total = solve((0, 0), (max_x, max_y), maze)
    total = solve2((0, 0), (max_x, max_y), maze)
    i = 1
    while (total != -1):
        maze = make_maze(memory, memory_size + i)
        print("Added ", memory[memory_size + i])
        total = solve2((0, 0), (max_x, max_y), maze)
        i += 1

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
