import sys
import functools

topo_map = []
max_x = 0
max_y = 0


@functools.lru_cache(maxsize=None)
def find_path(x, y):
    end_pts = set()
    current_height = topo_map[y][x]

    if current_height == 9:
        end_pts.add((x, y))
        return end_pts
    if x > 0:
        if topo_map[y][x - 1] == current_height + 1:
            end_pts.update(find_path(x - 1, y))
    if y > 0:
        if topo_map[y - 1][x] == current_height + 1:
            end_pts.update(find_path(x, y - 1))
    if x < (max_x - 1):
        if topo_map[y][x + 1] == current_height + 1:
            end_pts.update(find_path(x + 1, y))
    if y < (max_y - 1):
        if topo_map[y + 1][x] == current_height + 1:
            end_pts.update(find_path(x, y + 1))
    return end_pts


def find_paths():
    total = 0
    for y in range(max_y):
        for x in range(max_x):
            if topo_map[y][x] == 0:
                end_pts = find_path(x, y)
                print(
                    f"Found {len(end_pts)} end points at {x}, {y}: {end_pts}")
                total += len(end_pts)
    return total


def puzzle(filename):
    global max_x, max_y, topo_map
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    max_y = len(lines)
    max_x = len(lines[0])
    for line in lines:
        topo_map.append([int(x) for x in line.strip()])

    total = find_paths()
    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
