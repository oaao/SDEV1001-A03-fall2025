"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.


Find the sum of all the multiples of 3 or 5 below 100.
"""

# divisible by 3 or 5
# range(100)
# sum

# METHOD 1: for loops & numeric variable to store sum
# ---------
multiples_sum = 0

for n in range(1, 100):
	if (n % 3 == 0) or (n % 5 == 0):
		multiples_sum += n


# METHOD 2: sequence expression (in this case, list expression)
# ---------
multiples_sum_expr = [
	n for n in range(1, 100000000)
	if (n % 3 == 0) or (n % 5 == 0)
]

print(sum(multiples_sum_expr))


# METHOD 3: You can use generators!!!!!
# If I use regular brackets, and the result can be a functional expression,
# Python will return a generator rather than a tuple.

print(
	sum((n for n in range(1, 100000) if (n % 3 == 0) or (n % 5 == 0)))
)
