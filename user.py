from models import User
from storage import Storage
from logger import Logger

class UserManager:
    def __init__(self):
        self.users = Storage.load_users()

    def add_user(self, name, user_id):
        if not name or not user_id:
            print("All fields are required.")
            return
        if self.find_user_by_id(user_id):
            print("A user with this ID already exists.")
            return

        new_user = User(name, user_id)
        self.users.append(new_user)
        Storage.save_users(self.users)
        Logger.log(f"User added: {name}, {user_id}")
        print("User added successfully.")

    def list_users(self):
        if not self.users:
            print("No users available.")
            return

        print(f'{"Name":<20} {"User ID":<20}')

        for user in self.users:
            print(f'{user.name:<20} {user.user_id:<20}')

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def search_users(self, attribute, value):
        results = [user for user in self.users if getattr(user, attribute, "").lower() == value.lower()]
        return results

    def update_user(self, user_id, name=None):
        user = self.find_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            Storage.save_users(self.users)
            Logger.log(f"User updated: {user_id}")
            print("User updated successfully.")
            return True
        print("User not found.")
        return False

    def delete_user(self, user_id):
        user = self.find_user_by_id(user_id)
        if user:
            self.users.remove(user)
            Storage.save_users(self.users)
            Logger.log(f"User deleted: {user_id}")
            print("User deleted successfully.")
            return True
        print("User not found.")
        return False
