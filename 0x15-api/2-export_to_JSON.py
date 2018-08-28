#!/usr/bin/python3
"""
This module contains a function that gathers data from an API
"""
import json
import requests
from sys import argv


def request_data(resource, id):
    """
    Requests information about a given employee from an API
    """
    base = 'https://jsonplaceholder.typicode.com'
    url = '{}{}{}'.format(base, resource, id)
    return requests.get(url).json()


def display_api_data(id):
    """
    Exports requested data to JSON format
    """
    employee = request_data('/users/', id)
    name = employee.get('username')
    todo_list = request_data('/todos?userId=', id)
    tasks = [{'task': td.get('title'), 'completed': td.get('completed'),
              'username': name} for td in todo_list]
    jsonfile = id + '.json'
    data = {id: tasks}
    with open(jsonfile, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        display_api_data(argv[1])
