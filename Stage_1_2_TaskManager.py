TASKS_FILE = "mytasks.txt"

tasklist= []

def load_tasks_from_file():
    global tasklist
    tasklist = []
    try:
        with open(TASKS_FILE,"r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" | ")
                if len(parts)==4:
                    tasklist.append({"name":parts[0],"description":parts[1],"priority":parts[2],"end_date":parts[3]})
    except FileNotFoundError:
        tasklist=[]

def save_tasks_to_file():
    with open(TASKS_FILE,"w") as file:
        for task in tasklist:
            file.write(f"{task['name']} | {task['description']} | {task['priority']} | {task['end_date']}\n")

def create_task(name,description,priority,end_date):
    task = {"name":name,"description":description,"priority":priority,"end_date":end_date}
    tasklist.append(task)
    save_tasks_to_file()
    print('Task created successfully!\n')
    
def view_tasks():
    load_tasks_from_file()
    if not tasklist:
        print("No tasks available!\n")
        return
    else:
        print('\nYour Tasks:\n')
        for i in range(len(tasklist)):
            task=tasklist[i]
            print(f"Task {i+1}: {task['name']}\nDescription: {task['description']}\nPriority: {task['priority']}\nDue date: {task['end_date']}\n")
        
def update_task(index,name,description,priority,end_date):
    if 0<=index<len(tasklist):
        tasklist[index] = {"name":name,"description":description,"priority":priority,"end_date":end_date}
        save_tasks_to_file()
        print('Task updated successfully!\n')
    else:
        print('Invalid index. Try Again\n')

def delete_task(index):
    if 0<= index <len(tasklist):
        del tasklist[index]
        save_tasks_to_file()
        print('Task deleted successfully!\n')
    else:
        print('Invalid index. Try Again!\n')
        
if __name__=="__main__":
    load_tasks_from_file()
    while True:
        print('Personal Task Manager')
        print('1. Create Task')
        print('2. View Tasks')
        print('3. Update Task')
        print('4. Delete Task')
        print('5. Quit')
        choice = input('Enter preferred option: ')
        if choice == "1":
            while True:
                name = input('\nEnter name of task (or enter q to return to main menu): ').strip()  # Get task name
                if name =="q":
                    print()
                    break
                else:
                    description = input('Enter description: ').strip()  # Get task description
                    while True:
                        priority = input('Enter priority (High/Low): ').strip().lower()
                        if priority in ["high", "low"]:
                            break
                        print("Invalid priority. Please enter 'High' or 'Low'.")
                    end_date = input('Enter due date: ').strip()
                    create_task(name,description,priority,end_date)
                    break
        elif choice == "2":
            view_tasks()
        elif choice =="3":
            view_tasks()
            if tasklist:
                while True:
                    try:
                        index=input("Enter which task you wish to update (or enter q to return to main menu): ")
                        if index =="q":
                            print("")
                            break
                        else:
                            index=int(index)-1
                        if 0<=index<len(tasklist):
                            name = input('Enter new name for task: ').strip()
                            description = input('Enter new description for task: ').strip()
                            while True:
                                priority = input('Enter priority (High/Low): ').strip().lower()
                                if priority in ["high", "low"]:
                                    break
                                print("Invalid priority. Please enter 'High' or 'Low'.")
                            end_date = input('Enter new end date for task: ').strip()
                            update_task(index,name,description,priority,end_date)
                            break
                        else:
                            print('Invalid Index. Try again\n')
                    except ValueError:
                        print('Invaid Input. Try Again\n')
        elif choice =="4":
            view_tasks()
            if tasklist:
                while True:
                    try:
                        index=input("Enter which task you wish to delete (or enter q to return to main menu): ")
                        if index =="q":
                            print("")
                            break
                        else:
                            index=int(index)-1
                        if 0<=index<len(tasklist):
                            delete_task(index)
                            break
                        else:
                            print('Invalid index. Try Again\n')
                            continue
                    except ValueError:
                        print('Invalid Input. Try Again\n')
                        continue
        elif choice =="5":
            print("Quitting program...")
            break
        else:
            print('\nInvalid choice. Enter valid function')
