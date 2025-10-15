# Remember to use "p n" to print the value of n at each iteration, since "n" means "run next line" in the debugger.

# p n
# total
# c
#       ... repeat


numbers = [1, 2, 3, 4, 5]

total = 0

for n in numbers:
    breakpoint()
    total += n

print(f"Total {total}")
