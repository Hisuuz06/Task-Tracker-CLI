import task
from task import Task
import json
import argparse

file_path = "task.json"

def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tasks file not found.")

def save_data(data, file_path):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f)
    except FileNotFoundError:
        print("Tasks file not found.")

save_data({"hi" : "hello"}, file_path)
task_data = load_data(file_path)
print(task_data)
