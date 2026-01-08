import sys
import json
import os
from datetime import datetime

FILENAME = "tasks.json"


# Ensure JSON file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)


def load_tasks():
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(description):
    tasks = load_tasks()
    task_id = get_next_id(tasks)

    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Error: Task not found.")


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print("Error: Task not found.")
        return

    save_tasks(updated_tasks)
    print("Task deleted successfully.")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}.")
            return
    print("Error: Task not found.")


def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  task-cli add \"description\"")
        print("  task-cli update <id> \"description\"")
        print("  task-cli delete <id>")
        print("  task-cli mark-in-progress <id>")
        print("  task-cli mark-done <id>")
        print("  task-cli list [todo|in-progress|done]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(" ".join(sys.argv[2:]))

        elif command == "update":
            update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))

        elif command == "delete":
            delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress":
            mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            if len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                list_tasks()

        else:
            print("Error: Unknown command.")

    except (IndexError, ValueError):
        print("Error: Invalid arguments.")


if __name__ == "__main__":
    main()
