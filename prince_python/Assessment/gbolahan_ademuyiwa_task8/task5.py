# Creating a dictionary
store = {"Bag": 5, "Eraser": 10, "crayon": 15, "Book": 20, "Pen": 25}
print(store)
item = input(f"Enter the item you want to buy\nAvailable item: {", ".join(store.keys())}: ").title()
quantity = int(input(f"Enter the quantity of {item} you want to buy\nAvailable quantity {store.get(item)}: "))
print(f"Before Purchase: {store}")
# Using assignment operator to update
store[item] -= quantity
print(f"After Purchase: {store}")