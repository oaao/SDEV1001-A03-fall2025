import csv

# https://docs.python.org/3/library/csv.html
#   csv.DictReader: https://docs.python.org/3/library/csv.html#csv.DictReader
#   csv.DictWriter: https://docs.python.org/3/library/csv.html#csv.DictWriter



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
def read_csv(file_path):
	
	# this is going to be a list of dictionaries
	lines = []
	with open(file_path, 'r') as file:
		# note: no fieldnames param, so by default it'll assume first CSV row is fieldnames
		reader = csv.DictReader(file)
		for row in reader:
			lines.append(row)

	return lines

print("\nPrinting out books.csv...")
books = read_csv("books.csv")
for book in books:
	print(book["Title"], "-", book["Author"])


# 3. writing to a CSV file - using csv.DictWriter, we
#      - write the header row first (fieldnames as first line in CSV)
#      - then, write rows
def save_grades(filename, data):
	
	# open in write mode with no end-of-line suffix characters (like "\n"),
	# since we're just writing to CSV and each new row will be a new line in the output file anyway
		with open(filename, "w", newline="") as csvfile:
		
			# first, we need the column headers / fieldnames / dict keys:
			# you *could* fieldnames = data[0].keys(), but I'll list them explicitly
			fieldnames = ("student", "score")

			# then, initialise the csv.DictWriter(actual_file_buffer, fieldnames)
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			# first, write the header row (fieldnames) once, then write every content row
			writer.writeheader()
			for row in data:
				writer.writerow(row)


grades = [
	{"student": "Oliver", "score": 49},
	{"student": "Winnie the Pooh", "score": 99},
	{"student": "a plastic bag", "score": 75}
]

save_grades("scores.csv", grades)


# 4. Reading & filtering CSV data, using a list expression
print("\nReading from scores CSV file to filter for passing students...")
passing_students = [s for s in read_csv("scores.csv") if int(s["score"]) >= 50]
for s in passing_students:
	print(f"{s["student"]} passed with a grade of {s["score"]}!")
