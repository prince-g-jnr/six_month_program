# MODULARIZING YOUR CODE 1
# 1. Introduction to Modularity
# 2. Function (first level of modularity)
# See Examples of ude here
# range()
for i in range(3):
    print(i)
# Output: 0, 1, 2 

# zip()
names = ["Esther", "Precious", "Kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "scored", s)

# It's ok, if you dont kmow what lamba is or how to use it. I will touch on it later. Just focus on the outputs
# map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)
# Output: [1, 4, 9, 16]

# filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
# Output: [2, 4]

# Student Performance & Feedback System
# Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 =input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3= input("Enter third studdent name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display Data
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerformance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

# Step 5: Ranking (Using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")

# Step 6: Chech data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id (names))
print("ID of scores list:", id(scores))

# Step 7: Filter passing students (>50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)

# USER DEFINED FUNCTION
"""
In Python, we use the `def` keyword to define a function.
Then we call the function whenever we want to use it.
"""
"""
def function_name(takes in input):
    process block
    output block
"""
"""
def function_name(input - here, you will insert an item or list of what the function will need to work):
    "process block -here will contain the logic or what you want the function to do"
    " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or'print()' or 'yield'"
"""
def greet():
    print("Hello, welcome to AI Fellowship")
"""
When you want to use a function, this is how to call it.
And you can call it as many times as possible.
"""
greet()
greet()
greet()

# Function 3with an argument - the placeholder
def greet(name):
    print("Hello", name, "Welcome to python learning!")

# Calling with parameter - the actual name
greet("Class rep")
greet("Ridwan")

# When you use return,print(), and yield keywords inside a function
# a. print()
def greet(name):
    print("Hello", name)

# Function call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)

# b. return
def add(a,b):
    return a + b

# Function call
result = add(4, 6)
print("The sum is:", result)

# Note the output and compare it with that of print()

# c. yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i        # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)

# More on Function Arguments(Types of Arguments)
# 1. Positional Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce("Ngozi", "Ai Engineering")     #Correct order

# Change the arrrangement and watch the output
introduce("AI Engineering", "Ngozi")   #Incorrect order, this will throw a semantic error

# 2. Keyword Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name= "Ngozi", track= "AI Engineering")

# Change the arrangement and watch the output
introduce(track= "AI Engineering",name= "Ngozi") #Here you notice that order does not batter

# 3. Default Argument
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
# without specifying the default argument, but watch the output
introduce("Paul")

# specify the default argument and watch the output
introduce("Tunji Paul", track = "AI Deveplopment")

# 4. Varying Length Arguments
# a. non-keyword(tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# b. Keyword argument (dictionary)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# function call - Take note of the output
student_details(name ="Peter", track = "AI Engineering", interest = "Block Chain")

# Lets implement on full cade

# Define student profile function

# Ensure to note the order of arangement of the types of arguments used
# This is how to arrange it of you are using everthing or some of the together
def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n --- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # skillls (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
    
    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    return profile
# Do you remember 'return' and why it is used? We are using it so it can be reused in other places

# ---------- Lets Test ----------

# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length poditional (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest = "Blockchain", city = "Shagamu", phone = "08123456789"
))
