# Importing all the necessary modules
from tkinter import *
import tkinter.messagebox

# Function to add a new task and also cheaking some condithion
def entertask():
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some task")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

# Function to delete a selected task
def deletetask():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])

# Function to mark a task as completed
def markcompleted():
    marked = listbox_task.curselection()
    if marked:
        temp = marked[0]
        temp_marked = listbox_task.get(temp)
        temp_marked += "   ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)

# Create the main window and defigning the name of the app
window = Tk()
window.title("75day HARD To-Do List APP")

# Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to hold items and also defigning the color, height, width, and font style
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="LucidaGrande")
listbox_task.pack(side=LEFT)

# Scrollbar for the app
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Buttons used to add mark and to delete any task

# Enter task
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

# Delete task
delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

# Mark as read 
mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)
# Calling the main function to execute the whole program
window.mainloop()
