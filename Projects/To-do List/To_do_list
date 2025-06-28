""" Here is the main class of the program, including the main functionality and contact with user """

from list_of_tasks import List
from user_management import UserManagement

print("Welcome to my 'To-do List', in this program, you can:")
print("1. Create a new user.")
print("2. Create a new task.")
print("3. Delete a task.")
print("4. Modify a task.")
print("5. Show the current tasks.")
print("6. Show the current users.\n")

# Create the "database" to use the functions for the user
users_database: UserManagement = UserManagement()

while True:
    print("* To use the app, you must create a new user. Do you want to proceed? (y/n)")
    answer: str = input("Proceed: ")

    if answer not in ["y", "n"]:
        print("Invalid input. Please try again.")
        continue

    if answer == "y":
        users_database.create_new_user()
        break

    if answer == "n":
        print("\n* To use this app you need an account. Thank you for using the program.")
        exit()

print("\nGreat! Type the title of the list of tasks. For example: 'work', 'college', etc.")
list_title: str = input("Title: ")
# The same as the user "database"
tasks_database: List = List(list_title)

while True:
    print("\n1. Create a new task.")
    print("2. Delete a task.")
    print("3. Modify a task.")
    print("4. Show the current tasks.")
    print("5. Show the current users.")
    print("6. Exit.\n")

    option: str = input("Please select an option (1-6): ")

    if not option in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid input. Please try again.\n")
        continue

    if option == "6":
        print("Thank you for using the app!")
        exit()

    match option:
        case "1":
            tasks_database.add_task()
        case "2":
            tasks_database.delete_task()
        case "3":
            tasks_database.modify_task()
        case "4":
            tasks_database.show_tasks()
        case "5":
            users_database.show_users()

    option: str = input("\nDo you want to do another operation? (y/n): ")

    if option == "n":
        print("Thank you for using the app!")
        exit()

    if option == "y":
        continue
