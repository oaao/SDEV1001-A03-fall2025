from file_reader import read_file


def summarise_file():
	filename = input("Enter a filename: ")
	lines = read_file(filename)


if __name__ == "__main__":
	summarise_file()