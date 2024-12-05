import sys

def isValid(rules, before, after):
    if before in rules:
        return after in rules[before]
    return False

def updateValid(rules, update):
    for before in range(0, len(update) - 1):
        for after in range(before + 1, len(update)):
            if not isValid(rules, update[before], update[after]):
                return False
    return True

def getMiddle(update):
    return update[len(update) // 2]
    
def puzzle(filename):
    rules = {}
    updates = []
    inRules = True
    total = 0
    for line in open(filename, 'r'):
        line = line.strip()
        if line == "":
            inRules = False
            continue
        if inRules:
            pages = line.split("|")
            before = int(pages[0])
            after = int(pages[1])
            if before in rules:
                rules[before].append(after)
            else: 
                rules[before] = [after]           
        else: 
            update = [int(x) for x in line.split(",")]
            updates.append(update)
    print(rules)
    print(updates)

    needsFixing = []
    for update in updates:
        if updateValid(rules, update):
            print("Valid", update)
            total += getMiddle(update)
        else:
            print("Invalid", update)
            needsFixing.append(update)

    print("Part 1", total)
    total_pt2 = 0
    for update in needsFixing:
        print("Fixing", update)
        for before in range(0, len(update) - 1):
            for after in range(before + 1, len(update)):
                if not isValid(rules, update[before], update[after]):
                    print("Swapping", update[before], update[after])
                    temp = update[before]
                    update[before] = update[after]
                    update[after] = temp
        print("Fixed", update)
        total_pt2 += getMiddle(update)
    print("Part 2", total_pt2)
        
        

if __name__=="__main__":
    lists = puzzle(sys.argv[1])