# my_data/data

import json
import os

FILE_PATH ="library_data.json"
books = []

def load_book():
    """Load books from JSON file if exists"""
    global books
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            books = json.load(f)
    else:
        books = []

def save_books():
    """Save current books list to JSON file"""
    with open(FILE_PATH, "w") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})
    save_books()

def get_book():
    return books
