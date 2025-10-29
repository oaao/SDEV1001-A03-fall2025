"""
We can write functions to accept an unknown number of arguments.
Can you? Yes. Should you? Depends.

Normally, if we wanted to pass a series as an argument, we'd do:
"""
print("We're about to print numbers from a single iterable argument")
def some_func(arguments):
	for arg in arguments:
		print(arg)

some_func(
	[1, 2, 3]  # this is a single argument
)

"""
But what if we wanted an implementation that was fully agnostic about the
number (or type!) of arguments provided?

In order to do this, we pass an unpacked series as positional arguments,
which is basically any iterable with an asterisk in front of it.

A leading asterisk like this in Python (in front of any iterable) means,
"unpack this series into separate terms".
"""

print("We're about to unpack an unknown series of arguments")
def variable_positional_arguments(*args):
	for arg in args:
		print(arg)


variable_positional_arguments(1, 2, 3)
print("or...")
variable_positional_arguments(1, 2, 3, 4, 5, 6)



