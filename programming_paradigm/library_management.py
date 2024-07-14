#Define Book class with 3 attributes, title, author, and _is_checked_out
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = []

    def check_out(self):
        if self not in self._is_checked_out:
            self._is_checked_out.append(self)

    def return_book(self):
        if self in self._is_checked_out:
            self._is_checked_out.remove(self)

    def is_available(self):
        return self not in self._is_checked_out

#Define Library class to store instances of book as defined in the Book class
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")