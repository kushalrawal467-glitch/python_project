import time
current_time = time.ctime()

def add_task():
    tasks = {}
    enter_task = ""
    while enter_task != "exit":
        enter_task = input("enter task")
        if enter_task == "exit":
            continue
        enter_task_description = input("enter task description")
        tasks.update({len(tasks)+1:[enter_task,enter_task_description,"task not completed ❌",current_time]})
    return tasks