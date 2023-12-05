task_list = []

def add_task(task):
    task_list.append(task)
    print(f'Task {task} added')

def display_list():
    if not task_list
    for index, task in enumerate(task_list, start=1):
        print(f' {index}. {task}')

def complete_task(task_index):
    if 1<= task_index <= len(task_list):
        task_list[task_index+1] +="Completed"
        print(f'Task marked as completed')
    else:
        print("Invalid option")


def display_menu(self):
    print("\nOptions:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print()
    
