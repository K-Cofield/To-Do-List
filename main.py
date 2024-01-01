# Empty dictionary to hold tasks
tasks = {}


# Function to display menu
def display_menu():
    print("To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


# Function to add a task
def add_task():
    task_name = input("Enter the name of the task: ")
    task_due = input("Enter the due date (MM/DD/YYYY): ")
    task_priority = input("Enter the priority (High/Medium/Low): ")
    task_category = input("Enter the category (Work/Personal/School): ")
    task_details = {'Due Date': task_due, 'Priority': task_priority, 'Category': task_category}
    tasks[task_name.lower()] = task_details


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return

    print("Task List:")
    print("---------------------------------------------------------------------")
    print("{:<20} {:<15} {:<15} {:<15} ".format("Task Name", "Due Date", "Priority", "Category"))
    print("---------------------------------------------------------------------")

    for task, details in tasks.items():
        task_name = task.capitalize()
        task_due = details['Due Date']
        task_priority = details['Priority']
        task_category = details['Category']
        print("{:<20} {:<15} {:<15} {:<15}".format(task_name, task_due, task_priority, task_category,
                                                   ))


# Function to delete a task
def delete_task():
    task_to_delete = input("Enter the name of the task to delete: ").lower()
    if task_to_delete in tasks:
        del tasks[task_to_delete]
        print(f"Deleted {task_to_delete}")
    else:
        print("Task not found.")


# Main program loop
while True:
    choice = display_menu()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

    print("")
