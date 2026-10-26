# ✅ To-Do List (CLI)

A command-line task manager built with **Python**. Add tasks, set priorities, mark them done, and your data is saved automatically, so nothing is lost when you close the program.

## ✨ Features

- Add tasks with **High / Medium / Low** priority
- View all tasks in a clean table with status and created time
- Mark tasks as done and see your progress (e.g. `Completed: 3/5`)
- Edit and delete tasks (with delete confirmation)
- Search tasks by keyword
- Clear all completed tasks in one go
- Data saved in a `tasks.json` file (persists between runs)
- Input validation, so wrong input never crashes the program

## 🛠️ Tech Used

![Python](https://img.shields.io/badge/Python-10A37F?style=flat-square&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-0D1117?style=flat-square&logo=json&logoColor=white)

Concepts practiced: functions, dictionaries, lists, list comprehensions, file handling, JSON, exception handling, `datetime`.

## 🚀 How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repo
   ```bash
   git clone https://github.com/Sabeer0101/todo-list-cli.git
   cd todo-list-cli
   ```
3. Run the app
   ```bash
   python todo.py
   ```

## 🎮 Sample Output

```
========== TO-DO LIST ==========
1. Add task
2. View all tasks
3. Mark task as done
4. Edit task
5. Delete task
6. Search tasks
7. Clear completed tasks
8. Exit
================================
Enter your choice (1-8): 2

--------------------------------------------------------------
ID  Status  Priority  Title                         Created
--------------------------------------------------------------
1   [x]     High      Buy milk                      26-10-2026 10:05
2   [ ]     Medium    Study Python                  26-10-2026 10:05
--------------------------------------------------------------
Completed: 1/2
```

## 🔮 Future Improvements

- [ ] Due dates and overdue reminders
- [ ] Sort tasks by priority
- [ ] Categories / tags
- [ ] GUI version using Tkinter

## 👨‍💻 Author

**Sabeer** — [GitHub](https://github.com/Sabeer0101)
