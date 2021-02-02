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

    userTasks = {USER_ID: tasks}
    with open("{}.json".format(USER_ID), encoding='utf-8', mode='w') as file:
        string = json.dumps(userTasks)
        file.write(string)


if __name__ == '__main__':
    employee_tasks(sys.argv[1])
