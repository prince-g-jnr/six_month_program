# Super Market Price List
# Creating an empty Dictionary
stores_items = {}
# Storing items in a list
items = ["egg", "potatoes", "butter", "fish", "meat"]
# Adding items and price to a dictionary
stores_items[items[0]] = float(input("Enter the price of Item: "))
stores_items[items[1]] = float(input("Enter the price of Item: "))
stores_items[items[2]] = float(input("Enter the price of Item: "))
stores_items[items[3]] = float(input("Enter the price of Item: "))
stores_items[items[-1]] = float(input("Enter the price of Item: "))
# Displaying all items and price
print(stores_items)
# Available items
available_items = stores_items.keys()
print(available_items)
# Update items
updated_items = input("Enter the item you want to update: ")
# Validating user input
if updated_items in stores_items.keys():
    stores_items[updated_items] = float(input("Enter the price of the item: "))
else:
    print(f"{updated_items} is not in the items")
print(stores_items) 
