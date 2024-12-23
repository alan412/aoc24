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


# For each sequence [x, y, z, a] we store the buyer number and the amount of banannas
# If that sequence has already been stored for that buyer, then we don't bother
sequences = {}


class Buyer():

    def __init__(self, buyer_id, secret_number):
        self.buyer_id = buyer_id
        self.number = secret_number

    def calc_prices(self):
        self.prices = []
        self.changes = [0]
        last_cost = None
        number = self.number
        cost = number % 10
        self.prices.append(cost)
        last_cost = cost
        for i in range(2_000):
            number = next_number(number)
            cost = number % 10
            self.prices.append(cost)
            self.changes.append(cost - last_cost)
            last_cost = cost

    def store_sequences(self):
        for i in range(len(self.changes) - 3):
            sequence = tuple(self.changes[i:i + 4])
            if sequence in sequences:
                if (self.buyer_id in sequences[sequence]):
                    continue
                sequences[sequence][self.buyer_id] = self.prices[i + 3]
            else:
                sequences[sequence] = {self.buyer_id: self.prices[i + 3]}


buyers = []


def puzzle(filename):
    total = 0
    total_pt2 = 0

    lines = open(filename, 'r').read().split('\n')

    buyers = [(Buyer(buyer_id, int(line)))
              for buyer_id, line in enumerate(lines)]

    for buyer in buyers:
        buyer.calc_prices()
        buyer.store_sequences()

    max_bananas = 0
    for sequence in sequences:
        new_bananas = sum(sequences[sequence].values())
        if new_bananas > max_bananas:
            max_bananas = new_bananas
            print("New max", max_bananas, sequence)

    print("Part 1", total)
    print("Part 2", max_bananas)


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
