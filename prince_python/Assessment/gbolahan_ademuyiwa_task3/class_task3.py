# Task1
# 1. Write a program to take a string input from the user and display it in uppercase.
name = input("Enter your name: ")
print(name.upper())

# 2. Given the string "python", print its first and last character
word = "python"
print(word[0])
print(word[1])

# 3. Ask the user for their name and print "Hello,!" where is the user's input.
user_name = input("Enter your Name: ")
print(f"Hello {user_name}!")

# 4. Write a program to count the number of characters in a string without using len()
text = "where are you".lower()
print(text.count("e"))

# 5. Given "Hello World", replace "word" with "python".
message = "Hello Word"
print(message.replace("Word", "Python"))

# Task2
# 6. Check if a given string contains the substring "python" (case-insensitive)
text = "python"
print("python" in text)

# 7. Write a program to reverse a string without using slicing([::-1])
text = "python"
print("".join(reversed(text)))

# 8. Given a string with extra spaces, remove the leading and trailing spaces
text = "  python  "
print(text.strip())

# 9. Ask the user to enter a sentence and print the number of vowels in it
user = input("Write a sentence: ").lower()
count  = user.count("a") + user.count("e") + user.count("i") + user.count("o") + user.count("u")
print(f"Total vowel: {count}")

# 10. convert a string "1234" to an integer and multiply it by 2.
text = int("1234")
print(text * 2)

# Task3
# 11. Given an 'apple,banana,orange", split the string into a list of fruits.
fruits = "apple,banana,orange" 
print(fruits.split(","))

# 12. Ask the user for a sentence and print each word in a new line
user = input("Write a Sentence: ")
print("\n".join(user))

# 13. Replace all spaces in a string with underscores
message = "I love Programing"
print(message.replace (" ", "_"))

# 14. Count how many times the letter "a" appears in "Banana".
text = "Banana"
print(text.count("a"))

# Check if a given string starts with "https://"
text = "https://"
print(text.startswith("https://"))
