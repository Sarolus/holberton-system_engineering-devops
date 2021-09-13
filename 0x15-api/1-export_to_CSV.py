#!/usr/bin/python3
"""
    Export data to CSV format
"""
import csv
import json
import requests
from sys import argv


def request_user(id):
    """
        Returns information about the user corresponding to the
        given user ID
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    data = response.json()

    return data


def request_todo(id):
    """
        Returns information about the todo correspond to the
        given user ID
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    response = requests.get(url)
    data = response.json()

    return data

def write_csv_row(id, user, task_list, writer):
    """
        Write data in a CSV file
    """
    for task in task_list:
        writer.writerow([
            id,
            user.get("username"),
            task.get("completed"),
            task.get("title")
        ])


def export_csv_format(id):
    """
        Export the given data in CSV format
    """
    user_request = request_user(id)
    todo_request = request_todo(id)

    with open("{}.csv".format(id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, lineterminator='\n')
        write_csv_row(id, user_request, todo_request, writer)


if __name__ == "__main__":
    if len(argv) == 2:
        export_csv_format(argv[1])
