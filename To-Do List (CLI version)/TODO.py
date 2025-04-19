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
    task = input("Enter task: ")
    tasks[task] = 'in progress'


def view_tasks(tasks):
    for index, task in enumerate(tasks):
        print("[", index, "]", task)


def mark_as_done(tasks):
    i = 1
    for k, v in tasks:
        if v == 'in progress':
            print(i, k)
            i += 1
    which_task = int(input("Which task you want to mark as done? "))
    i = 1
    for k, v in tasks:
        if v == 'in progress':
            if which_task == i:
                tasks[k] = 'done'
            else:
                i += 1


def delete_task(tasks):
    i = 1
    for k, v in tasks:
        if v == 'in progress':
            print(i, k)
            i += 1
    which_task = int(input("Which task you want to delete? "))
    i = 1
    for k, v in tasks:
        if v == 'in progress':
            if which_task == i:
                del tasks[k]
            else:
                i += 1


run_app = True
while run_app:
    menu()
    tasks_dic = tasks()
    choice = make_choice()
    if choice not in [1, 2, 3, 4, 5]:
        print("wrong choice, choose again")
        choice = make_choice()
    if choice == 1:
        add_task(tasks_dic)
    elif choice == 2:
        view_tasks(tasks_dic)
    elif choice == 3:
        mark_as_done(tasks_dic)
    elif choice == 4:
        delete_task(tasks_dic)
    else:
        run_app = False
