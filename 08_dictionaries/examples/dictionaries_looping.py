# looping over dictionaries like you would a list will return only keys:
d = {
	"first_key":  1,
	"second_key": 2,
	"third_key":  3,
}

for k in d:
	print(k)  # "first_key", "second_key", "third_key"


# you can explicitly extract / loop over keys with d.keys(),
# and values with d.values()

# to loop over the key-value pairwise structure directly, use d.items()
#   note that key &
for key, value in d.items():
	print(key, value)



# examples from the slides:
# -------------------------

# 1. looping over keys
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("Students:")
for student in grades.keys():
print("-", student)

# 2. looping over values
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
total = 0
for score in grades.values():
total += score
print("Average score:", total / len(grades))

# 3. looping over key-value pairs
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, score in grades.items():
print(f"{name} scored {score}")

