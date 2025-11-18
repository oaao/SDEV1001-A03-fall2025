# 1. First, let's define a Car class
# ---------------------------------------------------------------
class Car:

	wheels = 4

	def __init__(self, make, model, year):

		self.make = make
		self.model = model
		self.year = year

	def __repr__(self):
		return f"Car<{self.year} {self.make} {self.model}>"

	def __str__(self):
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
class FancyGarage(Garage):

	def __init__(self, cars=None):
		super().__init__()
		if cars:
			self.cars.extend(cars)

	def __add__(self, garage):
		if not isinstance(garage, Garage):
			raise TypeError(
				f"Addition unsupported between FancyGarage and {type(garage)}."
			)
		else:
			self.cars.extend(garage.cars)
			return self


car4 = Car("Lotus", "Elise", 2007)
car5 = Car("SSC", "Tuatara", 2021)
fg1 = FancyGarage([car4, car5])
print("\n Before merging, mg1 contains:")
fg1.list_cars()

car6 = Car("Gibbs", "Aquada", 2003)
fg2 = FancyGarage([car6,])

print(f"\n Merging mg1 and mg2...")
fg3 = fg1 + fg2
fg3.list_cars()

print("\nBecause we type-checked with isinstance(), we can also add Garages to FancyGarages:")
fg4 = fg3 + garage
fg4.list_cars()

