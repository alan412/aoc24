import sys
from collections import deque
from functools import cache
from itertools import pairwise

N_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}
D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}
PADS = [N_PAD, D_PAD]


def bfs(start, end, pad):
    queue = deque([(start, "")])
    visited = {start}
    shortest = None
    shortest_paths = []
    while queue:
        node, path = queue.popleft()
        if node == end:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                shortest_paths.append(path + "A")
            continue
        if shortest and len(path) >= shortest:
            continue
        for neighbor, direction in pad[node]:
            visited.add(neighbor)
            queue.append((neighbor, path + direction))
    return shortest_paths


@cache
def dfs(sequence, level, which_pad):
    result = 0
    pad = PADS[which_pad]
    sequence = "A" + sequence
    for start, end in pairwise(sequence):
        paths = bfs(start, end, pad)
        if level == 0:
            result += min(map(len, paths))
        else:
            result += min(dfs(path, level - 1, 1) for path in paths)
    return result


def puzzle(filename):
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    for line in lines:
        line_numeric = int(line[:-1])
        num_moves = dfs(line, 2, 0)
        complexity = line_numeric * num_moves
        print("Complexity", line_numeric, num_moves, complexity)
        total += complexity

    print("Part 1", total)
    total_pt2 = 0
    for line in lines:
        line_numeric = int(line[:-1])
        num_moves = dfs(line, 25, 0)
        complexity = line_numeric * num_moves
        print("Complexity", line_numeric, num_moves, complexity)
        total_pt2 += complexity
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
