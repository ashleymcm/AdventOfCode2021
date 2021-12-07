import os, sys

# i hate that i need this when i'm on my windows machine
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

# loop through input rows, or "lines"
with open(os.path.join(dirname, "input.txt")) as lines_list:
  lines = [lines.rstrip().split(' -> ') for lines in lines_list]

print(lines)