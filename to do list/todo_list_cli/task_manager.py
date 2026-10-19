import time
current_time = time.ctime()

def add_task():
    task = {}
    task_num = len(task)+1
    option = input("enter the option sir 'enter task' OR 'exit'")
    if option == "enter task":
        task_name = input("enter the task : ")
        description = input("enter the task description : ")
        task.update({task_num:[f"task_name : {task_name}",f"description : {description}",f"created : {current_time}"]})
    elif option == "EXit":
        print("thank for visiting")
    else:
        print("program error")
    return task

add = add_task()
print(add)

def view_task(task_dict:dict):
    for i in task_dict:
        print(f"task number is {i} and detail are {task_dict.values()}")

view_task(add)

def complete_task(task_dict:dict):
    for i in task_dict.items():
        print(i)
    select_complete_task = int(input("enter the task number"))
    task_dict[select_complete_task].append("complete_task : ✅")
    print(task_dict)

complete_task(add)


def delete_task(task_dict:dict):
    delete_task_list = []
    for i in task_dict.items():
        print(i)
    select_del_task = int(input("enter the task number"))
    task_dict.pop(select_del_task)
    print(task_dict)

delete_task(add)


# def search_task():
#     pass

# def filter_task():
#     pass