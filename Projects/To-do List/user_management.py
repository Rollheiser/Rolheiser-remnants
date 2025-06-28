"""" This class manages all the functions related to the management of users. """

from user import User

# This function checks if the string has an uppercase letter and lowercase
def check_upplowcase_letters(string: str) -> bool:
    has_uppercase: bool = any(char.isupper() for char in string)
    has_lowercase: bool = any(char.islower() for char in string)

    return has_uppercase and has_lowercase

class UserManagement:
    def __init__(self):
        self.list_of_users: dict = {}
        self.amount_of_users: int = 0

    def create_new_user(self):
        e_mail: str = None
        username: str = None
        password: str = None

        print("=" * 50)
        while True:
            print("\n* The e-mail must be a valid one.")
            e_mail = input("Enter your e-mail: ")

            if not '@' in e_mail or not '.' in e_mail:
                print("Invalid e-mail. Please type a valid e-mail.")
                continue

            print("\n* The username must contain at least 8 characters and lower than 16.")
            username = input("Enter your username: ")

            if len(username) < 8 or len(username) > 16:
                print("The username must be between 8 and 16 characters.")
                continue

            if not check_upplowcase_letters(username):
                print("The username must contain at least one uppercase letter and lowercase letter.")
                continue

            print("\n* The password must contain at least 8 characters. Upper and lowercase letters and numbers.")
            password = input("Enter your password: ")

            if not check_upplowcase_letters(password):
                print("The password must contain at least one uppercase letter and lowercase letter.")
                continue

            if len(password) < 8:
                print("The password is not at least 8 characters.\n")
                continue

            if not password.isalnum():
                print("The password should contain numbers and letters.\n")
                continue

            break
        print("=" * 50)
        self.list_of_users[password] = User(username, e_mail, password)
        self.amount_of_users += 1

    def show_users(self):
        number: int = 0

        print("=" * 60)
        for user in self.list_of_users.values():
            print(f"{number + 1}. Username: {user.name_user}   |  E-mail: {user.email_account}")
            number += 1
        print("=" * 60)
