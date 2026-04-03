import task
import json
import argparse

from task import Task

file_path = "task.json"

def load_data():
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tasks file not found.")

def save_data(tasks):
    try:
        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=4)
    except FileNotFoundError:
        print("Tasks file not found.")

def add(name_task):
    task = Task(name_task)
    tasks = load_data()
    tasks[task.id] = task.to_dict()
    save_data(tasks)
    print(f"Task added. ID: {task.id}")


add("Learn Python")
add("Learn CLI")
