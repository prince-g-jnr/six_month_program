# Creating a list
items = ["Bag", "Chair", "Table", "Book", "Pen"]
prices = [1000, 1500, 2000, 300, 100]
# merging items and prices together
list = list(zip(items, prices))
print(list)
# Accumulating in key - value pair
item_price = {}
item_price[list[0][0]] = list[0][1]
item_price[list[1][0]] = list[1][1]
item_price[list[2][0]] = list[2][1]
item_price[list[3][0]] = list[3][1]
item_price[list[-1][0]] = list[-1][1]
# Empty cart
cart_total = 0
print(items)
list_of_items = ["Bag", "Table", "Book"]
# Adding the price of some items to cart_total
cart_total += item_price["Bag"]
cart_total += item_price["Table"]
cart_total += item_price["Book"]
print(f"Items: {list_of_items}\nTotal Price: ₦{cart_total}")