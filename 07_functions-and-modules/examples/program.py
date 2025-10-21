# program.py

# I need an __init__.py in any directory I'm importing *from*,
# so that Python ingests it as a Python module

from importing_example import math_functions

print(
    math_functions.add(2, 3)
)

# the other thing I can do is import specific functions from a module (file)
# however, this is less advisable because you lose the namespace the function belongs to
# and potentially enter into conflict with identically named functions from other namespace

from importing_example.math_functions import add

print(
	add(1, 3)
)