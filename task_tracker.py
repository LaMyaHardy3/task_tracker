import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNO tasks yet.\n")
        return

    print("\nYour Tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{number}. {task['name']} | Priotity: {task['priority']} | {status}")

    print()


def add_task(tasks):
    name = input("Task name: ")
    priority = input("Priority (High, Medium, Low): ")

    tasks.append({
        "name": name,
        "priority": priority,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added.\n")


def complete_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("Enter the task number to mark complete: "))
        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.\n")
    except (ValueError, IndexError):
        print("That task number is not valid.\n")


def delete_task(tasks):
    try:
        number = int(input("Enter the task number to delete: "))
        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed_task['name']}\n")
    except (ValueError, IndexError):
        print("That task number is not valid.\n")


def main():
    tasks = load_tasks()

    while True:
        print("Study Task Tracker")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Delete Tasks")
        print("5. EXIT")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! <3")
            break
        else:
            print("Please choose a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
