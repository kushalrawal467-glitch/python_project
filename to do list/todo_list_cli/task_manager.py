import time
import json

current_time = time.ctime()


def add_task():
    tasks = {}
    enter_task = ""
    while enter_task != "exit":
        enter_task = input("enter task")
        if enter_task == "exit":
            continue
        enter_task_description = input("enter task description")
        a = tasks.update(
            {
                len(tasks)
                + 1: [
                    enter_task,
                    enter_task_description,
                    "task not completed ❌",
                    current_time,
                ]
            }
        )
        print(a)

    with open("tasks.json", "a") as f:
        data = json.dumps(tasks)
        f.write(data)

    return tasks


def View_tasks():
    with open("tasks.json", "r") as f:
        content = json.load(f)
        for i in content.items():
            print(f"task number is {i[0]} and , task details are {i[1]}")

