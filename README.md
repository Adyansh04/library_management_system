# Library Management System

## Overview

The Library Management System is a Python-based project that allows users to manage a library's inventory of books and users. It provides functionalities to add, update, list, search, and delete books and users, as well as to check out and check in books.

## Features

1. **Add Book**: Add new books to the library inventory.
2. **List Books**: Display all books available in the library.
3. **Search Book**: Search for books by title, author, or ISBN.
4. **Update Book**: Update the details of an existing book.
5. **Delete Book**: Remove a book from the library inventory.
6. **Add User**: Add new users to the library system.
7. **List Users**: Display all users registered in the library system.
8. **Search User**: Search for users by name or user ID.
9. **Update User**: Update the details of an existing user.
10. **Delete User**: Remove a user from the library system.
11. **Checkout Book**: Check out a book to a user.
12. **Checkin Book**: Check in a book that was checked out.

## Project Structure

```bash
library-management-system/
├── main.py
├── models.py
├── storage.py
├── logger.py
├── book.py
├── user.py
├── check.py
├── books.json
├── users.json
└── library.log
```

### `main.py`

This is the entry point of the application. It contains the main menu and handles user inputs to interact with the system.

### `models.py`

Contains the `Book` and `User` classes which represent the books and users in the library system.

### `storage.py`

Handles the storage and retrieval of books and users data from JSON files.

### `logger.py`

Configures and handles logging of various operations in the system.

### `book.py`

Contains the `BookManager` class that manages operations related to books such as adding, listing, searching, updating, and deleting books.

### `user.py`

Contains the `UserManager` class that manages operations related to users such as adding, listing, searching, updating, and deleting users.

### `check.py`

Contains the `CheckoutManager` class that handles the checkout and checkin of books.

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Adyansh04/library_management_system.git
    cd library_management_system
    ```

2. **Ensure you have Python installed (version 3.6 or higher).**

3. **Run the application:**
    ```bash
    python main.py
    ```

## Usage

Upon running `main.py`, you will be presented with a menu that allows you to select various options for managing books and users in the library.

### Adding a Book

1. Select the option `1. Add Book`.
2. Enter the title, author, and ISBN of the book.
3. The book will be added to the library inventory.

### Listing All Books

1. Select the option `2. List Books`.
2. All books in the library will be displayed.

### Searching for a Book

1. Select the option `3. Search Book`.
2. Choose to search by title, author, or ISBN.
3. Enter the search value.
4. Matching books will be displayed.

### Updating a Book

1. Select the option `4. Update Book`.
2. Enter the ISBN of the book to update.
3. Enter the new title, author, and availability status (leave blank to keep current values).
4. The book details will be updated.

### Deleting a Book

1. Select the option `5. Delete Book`.
2. Enter the ISBN of the book to delete.
3. The book will be removed from the library inventory.

### Adding a User

1. Select the option `6. Add User`.
2. Enter the name and user ID of the user.
3. The user will be added to the library system.

### Listing All Users

1. Select the option `7. List Users`.
2. All users in the library system will be displayed.

### Searching for a User

1. Select the option `8. Search User`.
2. Choose to search by name or user ID.
3. Enter the search value.
4. Matching users will be displayed.

### Updating a User

1. Select the option `9. Update User`.
2. Enter the user ID of the user to update.
3. Enter the new name (leave blank to keep current value).
4. The user details will be updated.

### Deleting a User

1. Select the option `10. Delete User`.
2. Enter the user ID of the user to delete.
3. The user will be removed from the library system.

### Checking Out a Book

1. Select the option `11. Checkout Book`.
2. Enter the user ID and ISBN of the book to checkout.
3. The book will be checked out to the user.

### Checking In a Book

1. Select the option `12. Checkin Book`.
2. Enter the ISBN of the book to checkin.
3. The book will be marked as available in the library inventory.

### Exiting the Application

1. Select the option `13. Exit`.
2. The application will close.

## Logging

All operations performed in the system are logged to the `library.log` file for tracking and debugging purposes.

