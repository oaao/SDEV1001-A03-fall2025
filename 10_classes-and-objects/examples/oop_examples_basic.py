"""
And I OOP??????
- Object Oriented Programming examples in code
"""

print("1.a) Let's start off with a simple definition for an organism.")
class Organism:

	def __init__(self, binomial_name):
		genus, species = binomial_name.split(" ")  # splits string by space into a list of strings
		self.genus = genus.capitalize()
		self.species = species.lower()

	def __repr__(self):
		# instead of hardcoding "Organism", let's make this generic
		# so that other classes we build off of this will automatically show *their* name! 
		return f"{self.__class__.__name}<'{self.genus} {self.species}'>"

	def __str__(self):
		return f"{self.genus} {self.species}"


very_cool_sea_cucumber = Organism("Enypniastes eximia")
# printing, or casting into a string, uses the __str__() method:
print(very_cool_sea_cucumber)
print(f"The only sea cucumber that can swim is {very_cool_sea_cucumber}; it even has its own genus!")


# ---------------------------------------------------------------------------------------
print(
	"\n1.b) I could make an instance for every organism, but what if they need to behave slightly differently as code objects?"
	"Enter inheritance!"
)
class LandAnimal(Organism):  # LandAnimal inherits all attributes & methods from Organism

	def walk(self):
		print(f"{self} is walking!")  # uses self.__str__()!

	def run(self):
		print(f"{self} is running!")


class WaterAnimal(Organism):

	def swim(self):
		print(f"{self} is swimming!")


dog = LandAnimal("canis familiaris")
dog.walk()
dog.run()

leaf_sheep = WaterAnimal("Costasiella kuroshimae")
leaf_sheep.swim()


# ---------------------------------------------------------------------------------------
print(
	"\n1.c) You can even inherit from multiple parent/base classes!"
	" Unsurprisingly, this is called multiple inheritance."
)

class Amphibian(LandAnimal, WaterAnimal):
	pass


tiger_salamander = Amphibian("Ambystoma tigrinum")
tiger_salamander.walk()
tiger_salamander.run()
tiger_salamander.swim()


print("Just remember that in multiple inheritance, order matters.")
class A:
	def __init__(self):
		print("Class A conquers all!")

class B:
	def __init__(self):
		print("Class A conquers all!")

class C:
	def __init__(self):
		print("Class A conquers all!")


class Combination(A, B, C):
	def __init__(self):
		print("Who will win...?")
		super().__init__()


print("Pay attention to which of the print statements executes...")
order_matters = Combination()
