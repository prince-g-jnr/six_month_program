# How to Create a List
# You can create an empty list when you don't have elements yet but plan to add later.
# Method 1: Using square brackets
empty_list = []
print(empty_list)

# Method 2: Using the list() constructor.
empty_list2 = list()
print(empty_list2)

# Creating a List with initial Elements.
# List can store multiple items seperated by commas inside square brackets
# List of integers
number = [1,2,3,4,5]
print(number)

#  List of string
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

# Creating a List from A nother Sequence. You can convert strings, tuples, or other iterables into a list.
# From a string (each character becomes an element)
chars = list("hello")
print(chars)

# From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# From a range
numbers_range = list(range(5))
print(numbers_range)

# Creating a List Using List Comprehension. List comprehensions are a concise way to create lists using a loop in one line. 
# Squares of number 0-4
squares = [x**2 for x in range(5)]
print(squares) 

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

# Creating a Nested List. A list can contains other list it is useful for matrics or grouped data.
# Matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[0])
print(matrix[0][1])
print(matrix[1][0])

# Characteristics of a List
# 1. Ordered Collection
# The elements in a list maintain the order in which they are inserted
# The first element has index 0, the second has index 1, and so on.
fruits = ["mango", "orange", "banana"]
print(fruits)        #['mango', 'orange', 'banana']
print(fruits[0])     #mango (first element)
print(fruits[2])     #banana (third element)
print(fruits[1])     #orange (second element)

# 2. Allow Duplicates 
# List can store the same value multiple times.
items = ["rice", "beans", "yam", "rice"]
print(items)

# 3. Mutable (Can Be Changed)
# You can modify a list after it's created-change elements, add new ones, or remove existing ones.
numbers = [1,2,3]
numbers[1] = 20
print(numbers)

# 4. Can Contain Different Data Types
# A list can hold integers, strings, floats, booleans, and even other lists.
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

# 5. Can Be Nested
# A list can contain other lists (2D or multi-dimensional list)
nested_list = [[1,2], ["a","b"]]
print(nested_list)
print(nested_list[0][1])
print(nested_list[1][0])

# 6. Dynamic Size
# You don't need to declare the size of a list beforehand; it can grow or shrink as needed.
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)