import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to a file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# Add a new task
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks()
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete a selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Mark a task as done
def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = not tasks[selected_index]["done"]
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"[✔] {task['task']}" if task["done"] else f"[ ] {task['task']}"
        task_listbox.insert(tk.END, display_text)

# Initialize tasks
tasks = load_tasks()

# Create the GUI
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack()

task_listbox = tk.Listbox(root, font=("Arial", 12), height=10)
task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

done_button = tk.Button(root, text="Mark as Done", command=mark_done, font=("Arial", 12))
done_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_button.pack()

# Load existing tasks into the listbox
update_task_list()

# Run the Tkinter event loop
root.mainloop()
