# saingle quotes
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''once upone a time, there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssw0rd123"
print(password)

# String operations
# Indexing
word = "python"
print(word[0])  # p
print(word[-1]) # n 

# Slicing
word = "Python"
print(word[0:4])   #pyth
print(word[2:])    #thon 
print(word[:3])    #pyt
print(word[::2])   #pto
print(word[::-1])  #nohtyp

# String Concantenation & Repetition
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)  #Hello World

# Repetition
word = "Hi! "
print(word * 3)  # Hi! Hi! Hi!

# String Serching & Checking
# Membership
text = "Python programming"
print("Python" in text)    #True
print("java" not in text)  #True

# find() / rfind()
text = ("Hello World")
print(text.find("o"))    # 4
print(text.rfind("o"))   # 7

# index() / rindex
text = "Hello World"
print(text.index("World"))    #6
print(text.rindex("Hello"))   #0

# startswith() / endswitch
filename = "data.csv"
print(filename.startswith("data"))   # True
print(filename.endswith(".csv"))     # True


