import os

Tasks_file = "tasks.txt"
def load_tasks():
    if not os.path.exists(Tasks_file):
        return []
    with open(Tasks_file,"r") as file:
        tasks = []
        for line in file:
            tasks.append(line.strip())
            
        return tasks
    

def save_tasks(tasks):
    with open(Tasks_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")



def add_tasks():
    task = input("Please add a new task")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available")
    else:
        for idx in range(len(tasks)):
            print(f"{idx + 1}. {tasks[idx]}")
            

def edit_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No task to edit")
        return
    
    view_tasks()
    try: 
        task_num = int(input("Please enter the number you wish to edit"))
        if 0 < task_num >= len(tasks):
            print(f"tasks(task_num)")
        else:
            print("invalid task number")

        new_task  = input("Please enter the new task")
        with open(Tasks_file, "a") as file:
            file.insert(task_num, new_task)
        save_tasks(tasks)
    except:
        print("something is wrong")





def delete_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No task to delete")
        return
    
    view_tasks()

    try: 
        task_num = int(input("Please enter the number you wish to delete"))
        if 0 < task_num >= len(tasks):
            removed_task = tasks.pop(task_num - 1)

            save_tasks(tasks)
            print(f"Deleted task: {removed_task}")

        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")





def main():
    while True:
        print("\nTo do list Menu:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Edit task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = int(input("Choose an option"))
        
        if choice == 1:
           add_tasks()
        elif choice == 2:
           view_tasks()
        elif choice == 3:
            edit_tasks()
        elif choice == 4:
          delete_tasks()
        elif choice == 5:
          print("Bye for now")
          break
        else:
          print("Please enter a number")

if __name__ == "__main__":
    main()
