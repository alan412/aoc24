import sys
import functools


@functools.lru_cache(maxsize=None)
def solve(stone, left):
    if left == 0:
        return 1
    if stone == "0":
        return solve("1", left - 1)
    if len(stone) % 2 == 0:
        middle = len(stone) // 2
        return solve(str(int(stone[:middle])), left - 1) + solve(
            str(int(stone[middle:])), left - 1)
    return solve(str(2024 * int(stone)), left - 1)


def blink(stones, times):
    return sum(solve(stone, times) for stone in stones)


def puzzle(filename):
    total = 0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')
    stones = lines[0].split(' ')

    print("Part 1", blink(stones, 25))
    print("Part 2", blink(stones, 75))


if __name__ == "__main__":
    lists = puzzle(sys.argv[1])
