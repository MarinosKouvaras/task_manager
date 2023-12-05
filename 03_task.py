task_list = []

def add_task(task):
    task_list.append(task)
    print(f'Task {task} added')

def display_list():
    if not task_list:
        print("Task list is empty")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f' {index}. {task}')

def complete_task(task_index):
    if 1<= task_index <= len(task_list):
        task_list[task_index - 1] += "Completed"
        print('Task marked as completed')
    else:
        print("Invalid option")

def remove_task(task_index):
    if 1<= task_index <= len(task_list):
        removed_task = task_list.pop(task_index -1 )
        print(f'Task {removed_task} removed')
    else:
        print("Invalid option")

def display_menu():
    print("\nOptions:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


while True:
    
    display_menu()
    
    choice = int(input('Select an option'))

    if choice == 1:
        t = input("Enter the task: ")
        add_task(t)
    elif choice == 2:
        display_list()
    elif choice == 3:
        i = int(input("Give task to marked as completed: "))
        complete_task(i)
    elif choice == 4:
        i = int(input("Give task to remove: "))
        remove_task(i)
    elif choice == 5:
        break
    else:
        print("Invalid option")



    
