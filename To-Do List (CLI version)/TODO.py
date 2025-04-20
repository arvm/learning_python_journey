import os
import json


def menu():
    print("==== TO-DO APP ====")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def make_choice():
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_task(tasks):
    while True:
        task = input("Enter a task (type done to stop): ").strip()
        if task.lower() == 'done':
            break
        if not task:
            print("Task cannot be empty.")
        elif task in tasks:
            print("Task already exists.")
        else:
            tasks[task] = 'In Progress'
    return tasks


def view_tasks(tasks):
    print("====================================")
    for index, task in enumerate(tasks):
        status_symbol = '✅' if tasks[task] == 'Done' else '❌'
        print(f"[{index+1}]- {status_symbol} {task}")
        # print(f"[{index+1}]- {tasks[task]} | {task}")
    print('====================================')


def mark_as_done(tasks):
    in_progress_tasks = [task for task,
                         status in tasks.items() if status == 'In Progress']

    if not in_progress_tasks:
        print("No tasks to mark as done.")
        return tasks

    for i, task in enumerate(in_progress_tasks, 1):
        print(f"[{i}] - {task}")

    while True:
        try:
            choice = int(input("Which task do you want to mark as done? "))
            if 1 <= choice <= len(in_progress_tasks):
                tasks[in_progress_tasks[choice - 1]] = 'Done'
                break
            else:
                print(
                    f"Please enter a number between 1 and {len(in_progress_tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return tasks


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return tasks

    task_list = list(tasks.keys())

    for i, task in enumerate(task_list, 1):
        status_symbol = '✅' if tasks[task] == 'Done' else '❌'
        print(f"[{i}] - {status_symbol} | {task}")

    while True:
        try:
            choice = int(input("Which task do you want to delete? "))
            if 1 <= choice <= len(task_list):
                del tasks[task_list[choice - 1]]
                break
            else:
                print(f"Please enter a number between 1 and {len(task_list)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return tasks


def tasks_file(path):
    isFile = os.path.isfile(path)
    if not isFile:
        with open("tasks.json", 'x') as file:
            file.write("{}")


def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}


def save_tasks(tasks, file_path):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)


TASKS_FILE = 'tasks.json'

run_app = True
tasks_dic = load_tasks(TASKS_FILE)


while run_app:
    menu()
    choice = make_choice()
    # while choice not in [1, 2, 3, 4, 5]:
    #     print("wrong choice, choose again")
    #     choice = make_choice()
    if choice == 1:
        add_task(tasks_dic)
        save_tasks(tasks_dic, TASKS_FILE)
    elif choice == 2:
        view_tasks(tasks_dic)
    elif choice == 3:
        mark_as_done(tasks_dic)
        save_tasks(tasks_dic, TASKS_FILE)
    elif choice == 4:
        delete_task(tasks_dic)
        save_tasks(tasks_dic, TASKS_FILE)
    else:
        run_app = False
