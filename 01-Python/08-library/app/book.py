
class Book:

    _isbn_counter = 123

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        self.isbn = Book._isbn_counter
        Book._isbn_counter += 1
