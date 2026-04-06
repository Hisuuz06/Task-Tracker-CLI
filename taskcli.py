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

def delete(task_id):
    tasks = load_data()
    if task_id in tasks:
        del tasks[task_id]
        save_data(tasks)
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

def update(task_id, new_name):
    tasks = load_data()
    if task_id in tasks:
        task = Task.from_dict(tasks[task_id])
        task.id = task_id
        task.update_name(new_name)
        tasks[task_id] = task.to_dict()
        save_data(tasks)
        print(f"Task with ID {task_id} updated.")
    else:
        print(f"Task with ID {task_id} not found.")


parse = argparse.ArgumentParser(description="Task CLI")
sub = parse.add_subparsers(dest="command")
add_parser = sub.add_parser("add", help="Add a new task")
add_parser.add_argument("name_task", help="Name of the task")
delete_parser = sub.add_parser("delete", help="Delete a task")
delete_parser.add_argument("task_id", help="ID of the task to delete")
update_parser = sub.add_parser("update", help="Update a task")
update_parser.add_argument("task_id", help="ID of the task to update")
update_parser.add_argument("new_name", help="New name for the task")

args = parse.parse_args()
if args.command == "add":
    add(args.name_task)
elif args.command == "delete":
    delete(args.task_id)
elif args.command == "update":
    update(args.task_id, args.new_name)
