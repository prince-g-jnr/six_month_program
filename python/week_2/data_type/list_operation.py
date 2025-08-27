# List Operations in Python
# 1. Concatenation (+)
# Joins the lists into a new list
list1 = [1,2,3]
list2 = [4,5]
result = list1 + list2
print(result)

# 2. Repetition (*)
nums = [1,2]
repeated = nums * 3
print(repeated)

# 3. Indexing
# Access elements using their position (starting from 0)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# 4. Slicing
# Extract a portion of the list
numbers = [0,1,2,3,4,5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

# 5. Membership (in/not in)
# Checks if an element exists in a list
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

# 6. Length (len())
# Counts the number of elements in a list
items = ["pen", "book", "laptop"]
print(len(items))

# 7. Min and Max (min()/max())
# Returns the smallest or largest element
nums = [5,2,9,1]
print(min(nums))
print(max(nums))

# 8. Sum (sum())
# Add all numerical elements in a list
numbers = [1,2,3,4]
print(sum(numbers))

# 9. List Comprehension
# Creates a list in a single line
squares = [x**2 for x in range(5)]
print(squares)

# 10. Copying a List
# Create a duplicate list.
a = [1,2,3]
b = a.copy()
print(b)
a = [1,2,3]
b = list(a)
print(b)