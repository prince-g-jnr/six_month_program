# Tuples
# A tuple is an orderd, immutable (unchangeable) collection of items in python
# Creating Tuples1
# 1. Using parentheses ()
fruits = ("apple", "banana", "cherry")
print(fruits)

# Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)

# Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item)) 

# Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Characteristics of Tuples
# 1. Ordered
colors = ("red", "green", "blue")
print(colors[0])  

# 2. Immutable
# colors[1] = "yellow"  #Type error because it does not allow change in positioning

# 3. Allow duplicates
numbers = (1, 2, 2, 3 )
print(numbers)

# 4. Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# 5. Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)

# Tuple operations
# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# 2. Slicing
print(fruits[0:2])
print(fruits[::-1])

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) 

# 4. Repitition
nums = (1, 2)
print(nums *3)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# 6. Interation
for fruit in fruits:
    print(fruit)

# Unpacking Tuples
person = ("john", 25, "Nigeria")
name, age, country = person
print(name)
print(age)
print(country)

# Tuple Methods
# dot count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))    #2 (count occurrences of 2)
print(numbers.index(3))    #3 (position of first occurence of 3)

# Converting Between List and Tuple
# Tuple to list
t = (1, 2, 3)
lst =list(t)
lst.append(4)
print(lst)

# List back to Tuple
t = tuple(lst)
print(t)

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
