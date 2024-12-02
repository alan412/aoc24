import sys
import re

def puzzle(filename):
    list1 = []
    list2 = []
    pattern = r'(\d+)\s+(\d+)'
    for line in open(filename, 'r'):
        result = re.search(pattern, line)

        list1.append(int(result.group(1)))
        list2.append(int(result.group(2)))
    list1.sort()
    list2.sort()
    
    totalDistance = 0
    for pos in range(len(list1)):
        distance = abs(list2[pos] - list1[pos])
        totalDistance += distance
        print(list1[pos], list2[pos], distance, totalDistance)
    similarityScore = 0
    for pos in range(len(list1)):
        x = list1[pos]
        similarity = x * sum([y == x for y in list2])
        similarityScore += similarity
        print("Similarity", similarity, similarityScore)

if __name__=="__main__":
    lists = puzzle(sys.argv[1])