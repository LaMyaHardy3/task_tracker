# task_tracker
A simple task tracker in python

## Description
A command-line and web-based task tracker application that helps you manage your study tasks. Track your tasks, set priorities, mark them as complete, and delete them when needed.

## Live Website
- https://moonlight-task-arcade.onrender.com/

## Features
- **View Tasks** - Display all your tasks with their priority levels and completion status
- **Add Tasks** - Create new tasks with custom names and priority levels (High, Medium, Low)
- **Mark Complete** - Mark tasks as done
- **Delete Tasks** - Remove tasks you no longer need
- **Persistent Storage** - All tasks are saved to a JSON file so they persist between sessions
- **Web UI (Moonlight Task Arcade)** - A Flask-powered browser interface for managing tasks visually

## Installation
1. Clone the repository:
```bash
git clone https://github.com/LaMyaHardy3/task_tracker.git
cd task_tracker
```

2. Ensure you have Python 3 installed on your system

## Usage

### Command-line app
Run the application:
```bash
python task_tracker.py
```

### Web app (Moonlight Task Arcade)
Run the Flask app:
```bash
python moonlight-task-arcade/app.py
```

Then open your browser to:
- http://127.0.0.1:5000

The command-line application will display a menu with the following options:

```
Study Task Tracker
1. View Tasks
2. Add Tasks
3. Complete Tasks
4. Delete Tasks
5. EXIT
```

### Menu Options

**1. View Tasks** - Shows all your current tasks with:
- Task number
- Task name
- Priority level (High, Medium, Low)
- Status (Done or Not done)

**2. Add Tasks** - Create a new task by entering:
- Task name (what you want to do)
- Priority (High, Medium, or Low)

**3. Complete Tasks** - Mark an existing task as complete:
- View your tasks
- Enter the task number you want to mark as done

**4. Delete Tasks** - Remove a task by entering its task number

**5. EXIT** - Close the application

## File Structure
- `task_tracker.py` - Command-line application file
- `moonlight-task-arcade/app.py` - Flask web application file
- `tasks.json` - Auto-generated file storing your tasks (created after first use)

## Example Workflow
1. Run `python task_tracker.py` or `python moonlight-task-arcade/app.py`
2. Add a new task
3. View tasks
4. Mark tasks complete
5. Delete tasks as needed

Your tasks are automatically saved and will be available the next time you run the application!
