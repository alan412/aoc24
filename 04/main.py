import sys

def textCrossMAS(lines, x, y):
    try:
       if(x - 1 < 0 or y - 1 < 0):
           return False
       if lines[y][x] != 'A':
           return False
       crossOne = lines[y-1][x-1] + lines[y+1][x+1]
       crossTwo = lines[y-1][x+1] + lines[y+1][x-1]
       if (crossOne == 'MS' or crossOne == 'SM') and (crossTwo == 'MS' or crossTwo == 'SM'):
          print("Found crossMAS:", x, y)
          return True
    except:           
        # print("Exception-v")
        return False
    # print("Not Found XMAS at ", x, y)
    return False
    

def testXMAS(lines, x, y, xdir, ydir):
    try:
       if(x + xdir*3 < 0 or y + ydir*3 < 0):
           return False
       if lines[y][x] == 'X' and \
          lines[y + ydir*1][x + xdir*1] == 'M' and \
          lines[y + ydir*2][x + xdir*2] == 'A' and \
          lines[y + ydir*3][x + xdir*3] == 'S':
            print("Found XMAS:", x, y, xdir, ydir)
            return True
    except:           
        # print("Exception-v")
        return False
    # print("Not Found XMAS at ", x, y, xdir, ydir)
    return False
    
def puzzle(filename):
    total=0
    total_pt2 = 0
    lines = open(filename, 'r').read().split('\n')

    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if textCrossMAS(lines, x, y):
                total_pt2 += 1
            if testXMAS(lines, x, y, 1, 0):
                total += 1
            if testXMAS(lines, x, y, 0, 1):
                total += 1
            if testXMAS(lines, x, y, -1, 0):
                total += 1
            if testXMAS(lines, x, y, 0, -1):
                total += 1
            if testXMAS(lines, x, y, 1, 1):
                total += 1
            if testXMAS(lines, x, y, 1, -1):
                total += 1
            if testXMAS(lines, x, y, -1, 1):
                total += 1
            if testXMAS(lines, x, y, -1, -1):
                total += 1     
    print("Part 1", total)
    print("Part 2", total_pt2)
        
if __name__=="__main__":
    lists = puzzle(sys.argv[1])