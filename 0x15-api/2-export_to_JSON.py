#!/usr/bin/python3
"""
    Export data to JSON format
"""
import csv
import requests
import json
from sys import argv

from requests.api import request


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

def tasks_done(task_list):
    """
        Retrieve done tasks and make a list of it
    """
    done_tasks_list = []

    for tasks in task_list:
        if tasks.get("completed") is True:
            done_tasks_list.append(tasks)
    
    return done_tasks_list

def print_employee_information(employee_name, done_tasks_number, total_tasks_number):
    """
        Print employee name, the tasks that they have done on the total
        number of tasks
    """
    print("Employee {} is done with tasks({}/{})".format(
        employee_name,
        done_tasks_number,
        total_tasks_number,
    ))


def print_done_tasks(done_tasks_list):
    """
        Print the list of done tasks
    """
    for task in done_tasks_list:
        print("\t {}".format(task.get("title")))

def print_done_tasks_by_user(id):
    """
        Returns information about TODO list of a given user ID.
    """

    user_request = request_user(id)
    todo_request = request_todo(id)

    tasks_number = len(todo_request)
    done_tasks_list = tasks_done(todo_request)
    done_tasks_number = len(done_tasks_list)

    print_employee_information(
        user_request.get("name"),
        done_tasks_number,
        tasks_number,
    )

    print_done_tasks(done_tasks_list)


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

    with open("{:s}.csv".format(id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        write_csv_row(id, user_request, todo_request, writer)


def format_todo_employee(user:json, tasks:json):
    """
        Write json formatted tasks
    """
    task_dict = {}
    task_list = []

    for task in tasks:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    task_dict[user.get("id")] = task_list
    return task_dict


def export_employee_json_format(id):
    """
        Export the given data in JSON format
    """
    user_request = request_user(id)
    todo_request = request_todo(id)

    print(len(todo_request))

    task_dict = format_todo_employee(user_request, todo_request)


    with open("{:s}.json".format(id), "w") as file:
        file.write(json.dumps(task_dict))

if __name__ == "__main__":
    export_employee_json_format(argv[1])
