
import os

FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            t = input("Enter task: ")
            tasks.append(t)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
            idx = int(input("Enter task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
