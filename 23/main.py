import sys

connections = {}

triplets = set()


# If computer has connection to c1, and c1 to c2, and c2 to computer then a loop
def find_triplets(computer):
    for c1 in connections[computer]:
        for c2 in connections[c1]:
            if computer in connections[c2]:
                triplets.add(tuple(sorted([computer, c1, c2])))


explored = set()
max_lan_size = -1


def find_connected(computer, visited, index):
    global max_lan_size
    node_list = connections[computer]
    for i in range(index, len(node_list)):
        node = node_list[i]
        if node in explored:
            continue
        if not all(node in connections[n] for n in visited):
            continue
        visited.append(node)
        find_connected(computer, visited, i + 1)
        if len(visited) > max_lan_size:
            max_lan_size = len(visited)
            print("New max lan size", max_lan_size,
                  {','.join(x for x in sorted(visited))})
        visited.remove(node)


def puzzle(filename):
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')

    for line in lines:
        computers = line.split('-')
        if computers[0] not in connections:
            connections[computers[0]] = []
        connections[computers[0]].append(computers[1])
        if computers[1] not in connections:
            connections[computers[1]] = []
        connections[computers[1]].append(computers[0])

    print(connections)
    for computer in connections:
        find_triplets(computer)
    print(len(triplets), triplets)

    total = 0
    for triplet in triplets:
        if triplet[0].startswith("t") or triplet[1].startswith(
                "t") or triplet[2].startswith("t"):
            total += 1

    print("Part 1", total)
    for computer in connections:
        find_connected(computer, [computer], 0)
        explored.add(computer)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
