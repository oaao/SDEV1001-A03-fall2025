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

	def checkout_book(self, book_title):
		# there are a number of ways of doing this, but here's one example:		
		# 1. extract all the titles and check if the input title exists in the library
		titles = tuple(
			(book.title for book in self.books)
		)
		# 2. check all book titles in the library, remove the one that matches OR print an 'error' message
		if book_title in titles:
			for book in self.books:
				if book_title == book_title:
					self.books.remove(book)
			print(f"\nChecked out book: {book_title}")
		else:
			print(f"\nCould not check out book '{book_title}':\nTitle does not exist in library inventory: {book_title}")
