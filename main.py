from book import BookManager
from user import UserManager
from check import CheckoutManager
from logger import Logger

def main_menu():
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
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager(book_manager, user_manager)

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
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
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (or leave blank to keep current): ")
            author = input("Enter new author (or leave blank to keep current): ")
            available = input("Is the book available? (yes/no): ")
            available = True if available.lower() == 'yes' else None if available == '' else False
            book_manager.update_book(isbn, title, author, available)
        elif choice == '5':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
        elif choice == '7':
            user_manager.list_users()
        elif choice == '8':
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
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (or leave blank to keep current): ")
            user_manager.update_user(user_id, name)
        elif choice == '10':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '12':
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(isbn)
        elif choice == '13':
            print("Exiting.")
            Logger.log("Application exited.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
