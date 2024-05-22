from models import Book
from storage import Storage
from logger import Logger

class BookManager:
    def __init__(self):
        self.books = Storage.load_books()

    def add_book(self, title, author, isbn):
        if not title or not author or not isbn:
            print("All fields are required.")
            return
        if self.find_book_by_isbn(isbn):
            print("A book with this ISBN already exists.")
            return

        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        Storage.save_books(self.books)
        Logger.log(f"Book added: {title}, {author}, {isbn}")
        print("Book added successfully.")

    def list_books(self):
        if not self.books:
            print("No books available.")
            return

        print(f'{"Title":<25} {"Author":<25} {"ISBN":<20} {"Available":<15}')

        for book in self.books:
            print(f'{book.title:<25} {book.author:<25} {book.isbn:<20} {str(book.available):<15}')

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_books(self, attribute, value):
        results = [book for book in self.books if getattr(book, attribute, "").lower() == value.lower()]
        return results

    def update_book(self, isbn, title=None, author=None, available=None):
        book = self.find_book_by_isbn(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if available is not None:
                book.available = available
            Storage.save_books(self.books)
            Logger.log(f"Book updated: {isbn}")
            print("Book updated successfully.")
            return True
        print("Book not found.")
        return False

    def delete_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            Storage.save_books(self.books)
            Logger.log(f"Book deleted: {isbn}")
            print("Book deleted successfully.")
            return True
        print("Book not found.")
        return False
