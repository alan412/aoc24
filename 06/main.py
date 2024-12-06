import sys

mapLocations = {}

class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = "UP"
        self.locations ={(x, y): True}
    def next_spot(self):
        if self.dir == "UP":
          return(self.x, self.y - 1)
        elif self.dir == "DOWN":
          return(self.x, self.y + 1)
        elif self.dir == "LEFT":
          return(self.x - 1, self.y)
        elif self.dir == "RIGHT":
          return(self.x + 1, self.y)
    def turn_right(self):
        if self.dir == "UP":
          self.dir = "RIGHT"
        elif self.dir == "RIGHT":
          self.dir = "DOWN"
        elif self.dir == "DOWN":
          self.dir = "LEFT"
        elif self.dir == "LEFT":
          self.dir = "UP"
    def move(self):
        self.x, self.y = self.next_spot()
        if (self.x, self.y) not in self.locations:
           self.locations[(self.x, self.y)] = True
    def num_visited(self):
       return len(self.locations)
       
def puzzle(filename):
  startingGuard = None
  maxY = 0
  maxX = 0
  for y, line in enumerate(open(filename, 'r')):
      line = line.strip()
      for x, char in enumerate(line):
          if char == '#':
              mapLocations[(x, y)] = True
          elif char == '^':
              startingGuard = Guard(x, y)
          maxX = max(maxX, x)
          maxY = max(maxY, y)
  inMap = True
  while inMap:
     (new_x, new_y) = startingGuard.next_spot()
     if new_x < 0 or new_x > maxX or new_y < 0 or new_y > maxY:
       inMap = False
     elif (new_x, new_y) in mapLocations:
            startingGuard.turn_right()
     else:
        startingGuard.move()          
  print("Part 1", startingGuard.num_visited())

if __name__=="__main__":
    lists = puzzle(sys.argv[1])