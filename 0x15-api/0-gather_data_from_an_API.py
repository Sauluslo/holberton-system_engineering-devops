#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import requests as rq
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        id = argv[1]
    URL_td = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    session = rq.Session()
    URL_users = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = session.get(URL_users)
    name = response.json()['name']
    response = session.get(URL_td)
    body = response.json()
    task = []
    for content in body:
        if content['completed']:
            task.append('\t ' + content['title'])
    print("Employee", end=" ")
    print("{} is done with tasks({}/{}):".format(name, len(task), len(body)))
    print(*task, sep='\n')
