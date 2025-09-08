# # MODULARIZING YOUR CODE 1
# # 1. Introduction to Modularity
# # 2. Function (first level of modularity)
# # See Examples of ude here
# # range()
# for i in range(3):
#     print(i)
# # Output: 0, 1, 2 

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# # It's ok, if you dont kmow what lamba is or how to use it. I will touch on it later. Just focus on the outputs
# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)
# # Output: [1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)
# # Output: [2, 4]

# # Student Performance & Feedback System
# # Step 1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 =input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3= input("Enter third studdent name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display Data
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (Using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step 6: Chech data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id (names))
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)

# # USER DEFINED FUNCTION
# """
# In Python, we use the `def` keyword to define a function.
# Then we call the function whenever we want to use it.
# """
# """
# def function_name(takes in input):
#     process block
#     output block
# """
# """
# def function_name(input - here, you will insert an item or list of what the function will need to work):
#     "process block -here will contain the logic or what you want the function to do"
#     " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or'print()' or 'yield'"
# """
# def greet():
#     print("Hello, welcome to AI Fellowship")
# """
# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
# """
# greet()
# greet()
# greet()

# # Function 3with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "Welcome to python learning!")

# # Calling with parameter - the actual name
# greet("Class rep")
# greet("Ridwan")

# # When you use return,print(), and yield keywords inside a function
# # a. print()
# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)

# # b. return
# def add(a,b):
#     return a + b

# # Function call
# result = add(4, 6)
# print("The sum is:", result)

# # Note the output and compare it with that of print()

# # c. yield
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i        # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)

# # More on Function Arguments(Types of Arguments)
# # 1. Positional Arguments
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track,".")

# # function call
# introduce("Ngozi", "Ai Engineering")     #Correct order

# # Change the arrrangement and watch the output
# introduce("AI Engineering", "Ngozi")   #Incorrect order, this will throw a semantic error

# # 2. Keyword Arguments
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track,".")

# # function call
# introduce(name= "Ngozi", track= "AI Engineering")

# # Change the arrangement and watch the output
# introduce(track= "AI Engineering",name= "Ngozi") #Here you notice that order does not batter

# # 3. Default Argument
# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track, ".")

# # function call
# # without specifying the default argument, but watch the output
# introduce("Paul")

# # specify the default argument and watch the output
# introduce("Tunji Paul", track = "AI Deveplopment")

# # 4. Varying Length Arguments
# # a. non-keyword(tuple)
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# # function call
# # Take note of the output
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50)

# # b. Keyword argument (dictionary)
# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# # function call - Take note of the output
# student_details(name ="Peter", track = "AI Engineering", interest = "Block Chain")

# # Lets implement on full cade

# # Define student profile function

# # Ensure to note the order of arangement of the types of arguments used
# # This is how to arrange it of you are using everthing or some of the together
# def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
#     """
#     Generate a profile for a bootcamp participant using different types of arguments.
#     """
#     profile = f"\n --- Bootcamp Participant Profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"

#     # skillls (from *args)
#     if skills:
#         profile += "Skills: " + ", ".join(skills) + "\n"
#     else:
#         profile += "Skills: Not yet specified\n"
    
#     # Extra info (from **kwargs)
#     if extra_info:
#         profile += "Additional Info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"
#     return profile
# # Do you remember 'return' and why it is used? We are using it so it can be reused in other places

# # ---------- Lets Test ----------

# # Example 1: Using only positional arguments
# print(participant_profile("Peter", 24))

# # Example 2: Adding keyword/default argument
# print(participant_profile("Ridwan", 29, track="AI Engineering"))

# # Example 3: Adding variable-length poditional (*args)
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# # Example 4: Adding variable-length keyword arguments (**kwargs)
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest = "Blockchain", city = "Shagamu", phone = "08123456789"
# ))

# Namespaces and Scope
"""
**Namespace**

- A namespace is like a “container” that holds names (variables, functions, objects) and maps them to the actual data stored in memory.
- Think of it as a dictionary where keys are names and values are objects.
- Python uses namespaces to avoid name conflicts.
- Lets imagine a company where different departments can have employees with the same name.
  - In the IT department, there may be a "Chris".
  - In the Training department, there may also be a "Chris".
- Both exist, but they are identified by their department (namespace), so there's no confusion.
"""
# Global Namespace
employee = "General Employee"

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_department():
    # Local Namespace inside Training_Department
    employee = "Chris (Training)"
    print("Inside Training Department", employee)

print("In Global Namespace:", employee)     #Refers to global variable

IT_department()     #Uses local variable in IT
Training_department()     #Uses local variable in Training

# Using a built-in namespace function
print("Length of 'Python':", len("Python"))

# So 'chris' can exist in more than one namespace without conflict.

# Scope
# Scope defines where in the code a name is accessible. Python follows the LEGB Rule (order of search for a variable):
"""
L - Local → Inside the current function.
E - Enclosing → Inside any enclosing function(s).
G - Global → At the top level of the script/module.
B - Built-in → Python's built-in functions/objects.
"""
# Global Namespace
x ="global x"

def outer():
    x = "enclosing x"   # Enclosing Namespace

    def inner():
        x = "local x"     # Local Namespace
        print("Inside inner:", x)   #Local wins

    inner()
    print("Inside outer:", x)    #Enclosing

outer()
print("In global:", x)  #Global


### Global Keyword
# Used when you want to modify a global variable inside a function.

x = 5

def change_global():
    global x
    x = 10      # modifies the global x

change_global()
print(x)

# nonlocal keyword
# Used in nested functions when you want to modify the variable from enclosing scope (not global).

def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "chamged by inner"
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()

# Lamda Function
"""
- A lambda function is a small, anonymous function (no name) defined using the lambda keyword.
- It can have any number of arguments, but only one expression.
- The result of the expression is automatically returned.
"""
"""
- This is the syntax
lambda arguments: expression
"""
"""
-- You use lambda;
- When you need a short, throwaway function(not reuseable).
- To avoid writing full def functions for small tasks.
- Used with functions like map(), filter(), sorted(), and reduce()
"""

# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2
print(square(5))
print(square_lambda(5))

# This one has more than one arguments.

add = lambda a, b: a + b
print(add(3, 7))

# Let us lambda to apply the square function to a list

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Lets use lambda to filter even numbers

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Lets use lambda to sort the tuple within a list.

students = [("Ayo", 20), ("Bola", 18), ("Chike", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)