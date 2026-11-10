#!/usr/bin/python3
"""Export the TODO lists of all employees to todo_all_employees.json."""
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(path):
    """Fetch and decode JSON from the API at the given path."""
    return requests.get(BASE_URL + path).json()


def export_all_todos():
    """Write the TODO tasks of every employee to todo_all_employees.json."""
    users = get_json("/users")
    todos = get_json("/todos")
    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        data[str(user_id)] = [{"username": username,
                               "task": todo.get("title"),
                               "completed": todo.get("completed")}
                              for todo in todos
                              if todo.get("userId") == user_id]
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    export_all_todos()
