# Fruit collector
# Ask the user to enter 5 favourite fruits
#  Storing them in a set
fruits = set()
for i in range(1,6):
    fruit = input(f"Enter your {i} favourite fruits: ").title()
    fruits.add(fruit)
# Displaying the Set
print(fruits)