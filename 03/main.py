import sys
import re

def puzzle(filename):
    total=0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    enabled = True
    for line in open(filename, 'r'):
        matches = re.findall(pattern, line)
        for match in matches:
            results = re.search(r"mul\((\d+),(\d+)\)", match)
            if enabled and results:
              score = int(results.group(1)) * int(results.group(2))
              total += score
              print(score, total)
            if not results:
                results = re.search(r"do\(\)", match)
                if results:
                    enabled = True
                    print("enabled")
                else:
                    results = re.search(r"don't\(\)", match)
                    if results:
                        enabled = False
                        print("disabled")
if __name__=="__main__":
    lists = puzzle(sys.argv[1])