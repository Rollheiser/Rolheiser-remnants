""" This is the main logic of the program, where it can create a new task, modify it or delete it
    as well as receive user input and return the desired data. """

from task import Task
from queue import PriorityQueue
import re

# This function returns a number according to the priority,
# so it can be used in the priority queue
def get_priority_value(priority: str) -> int:
    if priority == "high":
        return 1
    elif priority == "medium":
        return 2
    else:
        return 3

class List:
    def __init__(self, title: str):
        self.title: str = title
        self.list_of_tasks: dict = {}
        self.amount_of_tasks: int = 0

    def add_task(self):
        date_pattern = re.compile(r'(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}')

        print("=" * 50)
        number_of_tasks: int = int(input("How many tasks do you wish to create?: "))
        print("\n")

        for i in range(number_of_tasks):
            print("Task #", i + 1)
            print("\n")
            title: str = input("Enter the title of the task: ")
            print("\n")
            description: str = input("Enter the description of the task: ")
            print("\n")
            date: str = input("Enter the date of the task (enter a valid date, such as MM-DD-YYYY): ")
            print("\n")

            if not date_pattern.match(date):
                print("Invalid date. Please enter a valid date.")
                continue

            priority_level: str = input("How important is this task? (low, medium, high): ").lower()
            print("\n")

            new_task: Task = Task(title, description, date, priority_level, False)

            if title not in self.list_of_tasks:
                self.list_of_tasks[title] = new_task
                self.amount_of_tasks += 1
            else:
                print("This task already exists.\n")
        print("=" * 50)

    def delete_task(self):
        print("=" * 58)
        print("To delete a task, enter the task's title. Please type it correctly (including apostrophes and punctuation).\n")
        task_title: str = input("Task's title: ").lower()

        if task_title not in self.list_of_tasks:
            print("This task does not exist.\n")
            return

        del self.list_of_tasks[task_title]
        print("Task has been deleted.\n")
        print("=" * 58)
        self.amount_of_tasks -= 1

    def modify_task(self):
        print("=" * 45)
        task_title = input("Enter the title of the task you want to modify (Type it correctly, including upper and lowercase): ")

        if task_title not in self.list_of_tasks:
            print("That task does not exist.\n")
            return

        task = self.list_of_tasks[task_title]

        print("\nWhat would you like to modify?")
        print("1. Title")
        print("2. Description")
        print("3. Date")
        print("4. Priority")
        print("5. Completed status\n")

        option: str = input("Select an option (1-5): ")

        if option not in ["1", "2", "3", "4", "5"]:
            print("Invalid input.")
            return

        match option:
            case "1":
                new_title = input("Enter the new title: ")
                if new_title in self.list_of_tasks:
                    print("A task with that title already exists.")
                    return

                # Updates the key in the dictionary
                self.list_of_tasks[new_title] = task
                del self.list_of_tasks[task_title]
                task.title = new_title
                print("Title updated successfully.")

            case "2":
                new_description = input("Enter the new description: ")
                task.description = new_description
                print("Description updated successfully.")

            case "3":
                date_pattern = re.compile(r'(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}')

                new_date = input("Enter the new date (MM-DD-YYYY): ")

                if date_pattern.match(new_date):
                    print("Invalid date.")
                    return

                task.date = new_date
                print("Date updated successfully.")

            case "4":
                new_priority = input("Enter the new priority (low, medium, high): ").lower()

                if new_priority not in ["low", "medium", "high"]:
                    print("Invalid priority.")
                    return

                task.priority_level = new_priority
                print("Priority updated successfully.")

            case "5":
                new_status = input("The task is 'pending' or 'completed'?: ").lower()
                if new_status not in ["pending", "completed"]:
                    print("Invalid status.")
                    return

                task.status = new_status
                print("Status updated successfully.")
        print("=" * 45)

    def show_tasks(self):
        if not self.list_of_tasks:
            print("There are no tasks yet.\n")
            return
        # I use a priority queue so I can use the function of data structure, for instance,
        # showing the tasks according to their priority levels
        priority_queue = PriorityQueue()

        for task in self.list_of_tasks.values():
            priority_value: int = get_priority_value(task.priority_level)
            priority_queue.put((priority_value, task))

        print("=" * 50)
        index: int = 1
        while not priority_queue.empty():
            _, task = priority_queue.get()

            print(f"{index}. Title: {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Date: {task.date}")
            print(f"   Priority: {task.priority_level}")
            print(f"   Completed: {task.return_task_status()}\n")

            index += 1
        print("=" * 50)
