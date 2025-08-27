# STRING OPERATIONS

# upper()
# Converts all characters in the string to uppercase
name = "Ada Balogun"
print(name.upper())

# lower()
# converts all characters in the string to lowercase
sentence = "PYTHON IS AMAZING"
print(sentence.lower())

# title()
# converts all characters in the string to title
sentence = "python is amazing"
print(sentence.title())

# strip()
# removes whitespace (or specified characters) from both ends of the string.
text = "  Abuja  "
print(text.strip())

# replace()
# replaces occurrences of a substring with another substring.
message = "I love Java"
print(message.replace("java", "python"))

# swapcase
# switches lowercase to uppercase and vice versa.
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip()
# remove whitespace (or specified characters) from the left side only.
text = "   Nigeria"
print(text.lstrip())

# rstrip
# removes whitespace (or specified characters) from the right side omly.
text = "Nigeria   "
print(text.rstrip())

# split()
# splits a string into a list using a seperator (default is space)
fruits = "mango orange banana"
print(fruits.split())

# rsplit()
# splits a string into a list from the right side
text = "one,two,three,four"
print(text.rsplit(",",2))

# splitlines()
# splits a string into a list at each newline(\n).
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# join(
# joins a list of strings info one string with a specified seperator).
words = ["I", "love", "python"]
print(" ".join(words))

# center
# centers the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.center(20, "-"))

# ljust
# leFt-aligns the string within a specified width, padding with spaces or characters.
text = "python"
print(text.ljust(10, "*"))

# rjust
# right-aligns the string within a specified width, padding with spaces or characters
text = "python"
print(text.rjust(10, "*"))

# zfill()
# pads a numeric string on the left with zeros until it reaches a given length.
num = "42"
print(num.zfill(5))

# isalpha()
# checks if the strings contains only letters.
print("Lagos".isalpha())      # True
print("Lagos123".isalpha())   # False

# isdigit()
# checks if the string contains only digits.
print("12345".isdigit())     #True
print("12345a".isdigit())    #False

# isalnum()
# checks if the string contains only letters and digits.
print("python3".isalnum())   #True
print("python 3".isalnum())  #False