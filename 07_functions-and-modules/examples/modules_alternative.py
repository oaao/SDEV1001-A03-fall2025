import math  # this imports the math module from Python's standard library

print(
	math.factorial(5)  # now I can call functions from it!
)


# or, I can import those functions directly, but then I lose explicit track
# of where they came from
from math import factorial

print(factorial(5))
