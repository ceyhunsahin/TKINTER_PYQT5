import tkinter as tk
from tkinter import ttk

window = tk.Tk() # high Level Window
window.geometry("800x600")


def FileFunction():
    print("here")



menubar = tk.Menu(window)
window.config(menu= menubar)

file = tk.Menu(menubar)
edit = tk.Menu(menubar)

menubar.add_cascade(label="file",menu = file)
menubar.add_cascade(label= "edit",menu = edit)

file.add_command(label = "new file", command = FileFunction)
edit.add_command(label = "undo", command = FileFunction)


window.mainloop()