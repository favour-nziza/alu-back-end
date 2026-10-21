#!/usr/bin/python3
"""Return information about an employee's TODO list progress using a REST API.

Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys


def main():
    """Fetch the employee and TODO data, then print the progress."""
    if len(sys.argv) < 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
