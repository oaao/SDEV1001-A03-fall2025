def read_journal(filename):
	"""Read the journal entries from a file"""
	try:
		with open(filename, "r") as f:
			# option 1: read all of the file at once
			entries = f.readlines()
		return entries
	except FileNotFoundError:
		return [f"ERROR: {filename} does not exist."]


def write_journal(filename, journal_entry):
	"""Write a journal entry into the given file"""
	with open(filename, "a") as file:  # 'a' mode -> 'a'ppends to file contents
		file.write(f"{journal_entry}\n")


if __name__ == "__main__":
	
	file_path = "journal.txt"

	while True:
		
		action = input("\nDo you want to:\n  (r)ead the journal, (w)rite a new entry, or (q)uit? ").lower()

		match action:
			case "r":
				entries = read_journal(file_path)
				print(f"\nJournal entries in {file_path}:\n")
				for i, entry in enumerate(entries, start=1):
					print(f"{i}: {entry}")
			case "w":
				new_entry = input("Enter your journal entry:\n")
				write_journal(file_path, new_entry)
				print("Entry added to journal.")
			case "q":
				print("OK, see ya!")
				break
			case _:
				print(f"{action} is not a valid action. Please try again.")
