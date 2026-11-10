#!/usr/bin/python3
"""Export the TODO list of one employee to a JSON file named USER_ID.json."""
import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(path):
    """Fetch and decode JSON from the API at the given path."""
    return requests.get(BASE_URL + path).json()


def export_to_json(employee_id):
    """Write all TODO tasks of the employee to USER_ID.json."""
    user = get_json("/users/{}".format(employee_id))
    todos = get_json("/todos?userId={}".format(employee_id))
    username = user.get("username")
    tasks = [{"task": todo.get("title"),
              "completed": todo.get("completed"),
              "username": username} for todo in todos]
    data = {str(employee_id): tasks}
    file_name = "{}.json".format(employee_id)
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    export_to_json(int(sys.argv[1]))
