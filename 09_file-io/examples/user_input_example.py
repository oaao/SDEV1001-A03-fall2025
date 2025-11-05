filename = "user_input_file.txt"

while True:
	action = input("\nAdd to file (a), read (r), or quit (q): ")
	match action:
		case "a":
			item = input("Enter a todo item: ")
			with open(filename, "a") as f:
				f.write(item + "\n")
		case "r":
			with open(filename, "r") as f:
				print(f"Reading from {filename}...")
				for line in f.readlines():
					print(line.strip())
		case "q":
			break
