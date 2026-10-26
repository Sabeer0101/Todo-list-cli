"""
To-Do List (CLI)
Author: Sabeer

Command-line task manager. Tasks JSON file me save hote hain,
isliye program band karne ke baad bhi data bacha rehta hai.
Features: add, view, complete, edit, delete, search, clear completed.
"""

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


# ---------- File handling ----------

def load_tasks():
    """File se tasks padhta hai. File nahi hai ya kharab hai to empty list deta hai."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read tasks file. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Tasks ko file me save karta hai."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def next_id(tasks):
    """Naye task ke liye unique id banata hai."""
    return max((t["id"] for t in tasks), default=0) + 1


# ---------- Input helpers ----------

def ask_task_id(tasks, prompt):
    """Valid task id leta hai. Galat input par None return karta hai."""
    value = input(prompt).strip()
    if not value.isdigit():
        print("Please enter a valid task number.")
        return None
    task_id = int(value)
    if not any(t["id"] == task_id for t in tasks):
        print(f"No task found with id {task_id}.")
        return None
    return task_id


def find_task(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


# ---------- Features ----------

PRIORITIES = {"1": "High", "2": "Medium", "3": "Low"}


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    print("Priority: 1. High  2. Medium  3. Low")
    choice = input("Choose (default 2): ").strip()
    priority = PRIORITIES.get(choice, "Medium")

    tasks.append({
        "id": next_id(tasks),
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%d-%m-%Y %H:%M"),
    })
    save_tasks(tasks)
    print(f"Added: '{title}' ({priority} priority)")


def show_tasks(tasks, items=None):
    items = tasks if items is None else items
    if not items:
        print("\nNo tasks to show.")
        return

    print("\n" + "-" * 62)
    print(f"{'ID':<4}{'Status':<8}{'Priority':<10}{'Title':<30}{'Created'}")
    print("-" * 62)
    for t in items:
        status = "[x]" if t["done"] else "[ ]"
        title = t["title"] if len(t["title"]) <= 27 else t["title"][:26] + "…"
        print(f"{t['id']:<4}{status:<8}{t['priority']:<10}{title:<30}{t['created']}")
    print("-" * 62)

    done = sum(1 for t in tasks if t["done"])
    print(f"Completed: {done}/{len(tasks)}")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    task_id = ask_task_id(tasks, "Task id to mark as done: ")
    if task_id is None:
        return
    task = find_task(tasks, task_id)
    task["done"] = True
    save_tasks(tasks)
    print(f"Marked as done: '{task['title']}'")


def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    task_id = ask_task_id(tasks, "Task id to edit: ")
    if task_id is None:
        return
    task = find_task(tasks, task_id)
    new_title = input(f"New title (Enter to keep '{task['title']}'): ").strip()
    if new_title:
        task["title"] = new_title
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("No changes made.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    task_id = ask_task_id(tasks, "Task id to delete: ")
    if task_id is None:
        return
    task = find_task(tasks, task_id)
    confirm = input(f"Delete '{task['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Cancelled.")


def search_tasks(tasks):
    keyword = input("Search keyword: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.")
        return
    matches = [t for t in tasks if keyword in t["title"].lower()]
    show_tasks(tasks, matches)


def clear_completed(tasks):
    done_count = sum(1 for t in tasks if t["done"])
    if done_count == 0:
        print("No completed tasks to clear.")
        return
    confirm = input(f"Remove {done_count} completed task(s)? (y/n): ").strip().lower()
    if confirm == "y":
        tasks[:] = [t for t in tasks if not t["done"]]
        save_tasks(tasks)
        print("Completed tasks cleared.")


# ---------- Main menu ----------

MENU = """
========== TO-DO LIST ==========
1. Add task
2. View all tasks
3. Mark task as done
4. Edit task
5. Delete task
6. Search tasks
7. Clear completed tasks
8. Exit
================================"""


def main():
    tasks = load_tasks()
    actions = {
        "1": add_task,
        "2": show_tasks,
        "3": complete_task,
        "4": edit_task,
        "5": delete_task,
        "6": search_tasks,
        "7": clear_completed,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Goodbye! Keep getting things done.")
            break
        action = actions.get(choice)
        if action:
            action(tasks)
        else:
            print("Invalid choice! Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
