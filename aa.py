import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x450")

def buttonFunc():
    print("here")
    #radio button
    m = method.get()
    if m == "1":
        print("method1")
    elif m == "2":
        print("method2")
    else:
        print("method1 & method2")




button = tk.Button(window, text = "Button", activebackground="red", bg="black", fg="red", activeforeground="black",
height = 15, width = 50, command = buttonFunc)


button.grid(row = 0, column = 0, pady=15)

#radio button

method = tk.StringVar()
tk.Radiobutton(window, text = "method1: ", value = "1", activebackground="red", bg="green",
height = 5, width = 5,  borderwidth=15, variable = method).grid(row = 1, column = 0)

tk.Radiobutton(window, text = "method2: ", value = "2", activebackground="red", bg="green",
height = 5, width = 5,  borderwidth=15, variable = method).grid(row = 1, column = 1, pady = 15)



window.mainloop()