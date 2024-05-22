import json
import os
from models import Book, User

class Storage:
    @staticmethod
    def save_books(books, filename='books.json'):
        """
        Save a list of books to a JSON file.

        Args:
            books (list): List of Book objects to be saved.
            filename (str): Name of the JSON file to save the books to. Default is 'books.json'.
        """
        with open(filename, 'w') as f:                                        # Open the file in write mode
            json.dump([book.to_dict() for book in books], f, indent=4)        # Write the list of book objects to the file

    @staticmethod
    def load_books(filename='books.json'):
        """
        Load a list of books from a JSON file.

        Args:
            filename (str): Name of the JSON file to load the books from. Default is 'books.json'.

        Returns:
            list: List of Book objects loaded from the JSON file.
        """
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:      # Check if the file exists and is not empty
            return []
        with open(filename, 'r') as f:                                           # Open the file in read mode
            try:                                                                # Try to load the data from the file
                return [Book.from_dict(data) for data in json.load(f)]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_users(users, filename='users.json'):
        """
        Save a list of users to a JSON file.

        Args:
            users (list): List of User objects to be saved.
            filename (str): Name of the JSON file to save the users to. Default is 'users.json'.
        """
        with open(filename, 'w') as f:                                  # Open the file in write mode
            json.dump([user.to_dict() for user in users], f, indent=4)  # Write the list of user objects to the file

    @staticmethod
    def load_users(filename='users.json'):
        """
        Load a list of users from a JSON file.

        Args:
            filename (str): Name of the JSON file to load the users from. Default is 'users.json'.

        Returns:
            list: List of User objects loaded from the JSON file.
        """
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:       # Check if the file exists and is not empty
            return []
        with open(filename, 'r') as f:                                           # Open the file in read mode
            try:                                                                 # Try to load the data from the file
                return [User.from_dict(data) for data in json.load(f)]
            except json.JSONDecodeError:
                return []
