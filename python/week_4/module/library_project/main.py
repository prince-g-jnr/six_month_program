from my_data import data
from utils import helpers
from services import library

# Add some books
data.add_book("Python Basics", "John Doe")
data.add_book("Advance Python", "Jane Smith")

# Display all books
print("Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))

# Borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python Basis"))

# Display books again
print("\nUpdated Library Collection:")
for b in data.get_books():
    print(helpers.format_book(b))