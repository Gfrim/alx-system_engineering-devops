#!/usr/bin/python3
import requests
import sys

user_id = sys.argv[1]
response = requests.get(f'https://jsonplaceholder.typicode.com
                        /users {user_id}').json()
tasks = requests.get(f'https://jsonplaceholder.typicode.com/to
                     dos').json()
user_name = response['name']
completed_task = 0
total_task = 0
titles = []

#loop through tasks
for i in tasks:
    if i.get('completed') == True:
        completed_task += 1
        titles.append(i.get('title'))
    total_task += 1

print(f'Employee {user_name} is done with tasks({completed_task}
      /{total_task}).')

#loop through titles
for i in titles:
    print(f'     {i}')

#function to make sure code is not executed when runned
if __name__ == "__main__":
    pass
