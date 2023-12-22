
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

def add_task():
    task_text = entry_task.get()
    if task_text:
        task_frame = tk.Frame(canvas, bg="white")
        task_frame.pack(fill=tk.X, padx=5, pady=2)

        task_label = tk.Label(task_frame, text=task_text, bg="white", width=25)
        task_label.pack(side=tk.LEFT)

        edit_button = tk.Button(task_frame, text="Edit", command=lambda t=task_label: edit_task(t), bg="blue", fg="white")
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda f=task_frame: delete_task(f), bg="red", fg="white")
        delete_button.pack(side=tk.LEFT, padx=5)

        tasks.append(task_frame)
        entry_task.delete(0, tk.END)

def edit_task(task_label):
    updated_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task_label.cget("text"))
    if updated_task:
        task_label.config(text=updated_task)

def delete_task(task_frame):
    task_frame.destroy()
    tasks.remove(task_frame)

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Add a heading
heading = tk.Label(root, text="To_Do_List", font=("Serif", 16), pady=10 )
heading.pack()

# Create an entry field and submit button for adding tasks
entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=add_task, background="green", fg="white")
submit_button.pack()

# Create a canvas to hold tasks
canvas = tk.Canvas(root, width=300, height=200, bg="lightgray")
canvas.pack(padx=10, pady=5)

tasks = []  # Store tasks in a list

# Start the Tkinter event loop
root.mainloop()



