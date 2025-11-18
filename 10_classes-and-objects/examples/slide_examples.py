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


# 2. Class attributes can have any type, including collections/lists!
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


# 3. Let's make a garage, and add some of those cars!
garage = Garage()
garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)
garage.add_car(Car("Harley Davidson", "Edgelord", 2001))

garage.list_cars()

