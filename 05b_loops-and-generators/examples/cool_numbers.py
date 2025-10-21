print("Enter numbers to add, type 'done' to finish.")

total = 0

while True:
	
	# I'm going to be soliciting inputs in a loop
	value = input("Enter a whole number: ")

	# then break at a defined condition
	if value == 'done':
		break

	total += int(value)

print(f"Total sum: {total}")
