class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            isbn=data.get("isbn"),
            available=data.get("available", True)
        )

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            user_id=data.get("user_id")
        )
