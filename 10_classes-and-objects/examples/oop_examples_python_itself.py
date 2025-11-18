# OK, so now that you have the basics of OOP and classes down,
# let's look at how classes & OOP principles build the Python language itself!
# This is an advanced example & not required for exams etc.

# 0. I *strongly* encourage you to read the explanation of Python's data model,
#    whether for learning how to use Python, or learning how it works under the hood:
#      https://docs.python.org/3/reference/datamodel.html


# 1. In Python, (almost) everything is an object!
#    This is the base class for pretty much everything else.
#    You may have also heard me call these 'silly' containers.
#
#    Every Python *type* is a class instance of *object*, and *object* is a *class*! 
#    (All usable types are classes, really.)
class SomeClass:
	pass

def some_func():
	pass

import math

# these are all *instances* of their *type*!
various_python_objects = [
	1.00,                        # <-- float   : 1.00 is an instance of float
	True,                        # <-- boolean : True is an instance of bool
	SomeClass,                   # class definitions AND class instances are object instances,
	SomeClass(),
	some_func,                   # and functions too!
	some_func(),                 # <-- returns None... even Python's null type is an object!
]

for thing in various_python_objects:
	print(f"{isinstance(thing, object)}: {thing} is an instance of object.")


# ---------------------------------------------------------------------------------------
print("\n2. Let's work backwards! Remember how I keep showing you booleans are really just integers under the hood?")
print(f"{0 == False}: 0 == False")
print(["first element", "second element"][False])
print(["first element", "second element"][True])

# Well, let's verify that.
type(True)       # <class 'bool'> ... True is an instance of bool
type(bool)       # <class 'type'> ... bool is a class definition that inherits from type
type(SomeClass)  # <class 'type'> ... *every* class definition you write becomes a type!

# When you write a class in Python, it's a new type!!!

# But wait.. didn't you say bool -> int -> type -> object? Where's the int?
type(bool)                # <class 'type'> ... type() shows you what *kind* of Python object it is, not whether B inherits from A.
isinstance(False, int)    # True           ... isinstance(instance, type) checks whether an *instance* inherits from a base *type*.

# Or in other words...
isinstance(3, type)       # False ... 3 is an instance of int, but
isinstance(int, type)     # True  ... the integer type itself is an instance/inheritor of type
isinstance(type, object)  # True  ... and type itself is an instance/inheritor of object


# And what's an object? Well, at that point you start getting into the C code that Python compiles down to...
# These are *fantastic* reads (especially the second one!) if you have the time.
# TYPE OBJECTS: https://docs.python.org/3/c-api/typeobj.html
# OBJECTS:      https://docs.python.org/3/reference/datamodel.html


# The closest built-in tools to inspect inheritance hierarchy are:
# a)
bool.__mro__        # (<class 'bool'>, <class 'int'>, <class 'object'>)
# ^ shows (more or less) the inheritance chain, going "upwards" in the hierarchy.
#   "MRO" stands for Method Resolution Order ... see Combination(A, B, C) example in oop_examples_basic.py
# b)
int.__subclasses__()  # [<class 'bool'>, <enum 'IntEnum'>, <flag 'IntFlag'>, <class 're._constants._NamedIntConstant'>, <class 're._ZeroSentinel'>]
# ^ shows which *subclasses* a given class is a *base class* for.

# Feeling brave? Run the file!
# The output doesn't even account for a lot of intermediary types that exist to build out the Python type system, but can't be instantiated directly!
print("\nWhat are all the things that *directly* inherit from Python's 'object'?")
for sc in object.__subclasses__():
	print(sc)




# ---------------------------------------------------------------------------------------
# 3. OK, now let's build it back up from scratch then, starting with object.

print("\n3. First, let's see what methods & attributes are already packaged into object!")
print(dir(object))
print(
	"\n^ I'll go over some of these:\n"
	"  - __class__: The type of class this object is an instance of - try dir(object.__class__) !\n"
	"  - __dir__():   Our dir() friend! This method contains logic for listing an object's attributes/methods without values.\n"
	# ^ basically, dir(object) == sorted(list(object.__dict__.keys()))
	"  - __eq__():    Equality comparison operator. Dictates happens when you write X == Y.\n"
	"  - other comparison operators:\n"
	"      - gt/lt are greater than/less than (X > Y, X < Y)\n"
	"      - ge/le are their -or-equal-to variants (X >= Y, X <= Y)\n"
	"      - ne is not equal to (X != Y)\n"
	# ^ e.g. when you do X > Y, what 'really' runs is X.__ge__(Y) !
	"  - our familiar friends __init__(), __repr__(), and __str__()!"  
)

# OK, according to bool.__mro__, the next thing up is an int.
# Let's write a function you can use to look at only the new methods/attributes:
def diff_dir(test_class, reference_class):
	# I'll use sets, not because I need deduplication, but because they make diffing super easy:
	return set(dir(test_class)).difference(set(dir(reference_class)))


print("\nWhat methods/attributes are new in 'int' after inheriting from 'object'?")
# Keep in mind, this only shows new methods/attributes! Existing ones may get overridden in the child class.
print(diff_dir(int, object))
# Note how integers already implement a __bool__ function - a way to resolve a value as truthy/falsey in conditional logic.
# 

print("\nOK, and what's new in a 'bool' that isn't in an 'int'?")
# Keep in mind, this only shows new methods/attributes! Existing ones may get overridden in the child class.
print(diff_dir(bool, int))
print(
	"\nWhoa! So there are no new methods/attributes!"
	"\nBut there's probably a lot of overridden logic to accommodate other data types, e.g. bool(\"\") == False"
)

# Here's a *very* simple example of what that means/looks like, *without* logic that accommodates other data types:
class simpleBool(int):
	# leaving out a WHOLE lot of comparison methods/logic...
	def __repr__(self):
		return 'False' if self == 0 else 'True'


# I told you it was just silly containers!
