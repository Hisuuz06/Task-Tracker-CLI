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
    max_id = int(max(tasks.keys(), default=0))
    task.id = max_id + 1
    tasks[task.id] = task.to_dict()
    save_data(tasks)
    print(f"Task \"{task.name}\" added. ID: {task.id}")


parse = argparse.ArgumentParser(description="Task CLI")
sub = parse.add_subparsers(dest="command")
add_parser = sub.add_parser("add", help="Add a new task")
add_parser.add_argument("name_task", help="Name of the task")
args = parse.parse_args()
if args.command == "add":
    add(args.name_task)
