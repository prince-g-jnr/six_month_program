# Task4: Tuple Unpacking
name = input("Enter your First Name: ")
age = int(input("Enter your Age: "))
color = input("Enter your Favorite Color: ")
town = input("Enter your Home Town: ")
details = (name, age, color, town)
print(details)
name, age, color, town = details
print(f"User Details\tResponse\nFirst Name\t{name}\nAge\t\t{age}\nFavorite Color\t{color}\nHome Town\t{town}")