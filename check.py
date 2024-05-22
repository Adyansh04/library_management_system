from storage import Storage
from models import Book, User
from logger import Logger

class CheckoutManager:
    """
    Manages the checkout and checkin of books in the library.

    Attributes:
        book_manager (BookManager): The book manager object.
        user_manager (UserManager): The user manager object.
        checkouts (list): A list of checked out books.

    Methods:
        checkout_book: Checks out a book for a user.
        checkin_book: Checks in a book.
    """

    def __init__(self, book_manager, user_manager):
        """
        Initializes a new instance of the CheckoutManager class.

        Args:
            book_manager (BookManager): The book manager object.
            user_manager (UserManager): The user manager object.
        """
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book for a user.

        Args:
            user_id (int): The ID of the user.
            isbn (str): The ISBN of the book.

        Returns:
            bool: True if the book was checked out successfully, False otherwise.
        """
        # Find the user and book objects
        user = self.user_manager.find_user_by_id(user_id)
        book = self.book_manager.find_book_by_isbn(isbn)
        
        # Check if the user and book exist and the book is available
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
        """
        Checks in a book.

        Args:
            isbn (str): The ISBN of the book.

        Returns:
            bool: True if the book was checked in successfully, False otherwise.
        """
        # Find the book object
        book = self.book_manager.find_book_by_isbn(isbn)
        
        # Check if the book exists and is checked out
        if book:
            book.available = True
            self.checkouts = [co for co in self.checkouts if co["isbn"] != isbn]
            Storage.save_books(self.book_manager.books)
            Logger.log(f"Book checked in: ISBN {isbn}")
            print("Book checked in successfully.")
            return True
        print("Checkin failed. The ISBN is incorrect.")
        return False
