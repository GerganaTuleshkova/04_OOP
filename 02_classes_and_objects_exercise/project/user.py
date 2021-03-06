class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):

        for user, books_dict in library.rented_books.items():
            if book_name in books_dict:
                return f'The book "{book_name}" is already rented and will be available in ' \
                       f'{library.rented_books[user][book_name]} days!'
        if author not in library.books_available:
            return

        if book_name not in library.books_available[author]:
            return
        self.books.append(book_name)
        library.books_available[author].remove(book_name)
        if self.username not in library.rented_books:
            library.rented_books[self.username] = {}
        library.rented_books[self.username][book_name] = days_to_return
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        if author not in library.books_available:
            library.books_available[author] = []
        library.books_available[author].append(book_name)

        del library.rented_books[self.username][book_name]

    def info(self):
        books_rented = sorted(self.books)
        return f"{', '.join(books_rented)}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {sorted(self.books)}"

