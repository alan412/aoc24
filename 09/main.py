import sys

disk_map = {}
empties = {}
files = {}


def read_disk_map(line):
    file_id = 0
    disk_pos = 0
    free_space = False
    for digit in line:
        digit = int(digit)
        if free_space:
            empties[disk_pos] = digit
            disk_pos += digit
            free_space = False
            file_id += 1
        else:
            files[file_id] = (digit, disk_pos)
            for i in range(digit):
                disk_map[disk_pos + i] = file_id
            disk_pos += digit
            free_space = True


def compact():
    list_keys = list(disk_map.keys())
    end_of_list = -1
    for empty_region in empties:
        for i in range(empties[empty_region]):
            key = list_keys[end_of_list]
            if key > (empty_region + i):
                print("Moved ", key, " to ", empty_region + i)
                disk_map[empty_region + i] = disk_map[key]
                del disk_map[key]
            end_of_list -= 1


def compact_pt2():
    list_files = reversed(list(files.keys()))

    # For each file in list, can we move it to the left?
    for file_id in list_files:
        (file_size, start_pos) = files[file_id]
        empty_list = sorted(list(empties.keys()))
        for empty in empty_list:
            if empties[empty] >= file_size:
                if start_pos > empty:
                    print("Moving file ", file_id, " to ", empty)
                    for i in range(file_size):
                        disk_map[empty + i] = file_id
                        del disk_map[start_pos + i]
                    files[file_id] = (file_size, empty)
                    if (empties[empty] > file_size):
                        empties[empty + file_size] = empties[empty] - file_size
                    del empties[empty]
                    break


def calculate_check_sum():
    total = 0
    for key in disk_map:
        total += key * disk_map[key]
    return total


def puzzle(filename):
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    for line in lines:
        read_disk_map(line)

    # print(disk_map)
    # print(empties)
    # compact()
    # print("After compact:", disk_map)
    #total = calculate_check_sum()

    # print("Part 1", total)
    compact_pt2()
    total_pt2 = calculate_check_sum()
    # print("After compact:", disk_map)

    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
