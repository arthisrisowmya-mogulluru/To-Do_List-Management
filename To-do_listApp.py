import pickle

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.description} [{self.status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully!")

    def delete_task(self, index):
        if index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid index!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index+1}. {task}")

    def save_tasks(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)
        print(f"Tasks saved to {filename} successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
            print(f"Tasks loaded from {filename} successfully!")
        except FileNotFoundError:
            print(f"File {filename} not found!")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List App ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            print("\n--- Task List ---")
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter the filename to save tasks to: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter the filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            print("Thank you for using the ToDo List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
