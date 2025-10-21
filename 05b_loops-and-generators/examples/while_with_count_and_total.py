count = 0
total = 0


while True:
	
	score = input("Enter a test score, or q to quit: ")

	if score == 'q':
		break

	total += int(score)
	count += 1


if count > 0:
	print(f"Average score: {total / count}")
else:
	print("No scores entered.")
