#!/usr/bin/python3
'''Export to JSON'''

import json
import requests
import sys


if __name__ == '__main__':
    param = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/users"
    url = baseurl + "/" + param

    response = requests.get(url).json()
    username = response['username']

    todourl = url + "/todos"
    tasks = requests.get(todourl).json()

    dictionary = {param: []}
    for task in tasks:
        dictionary[param].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(param), 'w') as filename:
        json.dump(dictionary, filename)
