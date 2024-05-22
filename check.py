from storage import Storage
from models import Book, User
from logger import Logger

class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        user = self.user_manager.find_user_by_id(user_id)
        book = self.book_manager.find_book_by_isbn(isbn)
        if user and book and book.available:
            book.available = False
            self.checkouts.append({"user_id": user_id, "isbn": isbn})
            Storage.save_books(self.book_manager.books)
            Logger.log(f"Book checked out: User {user_id}, ISBN {isbn}")
            print("Book checked out successfully.")
            return True
        print("Checkout failed. Either the user ID or ISBN is incorrect, or the book is not available.")
        return False

    def checkin_book(self, isbn):
        book = self.book_manager.find_book_by_isbn(isbn)
        if book:
            book.available = True
            self.checkouts = [co for co in self.checkouts if co["isbn"] != isbn]
            Storage.save_books(self.book_manager.books)
            Logger.log(f"Book checked in: ISBN {isbn}")
            print("Book checked in successfully.")
            return True
        print("Checkin failed. The ISBN is incorrect.")
        return False
