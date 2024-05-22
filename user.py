from models import User
from storage import Storage
from logger import Logger

class UserManager:
    """
    Class to manage users in the library management system.
    """

    def __init__(self):
        """
        Initializes a new instance of the UserManager class.
        """
        self.users = Storage.load_users()

    def add_user(self, name, user_id):
        """
        Adds a new user to the system.

        Args:
            name (str): The name of the user.
            user_id (int): The ID of the user.

        Returns:
            None
        """
        # Check if all fields are provided
        if not name or not user_id:
            print("All fields are required.")
            return
        if self.find_user_by_id(user_id):
            print("A user with this ID already exists.")
            return

        # Create a new user object and add it to the list of users
        new_user = User(name, user_id)
        self.users.append(new_user)
        Storage.save_users(self.users)
        Logger.log(f"User added: {name}, {user_id}")
        print("User added successfully.")

    def list_users(self):
        """
        Lists all the users in the system.

        Returns:
            None
        """
        if not self.users:               # Check if there are no users available
            print("No users available.")
            return

        # Print the details of each user in a formatted manner
        print(f'{"Name":<20} {"User ID":<20}')

        for user in self.users:
            print(f'{user.name:<20} {user.user_id:<20}')

    def find_user_by_id(self, user_id):
        """
        Finds a user by their ID.

        Args:
            user_id (int): The ID of the user to find.

        Returns:
            User or None: The user object if found, None otherwise.
        """
        for user in self.users:     # Iterate through the list of users
            if user.user_id == user_id:
                return user
        return None

    def search_users(self, attribute, value):
        """
        Searches for users based on a specific attribute and value.

        Args:
            attribute (str): The attribute to search for (e.g., "name", "user_id").
            value (str): The value to search for.

        Returns:
            list: A list of users that match the search criteria.
        """
        results = [user for user in self.users if getattr(user, attribute, "").lower() == value.lower()]
        return results

    def update_user(self, user_id, name=None):
        """
        Updates the information of a user.

        Args:
            user_id (int): The ID of the user to update.
            name (str, optional): The new name of the user. Defaults to None.

        Returns:
            bool: True if the user was updated successfully, False otherwise.
        """
        user = self.find_user_by_id(user_id)
        if user:        # Check if the user exists
            if name:
                user.name = name
            Storage.save_users(self.users)
            Logger.log(f"User updated: {user_id}")
            print("User updated successfully.")
            return True
        print("User not found.")
        return False

    def delete_user(self, user_id):
        """
        Deletes a user from the system.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted successfully, False otherwise.
        """
        user = self.find_user_by_id(user_id)
        if user:        # Check if the user exists
            self.users.remove(user)
            Storage.save_users(self.users)
            Logger.log(f"User deleted: {user_id}")
            print("User deleted successfully.")
            return True
        print("User not found.")
        return False
