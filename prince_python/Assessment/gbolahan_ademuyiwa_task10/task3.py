# Mixing Data Types
try:
    age = int(input("Enter your Age: "))
    height = float(input("Enter your Height: "))
    name = input("Enter your name: ")
    print(f"Hello {name}, you are {age} years old and your height is {height}.")
except ValueError:
    print("Error: Invalid Input")