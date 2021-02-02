#!/usr/bin/python3
"""using an API for a given employee ID returns information abput his/her
TODO list progress"""

import csv
from requests import get
import sys

DOMAIN = 'https://jsonplaceholder.typicode.com/'


def tasks(USER_ID):
    """make GET request to JSONServer"""
    req = get('{}todos?userId={}'.format(DOMAIN, USER_ID))
    obj = req.json()
    userReq = get('{}users?id={}'.format(DOMAIN, USER_ID))
    user = userReq.json()
    USERNAME = user[0].get('username')
    with open("{}.csv".format(USER_ID), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in obj:
            writer.writerow([USER_ID, USERNAME, task.get('completed'),
                             task.get('title')])


if __name__ == '__main__':
    tasks(sys.argv[1])
