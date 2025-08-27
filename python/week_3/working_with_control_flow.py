# Control Flow in Python
# A. Conditional Statement
# 1. if Statement
# Executes a block only when a condition is true
age = 20
if age >= 18:
    print("You are eligible to vote")   #Output: You are eligible to vote

# 2. if-else Statement
# Provides two alternative paths
wallet = 400
price = 500
if wallet >= price:
    print("Purchase Successful")
else:
    print("Insufficient balance")
## Some Usecases
# Deciding success or failure of a payment.
# Granting or denying access to a system
# Determining pass/fail in an exam, etc.

# if-elif-else Statement
# Used for multiple conditions.
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")
## Some Usecases
# Student grading systems.
# Assigning ticket categories (VIP, Regular, Student).
# Categorizing temperatures (Hot, Warm, Cold), etc.

# Nested if
# Placing an if inside another if
age = 19
citizen = True
if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")
##  Some Usecases
# voting eligibility (age + citizenship)
# Banking (account active + balance sufficient)
# School admission (age + grade level)

# B. Loops
# 1. for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)
# Iterates through each element in a LIST.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
## Some usecases
# Iterating through shopping lists
# Checking availability of products
# Displaying student names, etc

# Iterates through each element in a Tuple. This works like lists, but remember that tuoles are immutabhle.
coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")
## Some Usecases
# storing fixed sensor readings
# Displaying fixed seating positions, etc
 
# Iterates through each element in a Dictionary. Remeber that dictionaries have key-value pairs
student = {"name": "Tunde", "age": 16, "grade": "A"}
for key,value in student.items():
    print(f"{key}: {value}")
## Some Usecases
# Reading database records
# Showing user profile details
# Checking configuration settings, etc

# Iterates through each element in a STRING. Remember that strings are sequences of characters.
word = "PYTHON"
for char in word:
    print(char)
## Some usecases
# Counting vowels/consonants
# Password Validation (Checking digits/special chars)
# Text analysis, etc.

# 2. while loop
# A while loop is used to repeatedly execute a block of code as long as a given condition is true. Unlike the for loop (which iterates over sequences like lists, tuples, etc.), the while loop is condition-based
# while loop condition:
      # code block
# The condition must evalute to True for the loop to continue running
# When the condition become False, the loop stops.
# Using while loop
## Documentary my thoughts##
# Let the loop start with count = 1
# Let it keep printing until count is greater than 5
# Let the loop terminate when the condition is no longer true
## My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

# Incremating with 'while'
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

# Decremating with 'while'
timer = 10
while timer > 0:
    print("\ncountdown:", timer)
    timer -= 1

# while with user input
## keep asking until the user enters a correct password
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access Granted!")

# While True:
    #Code block
    # Must include a break statement to stop
    # Keep asking the user for a name untill they type "exit".
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# Loop Control Statements (break, continue and pass)
# These keywords help us control the behavior of loops (for and while). Instead of loops always running all iterations, we can skip steps, stop early, or do nothing intentionally.
# 1. break
# Stops loop immediately. it is used if a condition is met and there's no need to continue looping.
for num in range(1, 10):
    if num == 5:
        break
    print(num) 
# The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent unnecessary iterations.

# 2. Continue
# Skips the current iteration and moves to the next one. It is used if you want to ignore some values but keep the loop running
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# 3 is skippes, but the loop continues.
## Some Usecases
# Skip invalid data.
# Ignore unwanted characters (like spaces in a string)
# Continue running but avoid certain cases, etc.

# 3. Pass
# Does nothing. A placeholder to avoid errors. It is used if you haven't written the code yet but want to keep the structure
for num in range(1, 6):
    if num == 3:
        pass    # do nothing for now
    else:
        print(num)
# At num == 3, python executes pass (nothing happens).
## Some usecases
# Writing code structure (to fill in later).
# Placeholder in class/method definitions.
# Temporarily disable parts of code.

# Lets try while True again
# Try and think through this....
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid Choice. Try again.")

# Try and use while True for Validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# Lets make a guess
secret = "python"
while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")

# Do you remember this?
balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")