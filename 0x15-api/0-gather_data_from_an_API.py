#!/usr/bin/python3
"""using an API for a given employee ID returns information abput his/her
TODO list progress"""

from requests import get
import sys

DOMAIN = 'https://jsonplaceholder.typicode.com/'


def get_TODOS(id):
    """make GET request to JSONServer"""
    req = get('{}todos?userId={}'.format(DOMAIN, id))
    obj = req.json()
    userReq = get('{}users?id={}'.format(DOMAIN, id))
    user = userReq.json()
    EMPLOYEE_NAME = user[0].get('name')
    done = get('{}users/{}/todos?completed=true'.format(DOMAIN, id))
    NUMBER_OF_DONE_TASKS = len(done.json())
    TOTAL_NUMBER_OF_TASKS = len(obj)
    output = "Employee {} is done with tasks({}/{}):\n".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(output)
    for TODO in obj:
        if TODO.get('completed') is True:
            TASK_TITLE = TODO.get('title')
            print("\t {}".format(TASK_TITLE))


if __name__ == '__main__':
    get_TODOS(sys.argv[1])
