#Inputs:
#src = (0,0)
#dst = (3,3)
#Blocked = [(1,2),(2,2),(3,1)]
import random
global src
src = (0,0)
global dst
dst = (3,3)
global blocked
blocked = [(1,2),(2,2),(3,1)]
size = 4

global visited
visited = []
visited.append(tuple(src))
global valid_path
valid_path = []


def is_valid(x,y):
  #print("In valid check function: %s,%s" %(x,y))
  if x >= 0 and y >= 0 and x <= 3 and y <= 3:
    #print("Check 1")
    if (x,y) not in blocked:
      #print("Check 2")
      return True
  return False

global count_loop
count_loop = []

def travel(x,y,exclude=0):
  print("Visited: %s" %visited)
  print("Valid path: %s" %valid_path)
  count_loop.append('c')
  if len(count_loop) > 100:
    print("Will exit now")
    return -1
  direction = 0
  while True:
    direction = random.randint(1, 4)
    if direction != exclude: break
  print("Picked direction %s" %direction)
  #1 is left #2 is right #3 is top #4 is bottom
  # Check if you reached destination
  if (x,y) == dst:
    print("Entered this")
    return "reached"
  #Check if you are stuck in a Loop
  if direction == 1:
    if is_valid(x-1,y):
      #print("IS valid check passed in 1" )
      if (x-1,y) not in visited:
        visited.append(tuple((x-1,y)))
        print("Calling again with %s,%s" %(x-1,y))
        valid_path.append(tuple((x-1,y)))
        travel(x-1,y)
      else:
        travel(x,y)
    else:
      travel(x,y,exclude=1)
  elif direction == 2:
    if is_valid(x+1,y):
      #print("IS valid check passed in 2" )
      if (x+1,y) not in visited:
        visited.append(tuple((x+1,y)))
        print("Calling again with %s,%s" %(x+1,y))
        valid_path.append(tuple((x+1,y)))
        travel(x+1,y)
      else:
        travel(x,y)
    else:
      travel(x,y,exclude=2)
  elif direction == 3:
    if is_valid(x,y-1):
      #print("IS valid check passed in 3" )
      if (x,y-1) not in visited:
        visited.append(tuple((x,y-1)))
        print("Calling again with %s,%s" %(x,y-1))
        valid_path.append(tuple((x,y-1)))
        travel(x,y-1)
      else:
        travel(x,y)
    else:
      travel(x,y,exclude=3)
  else:
    if is_valid(x,y+1):
      #print("IS valid check passed in 4" )
      if (x,y+1) not in visited:
        visited.append(tuple((x,y+1)))
        print("Calling again with %s,%s" %(x,y+1))
        valid_path.append(tuple((x,y+1)))
        travel(x,y+1)
      else:
        travel(x,y)
    else:
      travel(x,y,exclude=4)

x1 = src[0]
y1 = src[1]

val = travel(x1,y1)
print(val)
