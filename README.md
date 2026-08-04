# task_tracker
A simple task tracker in python

## Description
A command-line task tracker application that helps you manage your study tasks. Track your tasks, set priorities, mark them as complete, and delete them when needed.

## Features
- **View Tasks** - Display all your tasks with their priority levels and completion status
- **Add Tasks** - Create new tasks with custom names and priority levels (High, Medium, Low)
- **Mark Complete** - Mark tasks as done
- **Delete Tasks** - Remove tasks you no longer need
- **Persistent Storage** - All tasks are saved to a JSON file so they persist between sessions

## Installation
1. Clone the repository:
```bash
git clone https://github.com/LaMyaHardy3/task_tracker.git
cd task_tracker
```

2. Ensure you have Python 3 installed on your system

## Usage
Run the application:
```bash
python task_tracker.py
```

The application will display a menu with the following options:

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
- `task_tracker.py` - Main application file
- `tasks.json` - Auto-generated file storing your tasks (created after first use)

## Example Workflow
1. Run `python task_tracker.py`
2. Select option `2` to add a new task
3. Enter task name: `Study Python`
4. Enter priority: `High`
5. Select option `1` to view all tasks
6. Select option `3` to mark a task as complete
7. Select option `5` to exit

Your tasks are automatically saved and will be available the next time you run the application!
