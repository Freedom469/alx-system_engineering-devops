#!/usr/bin/python3

"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':

    id = argv[1]

    # construct the URL to retrieve the user's information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        id)

    # make a request to the API and extract the user's username
    response = requests.get(user_url)
    username = response.json().get('username')

    # construct the URL to retrieve the user's tasks
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)

    # make a request to the API and convert the response to a JSON object
    todo = requests.get(todo_url).json()

    # create a new CSV file and write the user's tasks to it
    with open('{}.csv'.format(id), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # loop through the tasks and write each one to a row in the CSV file
        for task in todo:
            task_status = task.get('completed')
            task_title = task.get('title')
            writer.writerow([id, username, task_status, task_title])
