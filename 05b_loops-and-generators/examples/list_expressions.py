# normally, we write a for loop:
for n in range(10):
	n


# if we want to *store* that sequence, we can either:
#     A. loop through a sequence and store each step in a variable:
my_numbers1 = []

for n in range(10):
	my_numbers.append(n)

# or, B. call the list() method on a generator
my_numbers2 = list(range(10))


# i can also do a list expression:
my_numbers3 = [x for x in range(10)]


# which looks pointless, until i need conditionals/filtration etc.
my_even_numbers = [x for x in range(10) if x % 2 == 0]


"""
SIDE-NOTE: the nice thing about building sequences
through *expressions* rather than *for loops* is that it's all-or-nothing!

i.e. either the entire sequence (e.g. list) builds, or nothing happens.
     vs. with a for loop, you can end up with a partially constructed object.
"""


"""
Let's take a closer look at the structure of list expressions:

When you have a nested loop, to 'convert' to an expression, you  basically just:
    - take the last term in the for loop
    - put it at the *start* of the expression
    - continue the expression by 'writing out the for loop as normal'

"""

# ex.1
for b in a:
	b

[b for b in a]


# ex.2
for b in a:
	for c in b:
		c

[c for b in a for c in b]


# ex.3
for b in a:
	for c in b:
		for d in c:
			for e in d:
				d

[d for b in a for c in b for d in c for e in d]
