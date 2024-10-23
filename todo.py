import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['description']} [{status}]")

def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task {index + 1} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['description']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do CLI")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
