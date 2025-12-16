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
	# 4. If I can write a for loop, I can write a list expression!
	#   The easy mental cheat code for writing a list expression is..
    #   ... take the end-term in the for loop, put it at the start, write the rest
	dial = [
		int(
			line.replace("L", "-").replace("R", "")
		)
		for line in f.readlines()
	]


	dial = []
	for line in f.readlines():
		line = line.replace("L", "-").replace("R", "")
		dial.append(int(line))
