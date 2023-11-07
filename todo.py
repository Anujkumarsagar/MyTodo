
import tkinter as tk

from tkinter import Scrollbar
from PIL import ImageTk , Image

# Create the tkinter root window
root = tk.Tk()
img = Image.open("ogo.png")
logo_img = img.resize((16, 16))
logo = ImageTk.PhotoImage(image=logo_img)
root.iconphoto(False, logo)
root.title("MyTodo")



def add_task():
    global task_number  # Use t
    task = input_task.get()
    if task :
        task_text.insert(tk.END,str(task_number)+ ":" + task )
        input_task.delete(0,tk.END)
        task_number += 1
def deleted_selected_task():
    selected = task_text.curselection()
    if selected:
        task_text.delete(selected)


# Create a frame to hold the background image

original_image = Image.open("image_bg.png")
new_w = 700
new_h = 400
resize_image = original_image.resize((new_w,new_h))
image = ImageTk.PhotoImage(image=resize_image)
frame = tk.Frame(root , relief="raised", borderwidth=2,)
# Configure the frame for expansion
frame.pack(fill="both", expand=True)

label = tk.Label(frame, image=image)
label.pack()

Task = tk.Label(label, text="Task :", font=("Arial", 15), bg="#ca81d3")
Task.place(x=200, y=25)


input_task = tk.Entry(label, width=15, font=("Comic Sans MS", 15, "bold"),bg="#dcbaf0")
input_task.place(x=260, y=20)


task_text = tk.Listbox(label,height=15, width=34,bg="#d29fea")
task_text.place(x=247, y=78)
# Task.config(bg='systemTransparent')

button1 = tk.Button(label, text="Delete", font=("arial", 12),cursor="hand2",border=0.2,command=deleted_selected_task,bg="#e69aa6",activebackground="#974ce1")
button1.place(x=290, y=350)

button1 = tk.Button(label, text="Add", font=("arial", 12),cursor="hand2",border=0.2,command=add_task,bg="#e69aa6",activebackground="#974ce1")
button1.place(x=370, y=350)

task_number = 1  # Initialize the task number

# Run the tkinter main loop to display the window
root.mainloop()
