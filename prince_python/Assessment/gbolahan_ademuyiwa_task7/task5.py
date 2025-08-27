# Contact Quick Lookup
name = ("Alvin", "Joseph", "Daniel")
phone_no = ("07012345678", "08012345678", "09012345678")
# Combining tuples
combine = list(zip(name, phone_no))
# Creating a dictionary
dict = {}
dict[combine[0][0]] = combine[0][1]
dict[combine[1][0]] = combine[1][1]
dict[combine[-1][0]] = combine[-1][1]
# Asking User for a name
user = input(f"{", ".join(dict.keys())}\nEnter a name from the above name: ")
# Using .get() for safe retrieval
print(dict.get(user))