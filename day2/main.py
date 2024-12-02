import sys

def is_safe(report):
    ascending = int(report[0]) < int(report[1])
    for pos in range(0, len(report) - 1):
        diff = int(report[pos +1]) - int(report[pos])
        if not ascending:
            diff = -diff

        if diff < 1 or diff > 3:
            print("Not safe:", report, pos, diff, ascending)
            return False
    print("Safe", report)
    return True

def is_safe_pt2(report):
    if is_safe(report):
        return True
    num_reports = len(report)
    i = 0
    while i < num_reports:
        if i == 0:
            new_report = report[1:]
        else:
            new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
        i += 1
    print("Unsafe", report)
    return False

def puzzle(filename):
    numSafe = 0
    for line in open(filename, 'r'):
        if is_safe_pt2(line.split(" ")):
            numSafe += 1
    print("Total Safe", numSafe)

if __name__=="__main__":
    lists = puzzle(sys.argv[1])