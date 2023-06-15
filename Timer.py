from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title("Clock")

def update_time():
    string = time.strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, update_time)

label = Label(root, font=("Arial", 80), background="black", foreground="cyan")
label.pack(anchor='center')

update_time()
root.mainloop()
