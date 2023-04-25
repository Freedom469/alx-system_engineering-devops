#!/usr/bin/python3

"""
This script retrieves information about an employee
from the JSONPlaceholder API
and outputs the number of completed tasks
and a list of completed tasks.
"""

import requests
import sys

""" Check if the script is being run directly """
if __name__ == '__main__':

    """ Get the employee ID from the command line argument"""
    employee_ID = int(sys.argv[1])

    """ Construct the URL to retrieve the employee's information """
    user_url = 'https://jsonplaceholder.typicode.com\
                /users/{}'.format(employee_ID)

    """ Make a request to the API and convert the response to a JSON object """
    user_response = requests.get(user_url)
    user_data = user_response.json()

    """ Extract the employee's name from the JSON object """
    employee_name = user_data.get('name')

    """ Construct the URL to retrieve the employee's tasks """
    todo_url = 'https://jsonplaceholder.typicode.com\
                /todos?userId={}'.format(employee_ID)

    """ Make a request to the API and convert the response to a JSON object """
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    """ Initialize counters and lists to keep track of the number
    of completed tasks and the list of completed tasks """
    total_tasks = 0
    num_completed_tasks = 0
    completed_tasks = []

    """ Loop through the tasks and count the number of completed
    tasks and add the titles of completed tasks to the list """
    for task in todo_data:
        total_tasks += 1
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
            num_completed_tasks += 1

    """ Output the employee's name, the number of
    completed tasks, and the list of completed tasks"""
    print("Employee {} is done with tasks({}/{}):".format
          (employee_name, num_completed_tasks, total_tasks))
    for task_title in completed_tasks:
        print("\t {}".format(task_title))
