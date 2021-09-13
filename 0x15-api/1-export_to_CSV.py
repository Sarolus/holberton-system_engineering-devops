
#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeID)).json().get('username')
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employeeID)).json()

    with open("{}.csv".format(employeeID), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employeeID, username, task.get("completed"), task.get("title")]
         ) for task in todo]