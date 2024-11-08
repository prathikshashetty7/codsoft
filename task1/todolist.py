import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task to add.")

def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def open_update_dialog():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_text = tasks[task_index]
        
        # Creating a top-level window for update dialog
        update_dialog = tk.Toplevel(root)
        update_dialog.title("Update Task")
        update_dialog.configure(bg="#f2f2f2")  # background color

        # Label and entry for the update dialog
        tk.Label(update_dialog, text="Update Task:", bg="#f2f2f2", font=("Times New Roman", 12)).pack(pady=5)
        update_entry = tk.Entry(update_dialog, width=30, font=("Times New Roman", 12))
        update_entry.pack(pady=5)
        update_entry.insert(0, task_text)  # Show the current task text in the entry field
        
        # Function to save the updated task
        def save_updated_task():
            new_task = update_entry.get()
            if new_task:
                tasks[task_index] = new_task
                update_task_list()
                update_dialog.destroy()  # Closing the dialog
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")
        
        # Update button 
        save_button = tk.Button(update_dialog, text="Update", command=save_updated_task, bg="#4CAF50", fg="white", font=("Times New Roman", 10, "bold"))
        save_button.pack(pady=10)
        
    else:
        messagebox.showwarning("Warning", "Select a task to update.")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

# Main window setup
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="#efd7f3")  # background color

# Heading label
heading_label = tk.Label(root, text="To-Do List", bg="#efd7f3", fg="#333333", font=("Times New Roman", 16, "bold"))
heading_label.pack(pady=10)

# Frame for the listbox and scrollbar
frame = tk.Frame(root, bg="#efd7f3")
frame.pack(pady=10)

listbox_tasks = tk.Listbox(frame, width=50, height=10, bg="#efd7f3", fg="#333333", font=("Times New Roman", 12))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

# Task entry field
entry_task = tk.Entry(root, width=50, font=("Times New Roman", 12))
entry_task.pack(pady=5)

# Buttons for task operations
button_add_task = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Times New Roman", 10, "bold"))
button_add_task.pack(pady=5)

button_update_task = tk.Button(root, text="Update Task", command=open_update_dialog, bg="#FF9800", fg="white", font=("Times New Roman", 10, "bold"))
button_update_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Times New Roman", 10, "bold"))
button_delete_task.pack(pady=5)

root.mainloop()
