

class User:

    _id_counter = 1

    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.id = User._id_counter
        User._id_counter += 1
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("Aucun livre loué")
            return
        for book in self.borrowed_books:
            print(f"{book.title} par {book.author}")
