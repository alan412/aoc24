import sys


def mix(x, y):
    return x ^ y


def prune(number):
    return number % 16777216


def next_number(number):
    next_number = prune(mix(number * 64, number))
    next_number = prune(mix(int(next_number / 32), next_number))
    next_number = prune(mix(next_number * 2048, next_number))
    return next_number


def get_number(starting_number, sequence_number):
    number = starting_number

    for i in range(sequence_number):
        number = next_number(number)
    #number = get_number(next_num, sequence_number - 1)

    return number


buyers = []


def puzzle(filename):
    total = 0
    total_pt2 = 0

    lines = open(filename, 'r').read().split('\n')

    buyers = [(int(line)) for line in lines]

    for buyer in buyers:
        number = get_number(buyer, 2_000)
        total += number
        print("Buyer", buyer, "Number", number)

    print("Part 1", total)
    print("Part 2", total_pt2)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
