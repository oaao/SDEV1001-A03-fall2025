# dictionaries are 'just' sets with values!
s = {"name", "age", "occupation"}

d = {
	"name": "Oliver",
	"age": 35,
	"occupation": "puffin"
}


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

# you can check for uniqueness of an object by id()ing it
