# # Shopping List Manager
# Creating an empty list
# Asking user to enter 3 shopping items
# Adding them to the list
# Displaying the list as a single string, seperated by commas.
shopping_list = []
for i in range(1,4):
    items = input(f"Enter your number {i} shoping item: ").title()
    shopping_list.append(items)
print(shopping_list)
print(f"shopping list: {", ".join(shopping_list)}")