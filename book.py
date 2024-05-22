from models import Book
from storage import Storage
from logger import Logger

class BookManager:
    """
    The BookManager class manages the operations related to books in the library management system.
    """

    def __init__(self):
        """
        Initializes a new instance of the BookManager class.
        """
        self.books = Storage.load_books()

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.

        Returns:
            None
        """
        if not title or not author or not isbn:         # Check if all fields are provided
            print("All fields are required.")
            return
        if self.find_book_by_isbn(isbn):                # Check if a book with the same ISBN already exists
            print("A book with this ISBN already exists.")
            return

        # Create a new book object and add it to the list of books
        new_book = Book(title, author, isbn)            
        self.books.append(new_book)
        Storage.save_books(self.books)
        Logger.log(f"Book added: {title}, {author}, {isbn}")
        print("Book added successfully.")

    def list_books(self):
        """
        Lists all the books in the library.

        Returns:
            None
        """
        if not self.books:                     # Check if there are no books available
            print("No books available.")
            return

        # Print the details of each book in a formatted manner
        print(f'{"Title":<25} {"Author":<25} {"ISBN":<20} {"Available":<15}')

        for book in self.books:
            print(f'{book.title:<25} {book.author:<25} {book.isbn:<20} {str(book.available):<15}')

    def find_book_by_isbn(self, isbn):
        """
        Finds a book in the library by its ISBN.

        Args:
            isbn (str): The ISBN of the book to find.

        Returns:
            Book or None: The book object if found, None otherwise.
        """
        for book in self.books:     
            if book.isbn == isbn:
                return book
        return None

    def search_books(self, attribute, value):
        """
        Searches for books in the library based on a specific attribute and value.

        Args:
            attribute (str): The attribute to search for (e.g., "title", "author").
            value (str): The value to search for.

        Returns:
            list: A list of books that match the search criteria.
        """
        results = [book for book in self.books if getattr(book, attribute, "").lower() == value.lower()]
        return results

    def update_book(self, isbn, title=None, author=None, available=None):
        """
        Updates the details of a book in the library.

        Args:
            isbn (str): The ISBN of the book to update.
            title (str, optional): The new title of the book. Defaults to None.
            author (str, optional): The new author of the book. Defaults to None.
            available (bool, optional): The new availability status of the book. Defaults to None.

        Returns:
            bool: True if the book was updated successfully, False otherwise.
        """
        book = self.find_book_by_isbn(isbn)
        if book:        # Check if the book exists
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
        """
        Deletes a book from the library.

        Args:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if the book was deleted successfully, False otherwise.
        """
        book = self.find_book_by_isbn(isbn)
        if book:        # Check if the book exists
            self.books.remove(book)
            Storage.save_books(self.books)
            Logger.log(f"Book deleted: {isbn}")
            print("Book deleted successfully.")
            return True
        print("Book not found.")
        return False
