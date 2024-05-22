class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author, isbn, available=True):
        """
        Initializes a new instance of the Book class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
            available (bool, optional): Indicates if the book is available. Defaults to True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        """
        Converts the book object to a dictionary.

        Returns:
            dict: A dictionary representation of the book object.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a new instance of the Book class from a dictionary.

        Args:
            data (dict): A dictionary containing the book data.

        Returns:
            Book: A new instance of the Book class.
        """
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            isbn=data.get("isbn"),
            available=data.get("available", True)
        )


class User:
    """
    Represents a user in the library system.
    """

    def __init__(self, name, user_id):
        """
        Initializes a new instance of the User class.

        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier of the user.
        """
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """
        Converts the user object to a dictionary.

        Returns:
            dict: A dictionary representation of the user object.
        """
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a new instance of the User class from a dictionary.

        Args:
            data (dict): A dictionary containing the user data.

        Returns:
            User: A new instance of the User class.
        """
        return cls(
            name=data.get("name"),
            user_id=data.get("user_id")
        )
