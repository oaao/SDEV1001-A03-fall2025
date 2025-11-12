import csv

""" Sometimes, your CSV files will have fieldnames / column headings
    in the first row, in which case we'd just pop them out.

    In this example, I'll be specifying it manually.
    
    For CSV *dictionary* readers/writers, fieldnames are necessary,
    because that's what's used for keys.
"""

# 1. Reading from CSV file to a dictionary, if the CSV's first row contains no fieldnames / column headers
def read_csv(filename, fieldnames=None):
	if not fieldnames:
		print("Please provide a list of fieldnames so that we can parse CSV contents into a dictinoary.")
	else:
		with open(filename, 'r') as f:
			# NOTE: we're not passing the filename to csv.DictReader, but the buffer contents of the opened file
			reader = csv.DictReader(f, fieldnames=fieldnames)
			for row in reader:
				# you can access e.g. row["name"] directly if you wanted to!
				print(row)

print("\nPrinting out basic_csv.csv as dictionary rows...")
read_csv("basic_csv.csv", fieldnames=("name", "age", "occupation"))


# 2. Reading from CSV to dictionary, when CSV has fieldnames in first row
#    -> basically, I just don't provide it with any fieldnames and it should grab them from the first row in the CSV 
def read_books(file_path):
	
	# this is going to be a list of dictionaries
	books = []
	with open(file_path, 'r') as file:
		# note: no fieldnames param, so by default it'll assume first CSV row is fieldnames
		reader = csv.DictReader(file)
		for row in reader:
			books.append(row)

	return books

print("\nPrinting out books.csv...")
books = read_books("books.csv")
for book in books:
	print(book["Title"], "-", book["Author"])

