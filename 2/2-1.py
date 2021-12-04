import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "movements"
with open(os.path.join(dirname, "input.txt")) as movements_list:
  movements = [movements.split() for movements in movements_list]

def translateMovementToMath(movement, x, y):
  direction = movement[0]
  magnitude = int(movement[1])

  # i kind of see the submarine movement as traveling along a 2d graph
  # where the y-axis is inverted depth and the x-axis is forward movements
  if direction == 'down':
    y -= magnitude
  elif direction == "up":
    y += magnitude
  elif direction == 'forward':
    x += magnitude

  return x, y

def getProduct(movements):
  # it said we start at 0 depth and 0 horizontal movement
  x = 0
  y = 0

  for movement in movements:
    x, y = translateMovementToMath(movement, x, y)

  # return the product of end results because... it said so
  return abs(x * y)

print(getProduct(movements))
  
  