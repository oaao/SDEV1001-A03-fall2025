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
d2 = {
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


# if I try to access a nonexistent key, e.g. d["hobby"], I'll get a KeyError
try:
	key = "key that does not exist"
	d[key]
except KeyError:
	print(f"{key} is not a valid key in:\n{d}")

# however, if I use the .get() on a dictionary, I just get None if the key is missing
#     basically, d[k] vs. d.get(k)
#     is a decision between whether you want to trigger an exception, or return a default value (None),
#     if trying to access a missing key.
print(
	d.get("nonexistent key")
	# this is like, d.get("nonexistent key", default=None)
)

# you can also *dictate* what the default is rather than None
print(
	d.get("nonexistent key", "default value")
)
