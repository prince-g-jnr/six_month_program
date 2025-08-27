# Task 1: Create and Display
favorite_dish1 = input("Enter your favorite Nigerian Dishes: ")
favorite_dish2 = input("Enter your favorite Nigerian Dishes: ")
favorite_dish3 = input("Enter your favorite Nigerian Dishes: ")
dishes = (favorite_dish1, favorite_dish2, favorite_dish3)
print(dishes)
print(f"{favorite_dish1}\n{favorite_dish2}\n{favorite_dish3}")
# or
print(f"{dishes[0]}\n{dishes[1]}\n{dishes[-1]}")