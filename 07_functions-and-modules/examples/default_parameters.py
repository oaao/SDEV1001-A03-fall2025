def power(base, exponent=2):
	# by default, this function will square the base input
	# if I don't supply an exponent param to the function, it'll be 2
	return base ** exponent


print(power(2))    # 2 ^2  -> not supplying the second term uses the default value
print(power(2, 3)) # 2 ^3


# NOTE: keyword arguments must be *after* positional arguments