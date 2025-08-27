# List Method
# 1. dot append() method
# Adds an element to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# 2. dot insert() method
# Inserts an elements at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

# 3. dot extend() method
# Adds elements from another list (or iterable) to the end
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)

# 4. dot removed() method
# Removes the first occurrence of a specified value
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

# 5. dot pop() method
# Removes and returns the element at a given index(default:last)
fruits = ["apple", "banana", "cherry"]
last_fruits = fruits.pop()
print(last_fruits)
print(fruits)

# 6. dot clear() method
# Removes all elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# 7. dot index() method
# Returns the index of a first occurrence of a value
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)

# 8. dot count
# Counts how many times a value appears
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))

# 9. dot sort() method
# sorts the list in ascending order (default)
numbers =  [3, 1, 4, 2]
numbers.sort()
print(numbers)
# descending order
numbers.sort(reverse=True)
print(numbers)

# 10. dot reverse() method
# Reverses the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

# 11. copy()
# Returns a shallow copy of the list
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)