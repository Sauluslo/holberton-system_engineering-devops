#!/usr/bin/python3
""" get tasks from user and export to json file"""

from requests import get
import json
import sys


DOMAIN = 'https://jsonplaceholder.typicode.com/'


def employee_tasks(USER_ID):
    """OJ yeah one more time"""
    req = get('{}todos?userId={}'.format(DOMAIN, USER_ID))
    obj = req.json()
    userReq = get('{}users?id={}'.format(DOMAIN, USER_ID))
    user = userReq.json()
    USERNAME = user[0].get('username')
    tasks = []
    for task in obj:
        TASK_TITLE = task.get('title')
        TASK_COMPLETED_STATUS = task.get('completed')
        dictionary = {
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS,
                    "username": USERNAME
                    }
        tasks.append(dictionary)
    return json.dumps(tasks)


def todo_all_employees():
    """Do ya think im sexy"""

    with open("todo_all_employees.json", encoding='utf-8', mode='w') as file:
        tasks = {}
        for i in range(1, 10):
            userTasks = employee_tasks(i)
            tasks[i] = userTasks
        file.write(str(tasks))
if __name__ == '__main__':
    todo_all_employees()
