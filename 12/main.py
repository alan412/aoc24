import sys

plants = {}
already_placed = []
max_x = 0
max_y = 0


def calculate_perimeter(region):
    # Perimeter is four times the number of squares in the region minus the number of squares that are next to another square in the region
    perimeter = 4 * len(region)
    for x, y in region:
        if (x + 1, y) in region:
            perimeter -= 1
        if (x - 1, y) in region:
            perimeter -= 1
        if (x, y + 1) in region:
            perimeter -= 1
        if (x, y - 1) in region:
            perimeter -= 1
    return perimeter


def next_to(x1, y1, x2, y2):
    return (x1 == x2 - 1 and y1 == y2) or (x1 == x2 + 1 and y1 == y2) or (
        x1 == x2 and y1 == y2 - 1) or (x1 == x2 and y1 == y2 + 1)


def get_region(lines, plant, x, y):
    region = []
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return region
    if lines[y][x] != plant or already_placed[y][x]:
        return region
    region = [(x, y)]
    already_placed[y][x] = True
    region.extend(get_region(lines, plant, x + 1, y))
    region.extend(get_region(lines, plant, x - 1, y))
    region.extend(get_region(lines, plant, x, y + 1))
    region.extend(get_region(lines, plant, x, y - 1))

    return region


def split_into_plant_regions(lines):
    global max_x, max_y, already_placed
    max_x = len(lines[0])
    max_y = len(lines)
    already_placed = [[False for _ in range(max_x)] for _ in range(max_y)]
    print(already_placed)
    print(lines)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if not already_placed[y][x]:
                plant = lines[y][x]
                region = get_region(lines, plant, x, y)
                if plant not in plants:
                    plants[plant] = []
                plants[plant].append(region)


def puzzle(filename):
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    split_into_plant_regions(lines)
    print(plants)
    for plant in plants:
        for region in plants[plant]:
            area = len(region)
            perimeter = calculate_perimeter(region)
            price = area * perimeter
            print("Region ", plant, "Area", area, "Perimeter", perimeter,
                  "Price", price)
            total += price

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
