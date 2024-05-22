from book import BookManager
from user import UserManager
from check import CheckoutManager
from logger import Logger

def main_menu():
    # Displays the main menu options for the Library Management System
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add User")
    print("7. List Users")
    print("8. Search User")
    print("9. Update User")
    print("10. Delete User")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    # Initializes the book manager, user manager, and checkout manager
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager(book_manager, user_manager)

    # Main loop for the Library Management System
    while True:
        choice = main_menu()
        if choice == '1':
            # Adds a new book to the library
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            
        elif choice == '2':
            # Lists all the books in the library
            book_manager.list_books()
            
        elif choice == '3':
            # Searches for a book based on a given attribute (title, author, or ISBN)
            attribute = input("Search by (title, author, isbn): ").strip().lower()
            
            if attribute not in ['title', 'author', 'isbn']:
                print("Invalid attribute. Please choose 'title', 'author', or 'isbn'.")
                continue
            
            value = input(f"Enter {attribute}: ").strip()
            results = book_manager.search_books(attribute, value)
            
            if results:
                for book in results:
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}")
            else:
                print("No books found.")
                
        elif choice == '4':
            # Updates the details of a book based on its ISBN
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (or leave blank to keep current): ")
            author = input("Enter new author (or leave blank to keep current): ")
            available = input("Is the book available? (yes/no): ")
            available = True if available.lower() == 'yes' else None if available == '' else False
            book_manager.update_book(isbn, title, author, available)
            
        elif choice == '5':
            # Deletes a book from the library based on its ISBN
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            
        elif choice == '6':
            # Adds a new user to the library system
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            
        elif choice == '7':
            # Lists all the users in the library system
            user_manager.list_users()
            
        elif choice == '8':
            # Searches for a user based on a given attribute (name or user ID)
            attribute = input("Search by (name, user_id): ").strip().lower()
            
            if attribute not in ['name', 'user_id']:
                print("Invalid attribute. Please choose 'name' or 'user_id'.")
                continue
            
            value = input(f"Enter {attribute}: ").strip()
            results = user_manager.search_users(attribute, value)
            
            if results:
                for user in results:
                    print(f"Name: {user.name}, User ID: {user.user_id}")
            else:
                print("No users found.")
                
        elif choice == '9':
            # Updates the details of a user based on their user ID
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (or leave blank to keep current): ")
            user_manager.update_user(user_id, name)
            
        elif choice == '10':
            # Deletes a user from the library system based on their user ID
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
            
        elif choice == '11':
            # Checks out a book for a user based on their user ID and the book's ISBN
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
            
        elif choice == '12':
            # Checks in a book based on its ISBN
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(isbn)
            
        elif choice == '13':
            # Exits the program
            print("Exiting.")
            Logger.log("Application exited.")
            break
    
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
