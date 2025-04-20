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
    choice = int(input("Enter choice: "))
    return choice


def tasks():
    tasks = dict()
    return tasks


def add_task(tasks):
    while True:
        task = input("Enter a task (type done to stop): ")
        if task.lower() == 'done':
            break
        tasks[task] = 'In Progress'
    return tasks
    # enter_task = True
    # while enter_task:
    #     task = input("Enter a task (type done to stop): ")
    #     if task.lower() == 'done':
    #         enter_task = False
    #         continue
    #     tasks.update({task: 'In Progress'})
    # return tasks


def view_tasks(tasks):
    print("====================================")
    for index, task in enumerate(tasks):
        print(f"[{index+1}]- {tasks[task]} | {task}")
    print('====================================')


def mark_as_done(tasks):
    i = 1
    for k, v in tasks.items():
        if v == 'In Progress':
            print(f"[{i}]- {k}")
            i += 1
    which_task = int(input("Which task you want to mark as done? "))
    i = 1
    for k, v in tasks.items():
        if v == 'In Progress':
            if which_task == i:
                tasks[k] = 'Done'
            i += 1
    return tasks


def delete_task(tasks):
    for i, v in enumerate(tasks):
        print(f"[{i+1}]- {tasks[v]} | {v}")
    which_task = int(input("Which task you want to delete? "))
    for i, v in enumerate(tasks):
        if which_task-1 == i:
            del tasks[v]
            break
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

# def write_to_file(tasks, taskFile):
#     tasks_list = list(tasks)
#     for index, task in enumerate(tasks):
#         if task not in tasks_list:
#             tasks_list.append(task)
#     with open(taskFile, 'a') as file:
#         for index, task in enumerate(tasks):
#             file.write(f"[{index+1}]- {tasks[task]} | {task}")


# file_path = "./tasks.json"
# TASKS_FILE = 'tasks.json'
# run_app = True
# tasks_dic = dict()
# task_file = tasks_file(file_path)
TASKS_FILE = 'tasks.json'

run_app = True
tasks_dic = load_tasks(TASKS_FILE)


while run_app:
    menu()
    choice = make_choice()
    while choice not in [1, 2, 3, 4, 5]:
        print("wrong choice, choose again")
        choice = make_choice()
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
