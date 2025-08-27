# Fruit collector
# Ask the user to enter 5 favourite fruits. Store them in a set and display the set
fruits = set()
for i in range(1,6):
    fruit = input(f"Enter your {i} favourite fruits: ")
    fruits.add(fruit)
print(fruits)