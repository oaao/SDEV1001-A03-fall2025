"""
EXERCISE PROMPT: http://adventofcode.com/2025/day/1
"""

INPUT_FILE = "sample"

# option 1: good ol' for loop
# option 2: make a list [0] * 100 & +=1 each index landed at
# option 3: i don't have to resolve the range at all! i just need... x % 100 = 0

with open(INPUT_FILE, 'r') as f:
	# what do I need to do for input parsing?
	# 1. when I open a file & read from it, I get strings...
	# 2. I want to replace "L" with -, and "R" with nothing
	# 3. I want to cast those into integers
	# 4. If I can write a for loop, I can write a list expression!
	#   The easy mental cheat code for writing a list expression is..
    #   ... take the end-term in the for loop, put it at the start, write the rest
	dial = [
		int(line.replace("L", "-").replace("R", ""))
		for line in f.readlines()
	]


position = 50  # dial starts at 50
zeros = 0
# option 3: we just care about positions we land on
#           that are fully divisible by 100
for instruction in dial:
	# print(f"Starting at {position},")
	position += instruction
	# print(f"Updating position to {position} (with step: {instruction}")
	if position % 100 == 0:
		print("Landed on a zero!")
		zeros += 1

print(f"part A solution: {zeros}")

