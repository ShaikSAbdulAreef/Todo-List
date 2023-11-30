class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = False
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' removed successfully.")
        else:
            print(f"Task '{task}' not found.")

    def mark_as_done(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"Task '{task}' marked as done.")
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task, completed in self.tasks.items():
                status = "Done" if completed else "Not Done"
                print(f"- {task} ({status})")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark as Done")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input("Enter task to mark as done: ")
            todo_list.mark_as_done(task)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the Todo List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
