# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize the base Book class with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with base attributes and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a readable string representation of the EBook."""
        return f"EBook: '{self.title}' by {self.author}, File size: {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with base attributes and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a readable string representation of the PrintBook."""
        return f"PrintBook: '{self.title}' by {self.author}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize an empty library collection."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(f" - {book}")
