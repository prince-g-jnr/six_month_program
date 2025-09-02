import my_data.data as data

def borrow_book(title):
    for book in data.get_book():
        if book["title"].lower() == title.lower() and book["available"]:
            book["avilable"] = False
            data.save_books()
            return f"You have borrowed '{book['title']}'"