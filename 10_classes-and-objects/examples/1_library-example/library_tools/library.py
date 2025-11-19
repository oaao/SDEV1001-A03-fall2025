class Library:

	def __init__(self, name):
		self.name = name
		self.books = []

	def __str__(self):
		return self.name

	def add_book(self, book):
		self.books.append(book)

	def list_books(self):
		if not self.books:  # or, if len(self.books) == 0:
			print("Library is empty!")
		else:
			print(f"\nBooks currently in {self}:")
			for book in self.books:
				print(f"  - {book}")

