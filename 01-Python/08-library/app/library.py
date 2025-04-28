

class Library:
    def __init__(self, readers=None, books=None):
        self.readers = readers if readers is not None else []
        self.books = books if books is not None else []

    def borrow_book(self, user, book):
        if user in self.readers and book in self.books and book.available:
            user.borrowed_books.append(book)
            book.available = False

    def return_book(self, user, book):
        if user in self.readers and book in user.borrowed_books:
            user.borrowed_books.remove(book)
            book.available = True

    def add_reader(self, user):
        self.readers.append(user)

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title : {book.title} - Author : {book.author} - Disponible : { 'oui' if book.available else 'non'}")

    def display_readers(self):
        for user in self.readers:
            print(f"Name : {user.name} - Id : {user.id}")
