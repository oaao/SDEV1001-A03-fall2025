"""
Basic syntax for opening files:

1. the built-in function you use to open a file is: open()
   - you usually don't/shouldn't use open() 'manually', because you have to remember to
     manually close the file once you're done I/O, can't necessarily predict if/when data streaming
     finishes or actually happens concurrently with other lines of code or not, etc.
   - therefore, we use what's called a context manager
     - more here: https://stackoverflow.com/questions/31334061/file-read-using-open-vs-with-open
                  https://www.reddit.com/r/learnpython/comments/nfszml/with_open_vs_open_in_python/

2. context manager: with open()
   - anything inside the indented block safely runs AND THEN closes the file before proceeding
     to any subsequent lines of code (unless of course you're deliberately writing async code) 

3. you usually pass two arguments to open(): filename/path, and mode of access, e.g.
   - 'r': read
   - 'w': write
   - 'rw': both
"""

def read_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
	return lines

# iterating through each line will already print out a new element per new line,
# so we strip away the \n at the end of each element so it doesn't double up (try removing it and see what happens!)
print("Reading from file that exists...")
for line in read_file("example1.txt"):
	print(line.strip())


# file.read() parses e.g. a text file as a single string with newline characters marking newlines
# file.readline() returns one line as a string, and the 'cursor' remains at the start of the next line
# file.readlines() returns all lines as a list

# once you have 'gone through' the file within an open() context, you need to
# find some way to reset the 'cursor' for reading the file, similar to e.g. a record player
# - close and reopen the file
# - manually file.seek(0) -> i.e. seek back to the beginning of the file buffer contents

def safely_read_file(filename):
	# if the filename doesn't exist, a FileNotFoundError exception will be thrown
	try:
		with open(filename) as f:
			lines = f.readlines()
		return lines
	except FileNotFoundError as e:
		print(e)

print("\nReading from file that doesn't exist and capturing the exception message...")
safely_read_file("nonexistent_file")