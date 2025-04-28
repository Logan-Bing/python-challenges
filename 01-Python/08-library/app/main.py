from user import User
from book import Book
from library import Library

library = Library()

logan = User("logan")
julia = User("julia")
book1 = Book("coder proprement", "Robert")

library.add_reader(logan)
library.add_reader(julia)
library.add_book(book1)

library.borrow_book(logan, book1)
logan.display_borrowed_books()
library.return_book(logan, book1)

library.borrow_book(julia, book1)
julia.display_borrowed_books()

logan.display_borrowed_books()
