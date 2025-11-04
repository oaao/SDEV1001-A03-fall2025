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

# using:
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# 1. looping over keys
print("Students:")
for student in grades.keys():
	print("-", student)


# 2. looping over values
total = 0
for score in grades.values():
	total += score
	print("Average score:", total / len(grades))


# 3. looping over key-value pairs
for name, score in grades.items():
	print(f"{name} scored {score}")


# 4. you can also sort a dictionary, just like a list, using its keys
inventory = {"apples": 5, "bananas": 2, "oranges": 8}
for fruit, count in sorted(inventory.items()):
print(f"{fruit.title()}: {count}")

# 5. or (bonus: lambda functions, not required) sorted by its values
#    --> the x: x[1] expression means,
#        for the pairwise data structure [ (k, v), ... ] 
#        take the element at index 1 for each, i.e. here v
inventory = {"apples": 5, "bananas": 2, "oranges": 8}
for fruit, count in sorted(inventory.items(), key=lambda x: x[1]):
print(f"{fruit.title()}: {count}")


# 6. and, refactoring! what if 
inventory = {"apples": 0, "bananas": 0, "oranges": 0}
purchases = ["apples", "bananas", "apples", "oranges", "apples"]
for item in purchases:
	inventory[item] += 1
print("Inventory:")
for fruit, count in sorted(inventory.items()):
	print(f"{fruit.title()}: {count}")