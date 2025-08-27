# Simulate a football match ticket system
# storing all seat number (1 to 50) in a set.
# seat_number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 16, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}
seat_number = set(range(1, 51))
print(seat_number)
# Asking users to "book" a seat by entering a number
user = int(input("Book a Seat Number: "))
# Removing booked seats from the set.
removed = seat_number.remove(user)
print(f"Number {user} not available")
# Showing Remaining seats after each booking
print("Remaining:", seat_number)

