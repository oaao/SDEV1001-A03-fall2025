class Library:

	def __init__(self, name):
		self.name = name
		self.books = []

	def __str__(self):
		return self.name
