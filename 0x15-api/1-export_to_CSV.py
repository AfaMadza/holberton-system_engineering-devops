#!/usr/bin/python3
"""
This module contains a function that gathers data from an API
"""
import requests
from sys import argv
import csv


def request_data(resource, id):
    """
    Requests information about a given employee from an API
    """
    base = 'https://jsonplaceholder.typicode.com'
    url = '{}{}{}'.format(base, resource, id)
    return requests.get(url).json()


def display_api_data(id):
    """
    Exports requested data to csv
    """
    employee = request_data('/users/', id)
    name = employee.get('username')
    todo_list = request_data('/todos/?userId=', id)
    todo = [[td.get('completed'), td.get('title')] for td in todo_list]
    csvfile = id + '.csv'
    with open(csvfile, 'w') as f:
        file_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in todo:
            file_writer.writerow([id, name, t[0], t[1]])

if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        display_api_data(argv[1])
