import json
import os
from models import Book, User

class Storage:
    @staticmethod
    def save_books(books, filename='books.json'):
        with open(filename, 'w') as f:
            json.dump([book.to_dict() for book in books], f, indent=4)

    @staticmethod
    def load_books(filename='books.json'):
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return []
        with open(filename, 'r') as f:
            try:
                return [Book.from_dict(data) for data in json.load(f)]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_users(users, filename='users.json'):
        with open(filename, 'w') as f:
            json.dump([user.to_dict() for user in users], f, indent=4)

    @staticmethod
    def load_users(filename='users.json'):
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return []
        with open(filename, 'r') as f:
            try:
                return [User.from_dict(data) for data in json.load(f)]
            except json.JSONDecodeError:
                return []
