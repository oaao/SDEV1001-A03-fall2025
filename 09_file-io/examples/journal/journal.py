def read_journal(filename):
	"""Read the journal entries from a file"""
	with open(filename, "r") as f:
		# option 1: read all of the file at once
		entries = f.readlines()
	return entries


if __name__ == "__main__":
	
	file_path = "journal.txt"
	entries = read_journal(file_path)

	print(f"\nJournal entries in {file_path}:")
	for i, entry in enumerate(entries, start=1):
		print(f"{i}: {entry.strip()}")
