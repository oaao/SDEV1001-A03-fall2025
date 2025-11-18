# 1. First, let's define a Car class
# ---------------------------------------------------------------
class Car:

	# every single Car instance will have .wheels = 4
	# both the class definition: Car.wheels   ->  4
	# and any instances:         Car().wheels ->  4  
	# because it's being set directly on the class,
	# not in the constructor
	wheels = 4

	def __init__(self, make, model, year):
		# in the constructor, we set attributes of the new Car() instance
		# by assigning values to self.some_property
		# then, once we make the car instance, we can access those properties!
		# however, the class definition will not have any of these attributes
		self.make = make
		self.model = model
		self.year = year

	def __repr__(self):
		# this determines how the instance 'displays' as text in terminal/REPL
		return f"Car<{self.year} {self.make} {self.model}>"

	def __str__(self):
		# this determines how the instance 'displays' when cast as/into a string
		return f"{self.make} {self.model}, {self.year}"


# 2. Create an instance of the class by passing the necessary params to its constructor.
# ---------------------------------------------------------------
#     -> you can pass params here the same way you would a function, including
#        *unpacked_iterables and **unpacked_dictionaries!
car1 = Car("Toyota", "Corolla", 1990)

values = ("Renault", "Clio", 2004)
car2 = Car(*values)

d = {"make": "Toyota", "model": "Celica GTS", "year": 2002}
car3 = Car(**d)
# remember double-underscore ("dunder") methods? Try car3.__dict__ !


# 3. Class attributes can have any type, including collections/lists!
# ---------------------------------------------------------------
class Garage:

	# I'm not going to pass any arguments to the constructor
	def __init__(self):
		# when a new Garage() instance is created, it's simply
		# an instance with some_garage.cars as an empty list
		self.cars = []

	def add_car(self, car):
		self.cars.append(car)
		print(f"Successfully added: {car}")

	def list_cars(self):
		print("\nWelcome to MTV Cribs, brokeys, here's what's in my garage")
		for i, car in enumerate(self.cars, start=1):
			print(f"{i}: {car}")


# 4. Let's make a garage, and add some of those cars!
# ---------------------------------------------------------------
garage = Garage()
garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)
garage.add_car(Car("Harley Davidson", "Edgelord", 2001))

garage.list_cars()



# 5. BONUS: Let's take a look at some of those double-underscore ("dunder") methods
#           we've been looking at, so we can do fancy things with our classes! 
# ---------------------------------------------------------------


# First, we'll inherit from Garage -- this gives us access to everything in Garage,
# plus anything we're adding/overriding! 
# 
# i.e. we don't need to rewrite __init__, add_cars, list_cars because they're already built in.
class FancyGarage(Garage):

	def __init__(self, cars=None):
		# ^ since Garage already has an __init__ method, this is called 'overriding'.
		# If we didn't do this, Garage.__init__() would run when we make a FancyGarage instance.
		# By overriding the method, that won't happen, because we're *replacing* that method.

		super().__init__()
		# ^ However, what if you *wanted* to set things up with the __init__() of our base class first?
		# This is how! super() refers to the parent class, so we're calling its constructor first.
		# This way, we end up with an empty self.cars attribute, *and then* can do other stuff.
		# If the parent class's __init__() method took arguments, we would pass those in too.

		# now that we have our empty cars list from calling the __init__() of the parent class,
		# we can just chuck the cars param passed to this init__() function into that list,
		# and start with some cars if they're supplied to the constructor.
		if cars:
			self.cars.extend(cars)

	def __add__(self, garage):
		# by implementing __add__, we can write logic to let us combine garages 
		# just using x + y! For example, you can add lists together this way because
		# the list type is a class that has a specifically written __add__() method.
		if not isinstance(garage, Garage):
			# ^ we *could* check for type(self) == type(garage).
			#   -> However, isinstance(some_instance, some_type) checks the entire inheritance
			#      chain of the class, e.g. isinstance(True, int).
			#      This lets us add both FancyGarage and Garage instances to our current instance,
			#      since we're really just merging their .cars lists together.
			raise TypeError(
				f"Addition unsupported between FancyGarage and {type(garage)}."
			)
		else:
			# The important thing here is that __add__ *needs* a return value.
			self.cars.extend(garage.cars)  # add the new cars to self.cars list
			return self                    # return this instance, now that it has the new cars


# let's try it!
car4 = Car("Lotus", "Elise", 2007)
car5 = Car("SSC", "Tuatara", 2021)
fg1 = FancyGarage([car4, car5])
print("\n Before merging, mg1 contains:")
fg1.list_cars()

car6 = Car("Gibbs", "Aquada", 2003)
fg2 = FancyGarage([car6,])  # I use trailing commas for single-element series; not required!

print(f"\n Merging mg1 and mg2...")
fg3 = fg1 + fg2   # this calls our __add__ method, i.e. mg1.__add__(mg2) !
fg3.list_cars()

print("\nBecause we type-checked with isinstance(), we can also add Garages to FancyGarages:")
# though really, we could've just not written any type-checking,
# and ANYTHING with a .cars attribute that's a valid input for list.extend() would work!
fg4 = fg3 + garage
fg4.list_cars()

