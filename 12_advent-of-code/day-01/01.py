"""
EXERCISE PROMPT: http://adventofcode.com/2025/day/1
"""

START_POS = 50

# option 1: good ol' for loop
# option 2: make a list [0] * 100 & +=1 each index landed at
# option 3: 

with open(filename, 'r') as f:
	# what do I need to do for input parsing?
	# 1. when I open a file & read from it, I get strings...
	# 2. I want to replace "L" with -, and "R" with nothing
	# 3. I want to cast those into integers
	dial = []
	for line in f.readlines():
		line = line.replace("L", "-").replace("R", "")
		dial.append(int(line))
