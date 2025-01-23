class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task #{task_number} updated to '{new_task}'.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' has been removed.")
        except IndexError:
            print("Invalid task number.")

    def mark_as_complete(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task #{task_number} marked as completed.")
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as complete: "))
                todo_list.mark_as_complete(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
