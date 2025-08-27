# Unique Name Collector
# Write a program that collects the name of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
names = input("Enter the name of people attending a seminar seperated by commas: ")
names = names.split()
names = set(names)
names = list(names)
names.sort()
print(names)