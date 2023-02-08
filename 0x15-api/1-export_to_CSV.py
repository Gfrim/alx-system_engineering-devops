#!/usr/bin/python3
'''Export to CSV'''

import requests
import sys

if __name__ == '__main__':
    param = sys.argv[1]
    user_response = requests.get(f'https://jsonplaceholder.
        typicode.com/users/{param}').json()
    todo_response = requests.get(f'https://jsonplaceholder.
        typicode.com/todos').json()
    username = response['username']

    with open(f'{param}.csv', 'w') as file:
        for task in todo_response:
            file.write(f'"{param}","{username}","{task.get
                ('completed')}","{task.get('title)}"\n')
