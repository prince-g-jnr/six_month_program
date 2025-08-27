# Unique Members Registration
names = input("Enter three Names seperated by commas: ").split(",")
print(names)
# Converting to set
user = set(names)
# Creating a dictionary
lengths = {name: len(name) for name in user}
print(lengths)