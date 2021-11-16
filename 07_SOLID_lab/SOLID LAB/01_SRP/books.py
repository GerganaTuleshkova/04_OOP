class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"This book title is '{self.title}' and it is written by {self.author}"


class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book: Book):
        if book in self.books:
            return
        self.books.append(book)

    def find_book(self, title):
        for book_obj in self.books:
            if book_obj.title == title:
                return book_obj


book1 = Book("War and peace", "Leo Tolstoy")
library = Library("Local public", "Main str, New York")
library.add_book(book1)
print(library.find_book("War and peace"))
