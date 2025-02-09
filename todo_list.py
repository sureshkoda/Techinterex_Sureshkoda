import json

# In-memory task storage to avoid file I/O errors in restricted environments
tasks = []

def load_tasks():
    """Simulate loading tasks from storage."""
    global tasks
    tasks = []  # Start with an empty list since file I/O is restricted

def save_tasks():
    """Simulate saving tasks to storage."""
    print("Tasks saved (not persisted due to environment restrictions).")

def add_task(title):
    """Add a new task to the list."""
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'completed': False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "✔️" if task['completed'] else "❌"
        print(f"{task['id']}: {task['title']} [{status}]")

def update_task(task_id):
    """Toggle the completion status of a task."""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            print(f"Task '{task['title']}' status updated!")
            return
    print("Task ID not found!")

def delete_task(task_id):
    """Delete a task based on its ID."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task ID {task_id} deleted!")

def get_user_input(prompt):
    """Handle user input safely."""
    try:
        return input(prompt)
    except OSError:
        print("Input operation failed due to environment restrictions.")
        return None

def main():
    load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = get_user_input("Choose an option: ")
        if choice is None:
            break
        
        if choice == '1':
            title = get_user_input("Enter task title: ")
            if title:
                add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = get_user_input("Enter task ID to update: ")
            if task_id and task_id.isdigit():
                update_task(int(task_id))
        elif choice == '4':
            task_id = get_user_input("Enter task ID to delete: ")
            if task_id and task_id.isdigit():
                delete_task(int(task_id))
        elif choice == '5':
            save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
