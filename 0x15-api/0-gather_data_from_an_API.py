#!/usr/bin/python3
"""
This module contains a function that gathers data from an API
"""
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
    Displays requested info from API
    """
    employee = request_data('/users/', id)
    name = employee.get('name')
    todo_list = request_data('/todos?userId=', id)
    all_td = len(todo_list)
    done = [td.get('title') for td in todo_list if td.get('completed')]
    print ("Employee {} is done with tasks({}/{}):".format(name, done, all_td))
    for task in done:
        print('\t {}'.format(task))

if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        display_api_data(argv[1])
