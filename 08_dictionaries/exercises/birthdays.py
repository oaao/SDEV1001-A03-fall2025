birthdays = {
	"dan": "april 14",
	"gary": "june 23",
	"mary": "december 25"
}

name = input("Whose birthday do you want to look up? ")
print(
	birthdays.get(
		name,                                       # lookup key
		f"Sorry, we don't have {name}'s birthday."  # default return value if key missing
	)
)
