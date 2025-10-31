# dictionaries are 'just' sets with values!
s = {"name", "age", "occupation"}

d = {
	"name": "Oliver",
	"age": 35,
	"occupation": "puffin"
}

# you can check for uniqueness of an object by id()ing it!
# because dictionary keys are unique (sets),
print(
	d.keys() == s
)


# multiple values for the same key will retain the most recent value
d2 {
	"name": "Oliver",
	"age": 35,
	"age": 12,
	"occupation": "puffin"
} 

print(d2)


# you do lookups in a dictionary by *key*, rather than by *index*
print(d["name"])  # --> "Oliver"


# when you loop through a dictionary, you're only accessing keys:
for thingy in d:
	print(thingy)


# if you want to access values *as well*, you call .items() on the dictionary
print(d.items())  # gives us a [(key, val), ... ] pairwise structure

# because the structure is pairwise, we iterate over it with *two* placeholder terms
for key, value in d.items():
	print(f"{key}: {value}")
