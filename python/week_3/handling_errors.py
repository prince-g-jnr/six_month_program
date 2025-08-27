# Handling Errors in Python
# Errors in python are classified into three main categories:
# 1. Syntax Errors
# 2. Runtime Errors
# 3. Semantic Errors
# Each category has its own characteristics, subtypes, and ways to handle them.

# 1. Syntax Errors
# Common Subtypes of syntax Errors
# A. Indentation Error - Incorret Spacing
for i in range(3):
print(i)   #Wrong indentat6ion
# This will through error execept you fix the indentation

# B. Missing Colon/Parenthesis Error
if 5 > 3      # Missing colon
    print("Hello")

# C. Invalid Syntax - General grammar mistakes.
print "Hello"   # Missing parentheses in Python 3

# 2. Runtime Errors
# Common Subtypes of Runtime Errors
# A. ZeroDivision Error - Dividing by Zero
x = 10 / 0  #This will throw error
print(x)

# B. Name Error - Using a variable before defining it.
print (age)  # age not defined

# C. Type Error - Wrong data type in an operation.
result = "10" + 5   # str + int not allowed

# D. Value Error - Invalid value for a function
number = int("abc")  # cannot convert string to int

# E. Index Error - Accessing list index out of range.
fruits = ["apple", "banana"]
print(fruits[3])   #Index out of range

# F. Key Error - Accessing a dictionary withma missing key.
data = {"name": "Ada"}
print(data["age"])    # Key not found

# G. File Not Found Error - File does not exit
f = open("missing.txt")   # File not found

# Handling Runtime Errors
# The keywords used are;
# A. try - block of code to test for errors
# B. except - block of code that runs if an error occurs
# c. finally - block of code that always runs (whether error occurs or not)

# A. The try Block
# it is used to wrap code that might raise an error
# if no orror occurs python skips the except block
try:
    x = 10 / 2
    print("Result:", x)

# B. The except Block
# it defines what to do if an error occurs inside try
# it can catch specific errors or all errors

# This is a specific exception
try:
     x = 10 / 0
except ZeroDivisionError:
     print("Cannot divide by zero.")

# This is a case of multiple exception
try:
    number = int("abc")
    result = 10 / 0 
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print(" cannot divide by zero.")

# c. The finally Block
# Always runs, whether an error occured or not.
# Useful for cleanup task(e.g, closing files, releasing resources).

# If you don't understand this line of now, It's ok. But make sure you come back to it once we are done the *File Handling*
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("closing file if it was opened.")

# Lets have more example on the application of try-execpt-finally, but try to read in between the line for better understanding.
balance = 5000     # starting balance
print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")
try:
    amount = float(amount)
    if amount > balance:
        raise ValueError("Insufficient funds.")
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Transaction session closed.")
