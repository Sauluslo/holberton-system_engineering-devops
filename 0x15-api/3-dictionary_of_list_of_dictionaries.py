#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import json
import requests as rq

if __name__ == "__main__":
    ids = [i for i in range(1, 11)]
    session = rq.Session()
    info = {}
    for id in ids:
        URL_users = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        URL_ = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        response = session.get(URL_users).json()
        username = response['username']
        task = session.get(URL_).json()
        tasks = []
        info[id] = tasks
        for content in task:
            tasks.append({"username": username,
                          "task": content['title'],
                          "completed": content['completed']})
    with open("todo_all_employees.json", "w") as file:
        json.dump(info, file)
