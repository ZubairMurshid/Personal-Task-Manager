#Author: Zubair Murshid
#Date: 16th April 2025

#Tkinter GUI to View, Sort and Filter tasks - Main Program

import json

from tkinter_gui import open_task_viewer # Importing GUI to view tasks


TASKS_FILE = "tasks.txt"
tasklist = []


def load_tasks_from_file():
    """Load tasks from the tasks.txt file into the global tasklist."""
    global tasklist
    try:
        with open(TASKS_FILE, "r") as file:
            tasklist = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasklist=[]


def save_tasks_to_file():
    """Save the current tasklist to the tasks.txt file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasklist, file, indent=4)


def create_task(name, description, priority, due_date):
    """Create a new task and save it to file."""
    task = {
        "name":name,
        "description":description,
        "priority":priority,
        "due_date":due_date
    }
    tasklist.append(task)
    save_tasks_to_file()
    print('Task created successfully!\n')


def view_tasks():
    """Display all current tasks in the terminal."""
    if len(tasklist)==0:
        print('No Tasks available!\n')
        return
    else:
        print('\nYour tasks:\n')
        for i in range(len(tasklist)):
            task=tasklist[i]
            print(f"Task {i+1}: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Priority: {task['priority']}")
            print(f"Due date: {task['due_date']}\n")


def update_task(index, name, description, priority, due_date):
    """Update an existing task at a specific index."""
    if 0<= index <len(tasklist):
        tasklist[index] = {
            "name":name,
            "description":description,
            "priority":priority,
            "due_date":due_date
        }
        save_tasks_to_file()
        print('Task updated successfully!\n')
    else:
        print('Invalid index')
        return


def delete_task(index):
    """Delete a task at a specific index."""
    if 0<=index<len(tasklist):
        del tasklist[index]
        save_tasks_to_file()
        print('Task deleted successfully!\n')
    else:
        print('Invalid index')
        return


if __name__=="__main__":
    load_tasks_from_file()
    while True:
        print('Personal Task Manager')
        print('1. Create Task')
        print('2. View Tasks')
        print('3. Update Task')
        print('4. Delete Task')
        print('5. Quit program')

        choice=input('\nEnter your choice: ').strip()
        
        if choice =="1":
            # Create Task
            while True:
                name=input('\nEnter name of task (or enter exit to return to menu): ').strip()
                if name:
                    break
                print('Name cannot be blank. Try Again')
            if name.lower()=="exit":
                print("Returning to main menu...\n")
                continue
            
            while True:
                description=input('Enter description: ').strip()
                if description:
                    break
                print("Description cannot be blank. Try Again")
                
            while True:
                priority=input('Enter priority (High/Low): ').strip().lower()
                if priority in["high", "low"]:
                    break
                print("Enter valid priority")
                
            while True:
                due_date=input('Enter due date: ').strip()
                if due_date:
                    break
                print('Date cannot be blank')
                
            create_task(name, description, priority, due_date)
        
        elif choice=="2":
            # View Tasks using GUI
            open_task_viewer()
        
        elif choice=="3":
            # Update Task
            view_tasks()
            if len(tasklist)!=0:
                while True:
                    index=input('Enter index of task you wish to update (or enter exit to return to menu): ')
                    if index.lower()=="exit":
                            print('Returning to main menu...\n')
                            break
                    try:
                        index=int(index)-1
                        if 0<=index<len(tasklist):
                            while True:
                                name=input('\nEnter new name of task: ').strip()
                                if name:
                                    break
                                print('Name cannot be blank. Try Again')
                                
                            while True:
                                description=input('Enter description: ').strip()
                                if description:
                                    break
                                print("Description cannot be blank. Try Again")
                                
                            while True:
                                priority=input('Enter priority (High/Low): ').strip().lower()
                                if priority in["high", "low"]:
                                    break
                                print("Enter valid priority")
                                
                            while True:
                                due_date=input('Enter due date: ').strip()
                                if due_date:
                                    break
                                print('Date cannot be blank')
                                
                            update_task(index, name, description, priority, due_date)
                            break
                        else:
                            print("Index doesnt exist. Try Again\n")
                    except ValueError:
                        print("Invalid input. Enter valid index\n")
        
        elif choice=="4":
            #Delete Task
            view_tasks()
            if len(tasklist)!=0:
                while True:
                    index=input('Enter index of task you wish to delete (or enter exit to return to menu): ')
                    if index.lower()=="exit":
                        print('Returning to main menu..\n')
                        break
                    try:
                        index=int(index)-1
                        if 0<=index<len(tasklist):
                            delete_task(index)
                            break
                        else:
                            print('Index doesnt exist. Try again.\n')
                    except ValueError:
                        print('Invalid input. Enter valid index\n')
                        
        elif choice =='5':
            print('Quitting Task Manager...')
            break
        
        else:
            print('\nInvalid choice. Enter valid function\n')
