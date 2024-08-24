import os

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task, status = line.strip().split(',')
                tasks.append({"task": task, "status": status == 'True'})
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['status']}\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['status'] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "status": False})
    print(f"Task '{task}' added.")

def mark_task(tasks):
    try:
        task_number = int(input("Enter the task number to mark as done/undone: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]['status'] = not tasks[task_number]['status']
            status = "Done" if tasks[task_number]['status'] else "Not Done"
            print(f"Task '{tasks[task_number]['task']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    try:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    tasks = load_tasks("tasks.txt")
    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done/undone")
        print("4. Remove a task")
        print("5. Save and exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks("tasks.txt", tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
