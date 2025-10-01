# 1. Make the list & print it
groceries = [
	"lettuce",
	"tomatoes",
	"bread",
	"milk",
	"chicken",
	"apples"
]

# print("Our grocery list is:")
# print(groceries)
print(f"Our grocery list is:\n{groceries}")


# 2. Access some items in the list by index
print(f"\nThe FIRST item in the grocery list is: {groceries[0]}")
print(f"The THIRD item in the grocery list is: {groceries[2]}")
print(f"The LAST item in the grocery list is: {groceries[-1]}")


# 3. Change some things in the list
groceries[4] = "seitan"  # going veg
print(f"\nWe've modified the fifth element: {groceries}")


# 4. Let's slice some sublists!  --> list[start:end] --> start is inclusive; end is exclusive
print(f"\nThe first three items are: {groceries[:3]}")  # groceries[0:3]
print(f"The last two items are: {groceries[-2:]}")    


# 5. How long is our list? (How many elements does it contain?)
print(f"The length of our grocery list is {len(groceries)}")