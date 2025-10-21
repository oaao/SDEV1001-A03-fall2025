# fibonacci sequence with recursion:
# e.g. 1,   1,   2,   3,   5,   8,   13,  21,  34,  55
#      1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th

def nth_fibonacci(n):
	"""Calculate the nth number in the fibonacci sequence."""
	if n <= 1:
		return n
	return (
		nth_fibonacci(n-1) + nth_fibonacci(n-2)
	)


def print_first_n_fib_numbers(n):  # horrific function naming
	# range starts at 0 by default, and ends *before* the ceiling term
	# so, since we start counting at 1, our range needs to be 1 -> n+1
	for i in range(1, n+1):
		print(f"Fibonacci number {i} is: {nth_fibonacci(i)}")



# if I do this, I can import ^all this stuff^ in some other file
# without vTHISv code running when I do that import.
if __name__ == "__main__":
	# e.g. 1
	n = int(input("What is the nth fibonacci number you want to find out? "))
	print(
		f"The fibonacci number at position {n} is: {nth_fibonacci(n)}"
	)

	# e.g. 2
	num_fibs = int(input("I want to generate the first {n} fibonacci numbers: "))
	print_first_n_fib_numbers(num_fibs)

