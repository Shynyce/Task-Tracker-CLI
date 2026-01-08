# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage your tasks, built with Python. This project follows the [roadmap.sh](https://roadmap.sh/projects/task-tracker) backend project requirements.

## Features
- **Add** tasks with a description.
- **List** all tasks or filter by status (todo, in-progress, done).
- **Update** task descriptions or status.
- **Delete** tasks by ID.
- **Persistence**: Tasks are saved locally in a `tasks.json` file.

## How to Run

### Prerequisites
- Python 3.x installed.

### Commands
1. **Add a task**:
   ```bash
   python3 task_tracker.py add "Finish my project"

 * List all tasks:
   python3 task_tracker.py list

 * Mark a task as in-progress:
   python3 task_tracker.py mark-in-progress 1

 * Mark a task as done:
   python3 task_tracker.py mark-done 1

 * Delete a task:
   python3 task_tracker.py delete 1

<!-- end list -->