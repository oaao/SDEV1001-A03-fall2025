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

print("We're about to unpack an unknown series of positional arguments")
def variable_positional_arguments(*args):
	for arg in args:
		print(arg)


variable_positional_arguments(1, 2, 3)
print("or...")
variable_positional_arguments(1, 2, 3, 4, 5, 6)

a_tuple = (7, 8, 9)
variable_positional_arguments(*a_tuple)

"""
We can also do the same for keyword arguments, which are basically
dictionaries under the hood:
"""
print("\nWe're about to unpack an unknown series of keyword arguments")

def variable_keyword_arguments(**kwargs):
	for key, value in kwargs.items():
		print(f"Got value {value} for key {key}.")


variable_keyword_arguments(tree="ash", rock="igneous", water="tap")
variable_keyword_arguments(plant="madagascar palm", scarf="red")

a_dictionary = {"drink": "tea", "food": "oatmeal"}
variable_keyword_arguments(**a_dictionary)


"""
You can use both together! Just make sure positional args go before keyword args,
just like you'd have to order things anyway.
"""

def variable_args(*items, **options):
	print("\nItems Ordered:")
	for item in items:
		print(f"  - {item}")
	print("Options/Notes:")
	for key, value in options.items():
		print(f"  {key}: {value}")


variable_args(
	"55 burgers", "55 fries", "55 tacos", "55 pies", "55 drinks", "100 tater tots",
	drink="Coke", side_size="Large", drink_size="Large"
)
